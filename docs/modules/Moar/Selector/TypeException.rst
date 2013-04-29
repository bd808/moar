-----------------------------
Moar\\Selector\\TypeException
-----------------------------

.. php:namespace: Moar\\Selector

.. php:exception:: TypeException

    extends :php:class:`TraversalException`

    Thrown to indicate that a variable of an unexpected type was found.

    .. php:method:: __construct($message = "", $code = 0, $previous = null)

        :type $message: string
        :param $message: the message to throw
        :type $code: int
        :param $code: Exception code
        :type $previous: \\Exception
        :param $previous: Previous exception

    .. php:method:: getMessage()

    .. php:method:: getCode()

    .. php:method:: getFile()

    .. php:method:: getLine()

    .. php:method:: getTrace()

    .. php:method:: getPrevious()

    .. php:method:: getTraceAsString()

    .. php:method:: __toString()

    .. php:method:: __clone()

