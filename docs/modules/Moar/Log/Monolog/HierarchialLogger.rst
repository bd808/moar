-------------------------------------
Moar\\Log\\Monolog\\HierarchialLogger
-------------------------------------

.. php:namespace: Moar\\Log\\Monolog

.. php:class:: HierarchialLogger

    Subclass of Monolog log channel designed for hierarchical logging.

    Monolog keeps it's handler and processor chains in protected members. We extend the Logger class so that we can get access to another Loggers chains. This allows us to copy the chains of a parent handler.

    .. php:attr:: level

        protected int

    .. php:method:: setParent(Logger $parent)

        Set this logger's parent logger.

        :type $parent: Logger
        :param $parent: Parent logger
        :returns: void

    .. php:method:: setLevel($level)

        Sets minimum logging level at which this channel will emit.

        :type $level: int
        :param $level: Level
        :returns: void

    .. php:method:: isHandling($level)

        :param $level:

    .. php:method:: addRecord($level, $message, $context = array())

        :param $level:
        :param $message:
        :param $context:
