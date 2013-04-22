-------------------------
Moar\\Log\\ILoggerFactory
-------------------------

.. php:namespace: Moar\\Log

.. php:class:: ILoggerFactory

    ILoggerFactory instances manufacture LoggerInterface instances by name.

    .. php:method:: getLogger($name)

        Get a logger instance with the given name.

        :type $name: string
        :param $name: Name of the logger
        :returns: LoggerInterface
