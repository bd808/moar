------------------------------------------
Moar\\Selector\\UndefinedPropertyException
------------------------------------------

.. php:namespace: Moar\\Selector

.. php:exception:: UndefinedPropertyException

    extends :php:class:`TraversalException`

    Thrown to indicate that an object did not have a particular member
    property.

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
