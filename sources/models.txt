.. _models:

Models
======

Panya is made up of a collection of standalone Django applications, each providing various models. This document describes models included in the standard set of Panya apps.

.. contents:: Contents
    :depth: 5


.. _models-category:

Category Models
---------------

The following models are contained in ``category.models``.

.. _models-category-category:

Category
++++++++

.. _models-category-category-fields:

fields
~~~~~~

.. _models-category-category-field-title:

title
*****
*models.CharField*

Short descriptive title for the category.

.. _models-category-category-field-slug:

slug
****
*models.SlugField*

Short descriptive unique slug for this category for use in URLs.

.. _models-category-tag:

Tag
+++

.. _models-category-tag-fields:

fields
~~~~~~

.. _models-category-tag-field-title:

title
*****
*models.CharField*

Short descriptive title for the tag.

.. _models-category-tag-field-slug:

slug
****
*models.SlugField*

Short descriptive unique slug for this tag for use in URLs.

.. _models-category-tag-field-categories:

categories
**********
*models.ManyToManyField*

:ref:`Categories <models-category-category>` to which this tag belongs. Tags can belong to multiple categories. Tags are used as a means to sub-categorize objects within categories.

.. _models-panya:

Panya Models
------------

The following models are contained in ``panya.models``.

.. _models-panya-modelbase:

ModelBase
+++++++++

ModelBase provides default CMS behaviour for inherting models. All content types should inherit from ModelBase.

.. _models-panya-modelbase-fields:

fields
~~~~~~

.. _models-panya-modelbase-fields-anonymous_comments:

anonymous_comments
******************

*models.BooleanField*

Enable anonymous commenting for this object. Used by ModelBase's :ref:`can_comment <models-panya-modelbase-methods-can_comment>` method to determine whether or not anonymous users can comment on the given object.

.. _models-panya-modelbase-fields-anonymous_likes:

anonymous_likes
***************
*models.BooleanField*

Enable anonymous liking for this item. Used by ModelBase's :ref:`can_vote <models-panya-modelbase-methods-can_vote>` method to determine whether or not anonymous users can like the given object.

.. _models-panya-modelbase-fields-categories:

categories
**********     
*models.ManyToManyField*

Foreign key to :ref:`Category <models-category>`. Objects can be categorized by more than one category.  

.. _models-panya-modelbase-fields-class_name:

class_name
**********
*models.CharField*

Stores the object's class name. The is automatically set when the object is initially saved.
Used by the :ref:`as_leaf_class <models-panya-modelbase-methods-as_leaf_class>` method in conjunction with :ref:`content_type <models-panya-modelbase-fields-content_type>` to traverse to an inheriting child object.

.. _models-panya-modelbase-fields-content_type:

content_type
************
*models.ForeignKey*

Foreign key to the content object's content type. The is automatically set when the item is initially saved.
Used by the :ref:`as_leaf_class <models-panya-modelbase-methods-as_leaf_class>` method in conjunction with :ref:`class_name <models-panya-modelbase-fields-class_name>` to traverse to an inheriting child object.

.. _models-panya-modelbase-fields-comments_closed:

comments_closed
***************
*models.BooleanField*

Close commenting for this item. Used by ModelBase's :ref:`can_comment <models-panya-modelbase-methods-can_comment>` method to determine whether or not users can comment on the given object. Comments will still display, but users won't be able to add new comments.

.. _models-panya-modelbase-fields-comments_enabled:

comments_enabled
****************
*models.BooleanField*

Enable commenting for this object. Used by ModelBase's :ref:`can_vote <models-panya-modelbase-methods-can_vote>` method to determine whether or not users can comment on the given object. If this is ``False`` you should not display comments for the given object.

.. _models-panya-modelbase-fields-created:

created
*******
*models.DateTimeField*

Date and time on which this item was created. This is automatically set on creation, but can be changed subsequently through admin.

.. _models-panya-modelbase-fields-description:

description
***********
*models.TextField*

A short description. More verbose than the :ref:`title <models-panya-modelbase-fields-title>` but limited to one or two sentences.

.. _models-panya-modelbase-fields-likes_closed:

likes_closed
************
*models.BooleanField*

Close liking for this item. Used by ModelBase's :ref:`can_vote <models-panya-modelbase-methods-can_vote>` method to determine whether or not users can like the given object. Likes will still display, but users won't be able to like the item anymore.

.. _models-panya-modelbase-fields-likes_enabled:

likes_enabled
*************
*models.BooleanField*
        
Enable liking for this item. Used by ModelBase's :ref:`can_vote <models-panya-modelbase-methods-can_vote>` method to determine whether or not users can like the given object. If this is ``False`` you should not to display likes for the given object.

.. _models-panya-modelbase-fields-modified:

modified
********
*models.DateTimeField*

Date and time on which this item was last modified. This is automatically set each time the item is saved.

.. _models-panya-modelbase-fields-owner:

owner
*****
*models.ForeignKey*

Foreign key to content object owner's user. The owner is automatically set to the logged in user when the item is initially saved.

.. _models-panya-modelbase-fields-publish_on:

publish_on
**********
*models.DateTimeField*

Date and time on which to publish this item (state will change to 'published').

.. _models-panya-modelbase-fields-retract_on:

retract_on
**********
*models.DateTimeField*

Date and time on which to retract this item (state will change to 'unpublished').

.. _models-panya-modelbase-fields-sites:

sites
*****
*models.ManyToManyField*

Makes item eligible to be published on selected sites, see `Django's sites framework <http://docs.djangoproject.com/en/dev/ref/contrib/sites/>`_. This is field used by the :ref:`permitted manager <managers-panya-permitted>` to limit content access. The permitted manager's queryset will only include objects which have a site set corresponding to the `SITE_ID Django setting <http://docs.djangoproject.com/en/dev/ref/settings#site-id>`_.

