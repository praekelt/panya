import inspect
import re
import types

from django.db.models import Q
from django.db.utils import IntegrityError
from django.template.defaultfilters import slugify

def generate_slug(obj, text, tail_number=0):
    from panya.models import ModelBase
    """
    Returns a new unique slug. Object must provide a SlugField called slug.
    URL friendly slugs are generated using django.template.defaultfilters' slugify.
    Numbers are added to the end of slugs for uniqueness.
    """
    # use django slugify filter to slugify
    slug = slugify(text)
    
    existing_slugs = [item.slug for item in ModelBase.objects.filter(slug__regex=r'^%s(-\d+)?' % slug).exclude(id=obj.id)]
    
    tail_number = 0
    new_slug = slug
    while new_slug in existing_slugs:
        new_slug = slugify("%s-%s" % (slug, tail_number))
        tail_number += 1
    
    return new_slug

def modify_class(original_class, modifier_class, override=True):
    """
    Adds class methods from modifier_class to original_class.
    If override is True existing methods in original_class are overriden by those provided by modifier_class.
    """
    # get members to add
    modifier_methods = inspect.getmembers(modifier_class, inspect.ismethod)
    
    # set methods
    for method_tuple in modifier_methods:
        name = method_tuple[0]
        method = method_tuple[1]
        if isinstance(method, types.UnboundMethodType):
            if hasattr(original_class, name) and not override:
                return None
            else:
                setattr(original_class, name, method.im_func)

def normalize_query(query_string,
                    findterms=re.compile(r'"([^"]+)"|(\S+)').findall,
                    normspace=re.compile(r'\s{2,}').sub):
    """
    Splits the query string in invidual keywords, getting rid of unecessary spaces
    and grouping quoted words together.
    Example:
      
    >>> normalize_query('  some random  words "with   quotes  " and   spaces')
    ['some', 'random', 'words', 'with quotes', 'and', 'spaces']
    """
    
    return [normspace(' ', (t[0] or t[1]).strip()) for t in findterms(query_string)] 

def get_query(query_string, search_fields):
    """
    Returns a query, that is a combination of Q objects. That combination
    aims to search keywords within a model by testing the given search fields.
    search_fields should be something like: [('title', 'iexact'), ('content', 'icontains'), ]
    """
    query = None # Query to search for every search term        
    terms = normalize_query(query_string)
    for term in terms:
        or_query = None # Query to search for a given term in each field
        for field in search_fields:
            q = Q(**{"%s__%s" % (field[0], field[1]): term})
            if or_query is None:
                or_query = q
            else:
                or_query = or_query | q
        if query is None:
            query = or_query
        else:
            query = query & or_query
    return query
