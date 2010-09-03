.. _template-context-processors:

Template-Context Processors
===========================

Various Panya applications provide `template-context processors <http://docs.djangoproject.com/en/dev/ref/settings/?from=olddocs#template-context-processors>`_. This document describes those template context processors provided by the standard set of Panya apps.

.. contents:: Contents
    :depth: 5

.. _template-context-processors-panya:

Panya Template-Context Processors
---------------------------------

The following template context processors are contained in ``panya.context_processors``.

.. _template-context-processors-panya-site:

site
++++

Adds the current site object to context. See Django's `site framework docs <http://docs.djangoproject.com/en/dev/ref/contrib/sites/>`_ for more info.
