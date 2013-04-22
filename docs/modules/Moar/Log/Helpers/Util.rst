------------------------
Moar\\Log\\Helpers\\Util
------------------------

.. php:namespace: Moar\\Log\\Helpers

.. php:class:: Util

    .. php:method:: normalizeName($name)

        Normalize a given logger name.

        Removes characters other than letters, digits and periods. Underscores and
        backslashes are converted to periods. This results in names which can
        easily be used for hierarical logger configurations.

        :type $name: mixed
        :param $name: Logger name or class to create name for
        :returns: string Normalized name
