Models
======

Panya is made up of a collection of standalone Django applications, each providing various models. This document describes models included in the standard set of Panya apps.

Panya Models
------------

The following models are contained in ``panya.models``.

.. _models-modelbase:
ModelBase
+++++++++

ModelBase provides default CMS behaviour for inherting models. All content types should inherit from ModelBase.

fields
~~~~~~

.. _models-modelbase-fields-state:
state
~~~~~
*models.CharField*

Stores the current state of the content object, with state being one of the following choices::

    ('unpublished', 'Unpublished'),
    ('published', 'Published'),
    ('staging', 'Staging'),

A content object's state is used by the :ref:`permitted manager <managers-panya-permitted>` to limit content access. The permitted manager's queryset will never include an object with a state of ``unpublished``. 

.. _models-modelbase-fields-sites:
sites
~~~~~
*models.ManyToManyField*

Makes item eligible to be published on selected sites, see `Django's sites framework <http://docs.djangoproject.com/en/dev/ref/contrib/sites/>`_. This is field used by the :ref:`permitted manager <managers-panya-permitted>` to limit content access. The permitted manager's queryset will only include objects which have a site set corresponding to the `SITE_ID Django setting <http://docs.djangoproject.com/en/dev/ref/settings#site-id>`_.
