'''
Created on 19 Jul 2011

@author: euan
'''
from django.db import models

from panya.models import PublisherBase

from ckeditor.fields import RichTextField

from caching.base import CachingMixin, CachingManager

#==============================================================================
class ContentBlock(PublisherBase, CachingMixin):
    objects = CachingManager()
    
    name = models.CharField(max_length=255 ,blank=True, null=True)
    key = models.CharField(max_length=255, unique=True)
    content = RichTextField()
    
    #--------------------------------------------------------------------------
    def __unicode__(self):
        return unicode(self.name)

    #==========================================================================
    class Meta:
        ordering = ('key',)