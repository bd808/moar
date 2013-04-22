---------------------------------
Moar\\Net\\Http\\TimeoutException
---------------------------------

.. php:namespace: Moar\\Net\\Http

.. php:class:: TimeoutException

    Signals that a timeout event halted the request.

    This could be a timeout of the DNS lookup, the initial socket connect, the SSL handshake or the total runtime of the request. Check the exception message for more details on the origin of the failure.

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
