---------------------------------------------
Moar\\Log\\Helpers\\HierarchicalLoggerFactory
---------------------------------------------

.. php:namespace: Moar\\Log\\Helpers

.. php:class:: HierarchicalLoggerFactory

    Helper for creating hierarchically organized logger instances.

    .. php:attr:: logs

        protected array

        Logger instance cache.

    .. php:method:: register($name, LoggerInterface $logger)

        Register a LoggerInterface instance.

        :type $name: string
        :param $name: Logger name
        :type $logger: LoggerInterface
        :param $logger: Logger
        :returns: void

    .. php:method:: getDafaultLogger()

        Get the default logger.

        Must return the same logger instance on each call.

        :returns: LoggerInterface

    .. php:method:: newLogger($name, LoggerInterface $parent)

        Create a new LoggerInterface instance.

        :type $name: string
        :param $name: Name of new logger
        :type $parent: LoggerInterface
        :param $parent: Closest known ancestor logger
        :returns: LoggerInterface Logger

    .. php:method:: findParent($name)

        :type $name: string
        :param $name: Name of new logger
        :returns: LoggerInterface Parent logger

    .. php:method:: getLogger($name)

        Get a logger instance with the given name.

        :type $name: string
        :param $name: Name of the logger
        :returns: LoggerInterface
