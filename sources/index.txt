Welcome to Panya's documentation!
=================================

Panya is a set of Django applications that aims to make your life even easier than it already is. It means “blink” in seSotho. Panya makes rich portal development a breeze.    

Contents
--------
.. toctree::
    :maxdepth: 1

    apps_overview.rst
    managers.rst
    models.rst
    settings.rst

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

Support
-------

Chat now with fellow Panya users in the `#panya IRC channel on irc.freenode.net <irc://irc.freenode.net/panya>`_.

Bug Tracker
-----------

If you spot any bugs or have feature suggestions, please report them to our `issue tracker <https://praekelt.lighthouseapp.com/projects/55837-panya/overview>`_. Alternatively use the GitHub issue tracker for each respective app. 

License
-------

Panya and its constituent apps are licensed under the BSD License. See the LICENSE file in the top distribution directory of each package for the full license text.
