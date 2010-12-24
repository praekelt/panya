import datetime

from django.conf import settings
from django.db import models

import caching.base

class PermittedManager(models.Manager):
    def get_query_set(self):
        # get base queryset and exclude based on state
        queryset = super(PermittedManager, self).get_query_set().exclude(state='unpublished')

        # exclude objects in staging state if not in staging mode (settings.STAGING = False)
        if not getattr(settings, 'STAGING', False):
            queryset = queryset.exclude(state='staging')

        # filter objects for current site 
        queryset = queryset.filter(sites__id__exact=settings.SITE_ID)
        return queryset

#==============================================================================
class PublisherManager(caching.base.CachingManager):
    def get_query_set(self):
        queryset = super(PublisherManager, self).get_query_set().exclude(state='unpublished')

        if not getattr(settings, 'STAGING', False):
            queryset = queryset.filter(state='published')
            queryset = queryset.exclude(publish_on__gt=datetime.datetime.now())
            queryset = queryset.exclude(retract_on__lte=datetime.datetime.now())
            
        return queryset.filter(sites__id__exact=settings.SITE_ID)