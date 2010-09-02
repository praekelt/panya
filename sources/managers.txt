.. _managers:

Managers
========

This document describes custom managers provided by the standard set of Panya apps. 

.. contents:: Contents
    :depth: 5


.. _managers-panya:

Panya Managers
--------------

The following managers are contained in ``panya.managers``.

.. _managers-panya-permitted:

PermittedManager
++++++++++++++++

The permitted manager is used to limit queryset results based on object state and site eligibility, see :ref:`ModelBase's <models-panya-modelbase>` :ref:`state <models-panya-modelbase-fields-state>` and :ref:`sites <models-panya-modelbase-fields-sites>` fields. The managers resulting queryset is determined by the following rules:

    #. Exclude all objects which have a state of ``unpublished``. 
    #. Only include those objects which have a state of ``published`` and a site set corresponding to the `SITE_ID Django setting <http://docs.djangoproject.com/en/dev/ref/settings#site-id>`_.
    #. If the setting :ref:`STAGING <settings-staging>` is ``True``, also include those objects which have a state of ``staging``.

The permitted manager is accessible on the :ref:`Panya ModelBase model's<models-panya-modelbase>` ``permitted`` member. 
