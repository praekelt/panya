'''
Created on 19 Jul 2011

@author: euan
'''
from django import template

from general.models import ContentBlock

register = template.Library()

#------------------------------------------------------------------------------
@register.inclusion_tag('contentblocks/templatetags/content_block.html', takes_context=True)
def content_block(context, key):
    try:
        object = ContentBlock.published.get(key=key)
    except:
        object = None

    return { 'content_block': object }