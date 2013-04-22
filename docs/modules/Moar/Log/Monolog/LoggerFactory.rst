---------------------------------
Moar\\Log\\Monolog\\LoggerFactory
---------------------------------

.. php:namespace: Moar\\Log\\Monolog

.. php:class:: LoggerFactory

    Logger factory for Monolog instances.

    .. php:attr:: root

        protected Logger

    .. php:attr:: logs

        protected array

        Logger instance cache.

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

    .. php:method:: register($name, LoggerInterface $logger)

        Register a LoggerInterface instance.

        :type $name: string
        :param $name: Logger name
        :type $logger: LoggerInterface
        :param $logger: Logger
        :returns: void

    .. php:method:: findParent($name)

        :type $name: string
        :param $name: Name of new logger
        :returns: LoggerInterface Parent logger

    .. php:method:: getLogger($name)

        Get a logger instance with the given name.

        :type $name: string
        :param $name: Name of the logger
        :returns: LoggerInterface
