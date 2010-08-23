.. _settings:
Settings
========
Here’s a full list of all available settings as required by the standard set of Panya apps, in alphabetical order, and their default values.

.. _settings-staging:
STAGING
-------
Default: ``False``

A boolean that turns on/off staging mode.

If this setting is set to ``True`` the :ref:`permitted manager's <managers-panya-permitted>` resulting queryset will additionaly include objects which have a :ref:`state <models-modelbase-fields-state>` set to ``staging``. Use this setting to create staging instances with which you can preview content without the content being available to the general public.
