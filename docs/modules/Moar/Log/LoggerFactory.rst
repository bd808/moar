------------------------
Moar\\Log\\LoggerFactory
------------------------

.. php:namespace: Moar\\Log

.. php:class:: LoggerFactory

    Logger instance factory.

    The pattern suggested by PSR-3 is for all objects desiring to log messages to implement the Psr\Log\LoggerAwareInterface interface so that a Logger instance can be provided via dependency injection or other object wiring means. Moar finds this pattern to be less than desirable since we prefer explicit over implicit DI wiring and also believe that any and all objects should use logging.

    Moar prefers to use a factory pattern for creating Logger instances, but we don't want to couple our code to any particular PSR-3 implementation at the factory level. This class and it's associated interfaces provide a SPI that can be used to bind any PSR-3 compliant logging system to a Moar application. The API for this is taken from the SLF4J project.

    .. php:method:: getLogger($name)

        Get a logger instance with the given name.

        :type $name: string
        :param $name: Name of the logger
        :returns: LoggerInterface

    .. php:method:: getILoggerFactory()

        Get the currently configured ILoggerFactory.

        :returns: ILoggerFactory Logger factory

    .. php:method:: setILoggerFactory($factory)

        Set the IloggerFactory to use for crating logger instances.

        :type $factory: ILoggerFactory
        :param $factory: Factory instance
        :returns: void

    .. php:method:: __construct()

        Construction of utility class is not allowed.
