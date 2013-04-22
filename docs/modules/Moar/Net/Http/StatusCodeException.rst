------------------------------------
Moar\\Net\\Http\\StatusCodeException
------------------------------------

.. php:namespace: Moar\\Net\\Http

.. php:class:: StatusCodeException

    Signals that the response status code was not as expected.

    .. php:attr:: request

        protected Request

        Request that triggered this exception.

    .. php:attr:: message

        protected

    .. php:attr:: code

        protected

    .. php:attr:: file

        protected

    .. php:attr:: line

        protected

    .. php:method:: __construct($msg, $code, $req = null)

        Constructor.

        :type $msg: string
        :param $msg: Error message
        :type $code: int
        :param $code: Error code
        :type $req: Request
        :param $req: Request that triggered this exception

    .. php:method:: getRequest()

        Get the request that triggered this exception.

        :returns: Request Request

    .. php:method:: setRequest($req)

        Set the request that triggered this exception.

        :type $req: Request
        :param $req: Request
        :returns: Exception Self, for message chaining

    .. php:method:: __clone()

    .. php:method:: getMessage()

    .. php:method:: getCode()

    .. php:method:: getFile()

    .. php:method:: getLine()

    .. php:method:: getTrace()

    .. php:method:: getPrevious()

    .. php:method:: getTraceAsString()

    .. php:method:: __toString()
