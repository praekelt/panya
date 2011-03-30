Welcome to Panya's documentation!
=================================

Panya is a set of Django applications that aims to make your life even easier than it already is. It means “blink” in seSotho. Panya makes rich portal development a breeze.    

.. contents:: Contents
    :depth: 2

Quick Start
-----------
Panya provides a Paste template which you can use to create a self contained Django instance with relevant project and Panya app settings preconfigured.

In order to use the Paste template you need to install Paste and the Panya specifc templates::
    
    $ sudo easy_install paste
    $ sudo easy_install panya-paste

Once the Paste templates have been installed, create your project by running::
    
    $ paster create -t panya_project

Provide a project name and follow the prompts.

The Paste process will create a Buildout environment for you. *Buildout provides tools for assembling applications from multiple parts, Python or otherwise*. In Panya's case Buildout is used to create a self contained Django environment with all the relevant Panya apps installed and configured, as well as initialising a Django project.

To initialise the Buildout environment::
    
    $ cd <project_name>
    $ python bootstrap.py
    $ ./bin/buildout

After the Buildout process completes you can start your Django instance by running::
    
    $ ./bin/<project_name> runserver
    
The ``bin/<project_name>`` script acts as Django's normal ``manage.py`` script.

App Overview
------------
Panya is made up of a collection of standalone Django applications. The panya app(see below) provides additional CMS and view related functionality required by some apps, hence the panya-___ designations. 

django-ckeditor
~~~~~~~~~~~~~~~

Django admin CKEditor integration.

Install from PyPI::
    
    easy_install django-ckeditor

Or clone from GitHub::
    
    git clone http://github.com/shaunsephton/django-ckeditor.git


django-generate
~~~~~~~~~~~~~~~

Slightly smarter than fixtures content generator.

Install from PyPI::
    
    easy_install django-generate

Or clone from GitHub::
    
    git clone http://github.com/praekelt/django-generate.git

django-gizmo
~~~~~~~~~~~~

URL pattern like template tag configuration. Allows view or URL specific template tags to be configured from a distance.

Install from PyPI::
    
    easy_install django-gizmo

Or clone from GitHub::
    
    git clone http://github.com/praekelt/django-gizmo.git 

django-googlesearch
~~~~~~~~~~~~~~~~~~~

Django Google custom search engine integration.

Install from PyPI::
    
    easy_install django-googlesearch

Or clone from GitHub::
    
    git clone http://github.com/praekelt/django-googlesearch.git

django-likes
~~~~~~~~~~~~

Provides rich liking interaction for anonymous and authenticated users. Utilises django-secretballot. 

Install from PyPI::
    
    easy_install django-likes

Or clone from GitHub::
    
    git clone http://github.com/praekelt/django-likes.git

django-order
~~~~~~~~~~~~

Django app allowing users to manually order objects via admin.

Install from PyPI::
    
    easy_install django-order

Or clone from GitHub::
    
    git clone http://github.com/praekelt/django-order.git

django-preferences
~~~~~~~~~~~~~~~~~~

Allows users to set app specific preferences through the admin interface.

Install from PyPI::
    
    easy_install django-preferences

Or clone from GitHub::
    
    git clone http://github.com/praekelt/django-preferences.git

django-profile
~~~~~~~~~~~~~~

Includes a generic set of user profile models from which portal specific user profile views, forms and models can be easily constructed. Also provides a django-registration backend. 

Install from PyPI::
    
    easy_install django-profile

Or clone from GitHub::
    
    git clone http://github.com/praekelt/django-profile.git

django-publisher
~~~~~~~~~~~~~~~~

Publishes content to external sites, i.e. Facebook, Twitter, Digg etc.

Install from PyPI::
    
    easy_install django-publisher

Or clone from GitHub::
    
    git clone http://github.com/praekelt/django-publisher.git

django-recaptcha
~~~~~~~~~~~~~~~~

ReCaptcha form field/widget integration.

Install from PyPI::
    
    easy_install django-recaptcha

Or clone from GitHub::
    
    git clone http://github.com/praekelt/django-recaptcha.git