.. _models-panya-modelbase-fields-slug:

slug
****
*models.SlugField*

Unique slug for the content object generated from the :ref:`title field<models-panya-modelbase-fields-title>` when the item is initially saved. Guaranteed to be unique for all models inheriting from ModelBase.

.. _models-panya-modelbase-fields-state:

state
*****
*models.CharField*

Stores the current state of the content object, with state being one of the following choices::

    ('unpublished', 'Unpublished'),
    ('published', 'Published'),
    ('staging', 'Staging'),

A content object's state is used by :ref:`ModelBase's is_permitted property <models-panya-modelbase-methods-is_permitted>` and the :ref:`permitted manager <managers-panya-permitted>` to limit content access. The permitted manager's queryset will never include an object with a state of ``unpublished``. In the same way ModelBase's is_permitted property will always be ``False`` for objects with a state of ``unpublished``.

.. _models-panya-modelbase-fields-tags:

tags
****
*models.ManyToManyField*

Foreign key to :ref:`Tag <models-category-tag>`. Objects can be tagged by more than one tag.  

.. _models-panya-modelbase-fields-title:

title
*****
*models.CharField*

A short descriptive title. 

.. _models-panya-modelbase-managers:

managers
~~~~~~~~

.. _models-panya-modelbase-managers-permitted:

permitted
*********
Returns a queryset containing only permitted objects, see the :ref:`PermittedManager <managers-panya-permitted>`.

.. _models-panya-modelbase-methods:

methods
~~~~~~~

.. _models-panya-modelbase-methods-as_leaf_class:

as_leaf_class
*************
Returns the leaf class object no matter where the calling instance is in the inheritance hierarchy.

For instance consider the following inheritance structure::

    from panya.models import ModelBase

    class SomeContentType(ModelBase):
        pass

When you use a ModelBase manager you'll receive objects of class ModelBase. To traverse to an object's inheriting child class call the as_leaf_class method, i.e.::

    >>> SomeContentType(id=1, title='SomeContentType Title').save()
    >>> ModelBase.objects.get(id=1)
    <ModelBase: SomeContentTypeTitle>
    >>> ModelBase.objects.get(id=1).as_leaf_class()
    <SomeContentType: SomeContentTypeTitle>

This enables you to query against ModelBase for a wide range of content types whilst still being able to traverse to inheriting models.

.. _models-panya-modelbase-methods-can_comment:

can_comment
***********
Determines whether or not the requesting user can comment on the object, based on ModelBase's :ref:`anonymous_comments <models-panya-modelbase-fields-anonymous_comments>`, :ref:`comments_closed <models-panya-modelbase-fields-comments_closed>` and :ref:`comments_enabled <models-panya-modelbase-fields-comments_enabled>` fields. 

.. _models-panya-modelbase-methods-can_vote:

can_vote
********
Determines whether or not the requesting user can vote on the object, based on ModelBase's :ref:`anonymous_likes <models-panya-modelbase-fields-anonymous_likes>`, :ref:`likes_closed <models-panya-modelbase-fields-likes_closed>` and :ref:`likes_enabled <models-panya-modelbase-fields-likes_enabled>` fields. Returns a bool as well as a string indicating the current vote status, with vote status being one of: ``'closed', 'disabled', 'auth_required', 'can_vote', 'voted'``.

.. _models-panya-modelbase-methods-comment_count:

comment_count
*************
A property calculating total number of comments made on the objects underlying ModelBase object. Comments should always :ref:`reference underlying ModelBase objects <models-panya-modelbase-methods-modelbase_obj>` in order to enable consistent behaviour of this method regardless of where the calling instance is in the inheritance hierarchy.

.. _models-panya-modelbase-methods-is_permitted:

is_permitted
************
A property determining whether or not the given object is accesible based on its :ref:`state <models-panya-modelbase-fields-state>`. Result is determined as follows:

    #. If the object has a state of ``unpublished``, return ``False``. 
    #. If the object has a state of ``published`` and a :ref:`site <models-panya-modelbase-fields-sites>` set corresponding to the `SITE_ID Django setting <http://docs.djangoproject.com/en/dev/ref/settings#site-id>`_, return ``True``.
    #. If the setting :ref:`STAGING <settings-staging>` is ``True`` and the object has a state of ``staging`` as well as a :ref:`site <models-panya-modelbase-fields-sites>` set corresponding to the `SITE_ID Django setting <http://docs.djangoproject.com/en/dev/ref/settings#site-id>`_, return ``True``.
    #. In all other cases return ``False``.


.. _models-panya-modelbase-methods-modelbase_obj:

modelbase_obj
*************
Returns a ModelBase object no matter where the calling instance is in the inheritance hierarchy. Can be considered the reverse of :ref:`as_leaf_class <models-panya-modelbase-methods-as_leaf_class>`.

For instance consider the following inheritance structure::

    from panya.models import ModelBase

    class SomeContentType(ModelBase):
        pass

When you use a SomeContentType manager you'll receive objects of class SomeContentType. The modelbase_obj property points to the object's ModelBase parent object, i.e.::

    >>> SomeContentType(id=1, title='SomeContentType Title').save()
    >>> SomeContentType.objects.get(id=1)
    <SomeContentType: SomeContentTypeTitle>
    >>> SomeContentType.objects.get(id=1).modelbase_obj
    <ModelBase: SomeContentTypeTitle>

This is used to make objects behave consistently regardless of content type.

.. _models-panya-modelbase-methods-vote_total:

vote_total
**********
A property calculating vote total as total_upvotes - total_downvotes.  See `django-secretballot <http://pypi.python.org/pypi/django-secretballot>`_.

