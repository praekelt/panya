'''
Created on 19 Jul 2011

@author: euan
'''
from django import template

from contentblocks.models import ContentBlock

register = template.Library()

#------------------------------------------------------------------------------
@register.inclusion_tag('contentblocks/templatetags/content_block.html', takes_context=True)
def content_block(context, key):
    try:
        return { 'content_block': ContentBlock.published.get(contentblock__key=key).as_leaf_class() }
    except:
        return { 'content_block': None }