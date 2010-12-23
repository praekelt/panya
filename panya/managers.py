from django.conf import settings
from django.db import models

import caching.base

class PublisherManager(caching.base.CachingManager):
    def get_query_set(self):
        queryset = super(PublisherManager, self).get_query_set().exclude(state='unpublished')

        if not getattr(settings, 'STAGING', False):
            queryset = queryset.filter(state='published')
            queryset = queryset.exclude(publish_on__gt=datetime.datetime.now())
            queryset = queryset.exclude(retract_on__lte=datetime.datetime.now())
            
        return queryset.filter(sites__id__exact=settings.SITE_ID)
