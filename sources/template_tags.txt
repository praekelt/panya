.. _template-tags:

Template Tags
=============

This document describes template tags provided by the standard set of Panya apps. A template tag takes some input and returns a modified result. For tags returning HTML structures for inclusion within templates see :ref:`inclusion tags <inclusion-tags>`. 

.. contents:: Contents
    :depth: 5

.. _template-tags-panya:

Panya Template Tags
-------------------

The following tags are contained in ``panya.templatetags.panya_template_tags``. 

To activate them use ``{% load panya_template_tags %}`` in your template.

.. _template-tags-panya-humanize_time_diff:

humanize_time_diff
++++++++++++++++++
 
Outputs a humanized string representing the time difference between now and the provided datetime. A suffix as provided is appended to the output.

**Sample usage**::

    {% humanize_time_diff object.created 'ago' %}

**Sample output**::

    4 days ago

.. _template-tags-panya-smart_query_string:

smart_query_string
++++++++++++++++++
 
Outputs current GET query string with additions appended and existing parameters updated. Parameters and their values are provided in token pairs. 

**Sample usage**::
    
    {% smart_query_string 'page' '2' 'color' 'red' %}

**Consider the following example:**

A page is accessed with the following GET query string::
    
    ?page=2

If you want to update the query string to have a ``page`` value of ``3`` and add another parameter called ``color`` set to ``red``, you would call the ``smart_query_string`` tag as follows::

    {% smart_query_string 'page' '3' 'color' 'red' %}

Which would output::

    ?page=3&color=red
   
Note how the existing ``page`` parameter was updated, and the new ``color`` parameter was appended to the query string.


.. _template-tags-panya-smart_url:

smart_url
+++++++++

Outputs a URL as determined by a provided callable for a provided object.

**Sample usage**::

    {% smart_url url_callable object %}

The provided callable should accept an ``obj`` parameter, which is the object provided in the tag.

**Consider the following example:**

A callable returning a URL has been defined as follows::

    class SectionURL(object):
        def __call__(self, obj=None):
            if obj.categories.filter(title__iexact='news'):
                return reverse('news_detail', kwargs={'slug': obj.slug})
            else:
                return object.get_absolute_url()

When this callable is used with the ``smart_url`` tag a URL pointing to the ``news_detail`` view would be returned if the object was categorized  as *News*. Otherwise the object's normal ``get_absolute_url`` method output is returned. 

This tag enables objects to arbitrarily link to various URLs. Specialized generic URL callables can be created in view code without having to modify model specific ``get_absolute_url`` methods.