django-richcomments
~~~~~~~~~~~~~~~~~~~

Wraps existing Django comments framework to provide rich AJAX interactions. 

Install from PyPI::
    
    easy_install django-richcomments

Or clone from GitHub::
    
    git clone http://github.com/praekelt/django-richcomments.git

django-section
~~~~~~~~~~~~~~

Template Context Processor determining site section by request per view/URL.

Install from PyPI::
    
    easy_install django-section

Or clone from GitHub::
    
    git clone http://github.com/praekelt/django-section.git

panya
~~~~~

Panya base application providing CMS functionality. Also includes generic views, pagemenus and additional template tags.

Install from PyPI::
    
    easy_install panya

Or clone from GitHub::
    
    git clone http://github.com/praekelt/panya.git

panya-banner
~~~~~~~~~~~~

Panya dependant advertising banner content type.

Install from PyPI::
    
    easy_install panya-banner

Or clone from GitHub::
    
    git clone http://github.com/praekelt/panya-banner.git

panya-calendar
~~~~~~~~~~~~~~

Panya dependant calendar app. Allows for scheduling of content (i.e. events and shows) on specific or recurring dates.

Install from PyPI::
    
    easy_install panya-calendar

Or clone from GitHub::
    
    git clone http://github.com/praekelt/panya-calendar.git

panya-chart
~~~~~~~~~~~

Panya dependant chart content type.

Install from PyPI::
    
    easy_install panya-chart

Or clone from GitHub::
    
    git clone http://github.com/praekelt/panya-chart.git

panya-competition
~~~~~~~~~~~~~~~~~

Panya dependant competition content type.

Install from PyPI::
    
    easy_install panya-competition

Or clone from GitHub::
    
    git clone http://github.com/praekelt/panya-competition.git

panya-contact
~~~~~~~~~~~~~

Panya dependant reusable contact form.

Install from PyPI::
    
    easy_install panya-contact

Or clone from GitHub::
    
    git clone http://github.com/praekelt/panya-contact.git

panya-event
~~~~~~~~~~~

Panya dependant competition content type.

Install from PyPI::
    
    easy_install panya-event

Or clone from GitHub::
    
    git clone http://github.com/praekelt/panya-event.git

panya-gallery
~~~~~~~~~~~~~

Panya dependant gallery content type. Provides image and video(external and Flowplayer based) galleries.

Install from PyPI::
    
    easy_install panya-gallery

Or clone from GitHub::
    
    git clone http://github.com/praekelt/panya-gallery.git

panya-music
~~~~~~~~~~~

Panya dependant music content type.

Install from PyPI::
    
    easy_install panya-music

Or clone from GitHub::
    
    git clone http://github.com/praekelt/panya-music.git

panya-post
~~~~~~~~~~

Panya dependant post content type.

Install from PyPI::
    
    easy_install panya-post

Or clone from GitHub::
    
    git clone http://github.com/praekelt/panya-post.git

panya-show
~~~~~~~~~~

Panya dependant show content type.

Install from PyPI::
    
    easy_install panya-show

Or clone from GitHub::
    
    git clone http://github.com/praekelt/panya-show.git

panya-social
~~~~~~~~~~~~

Utilises and extends django-socialregistration, django-activity-stream, django-friends and django-notification to provide social functionality.

Install from PyPI::
    
    easy_install panya-social

Or clone from GitHub::
    
    git clone http://github.com/praekelt/panya-social.git

Support
-------

Ask questions on our :ref:`forum/mailing list <forum>`, or chat now with fellow Panya users in the `#panya IRC channel on irc.freenode.net <irc://irc.freenode.net/panya>`_.

Issue Tracker
-------------

If you spot any bugs or have feature suggestions, please report them to our `issue tracker <https://praekelt.lighthouseapp.com/projects/55837-panya/overview>`_. Alternatively use the GitHub issue tracker for each respective app. 

License
-------

Panya and its constituent apps are licensed under the BSD License. See the LICENSE file in the top distribution directory of each package for the full license text.
