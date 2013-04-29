----------------------------------
Moar\\Selector\\TraversalException
----------------------------------

.. php:namespace: Moar\\Selector

.. php:exception:: TraversalException

    extends :php:class:`\Exception`

    Thrown to indicate that a traversal error occured.

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
