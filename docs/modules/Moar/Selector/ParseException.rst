------------------------------
Moar\\Selector\\ParseException
------------------------------

.. php:namespace: Moar\\Selector

.. php:class:: ParseException

    Thrown to indicate that a parsing error occurred.

    .. php:attr:: offset

        protected int

        Error offset in parse stream.

    .. php:attr:: message

        protected

    .. php:attr:: code

        protected

    .. php:attr:: file

        protected

    .. php:attr:: line

        protected

    .. php:method:: __construct($msg, $offset)

        Constructor.

        :type $msg: string
        :param $msg: Error message
        :type $offset: int
        :param $offset: Offset from start of parse stream where error was detected.

    .. php:method:: getErrorOffset()

        Returns the position where the error was found.

        :returns: int Error offset in parse stream

    .. php:method:: __clone()

    .. php:method:: getMessage()

    .. php:method:: getCode()

    .. php:method:: getFile()

    .. php:method:: getLine()

    .. php:method:: getTrace()

    .. php:method:: getPrevious()

    .. php:method:: getTraceAsString()

    .. php:method:: __toString()
