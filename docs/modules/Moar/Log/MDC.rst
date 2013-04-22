--------------
Moar\\Log\\MDC
--------------

.. php:namespace: Moar\\Log

.. php:class:: MDC

    Based on the org.apache.log4j.MDC class, a MDC is a
    collection of (name, value) pairs that add useful diagnostic information to
    a log event.

    This is especially useful in a interleaved logging context as when a web server handles multiple connections near-simultaneously. The diagnostic context can be used to give a distinctive stamp to each message associated with a particular request.

    .. php:const:: KEY_SERVER_HOSTNAME

        MDC key for putServerHostname().

    .. php:const:: KEY_REMOTE_ADDR

        MDC key for putRemoteAddress().

    .. php:const:: KEY_VHOST

        MDC key for putVhost().

    .. php:attr:: singleton

        protected MDC

    .. php:attr:: map

        protected array

        Context data

    .. php:method:: __construct($data = null)

        Constructor.

        :type $data: array
        :param $data: Initial data

    .. php:method:: get($key)

        Get the context identified by the given key.

        :type $key: string
        :param $key: Key
        :returns: mixed Context

    .. php:method:: put($key, $value)

        Put a value into the current context.

        :type $key: string
        :param $key: Key
        :type $value: mixed
        :param $value: Context value
        :returns: MDC Self

    .. php:method:: remove($key)

        Remove the context identified by the given key.

        :type $key: string
        :param $key: Key
        :returns: MDC Self

    .. php:method:: clear()

        Remove all data from context.

        :returns: MDC Self

    .. php:method:: putServerHostname()

        Add server hostname minus domain (eg "example.com") into this logging
        context.

        :returns: MDC Self

    .. php:method:: putRemoteAddress()

        Add remote user's ip address to this logging context if available.

        :returns: MDC Self

    .. php:method:: putVhost()

        Add apache vhost name to this logging context if available.

        :returns: MDC Self

    .. php:method:: putCommonKeys()

        Put commonly desirable keys (ip, vhost) in this logging context.

        :returns: MDC Self

    .. php:method:: getContext()

        Get the current context as a hashtable.

        This method is intended to be used by friendly classes. Normal userspace
        code typically won't have a need for direct access to the underlying
        context.

        :returns: array context

    .. php:method:: __toString()

        Human readable string.

        :returns: string

    .. php:method:: formatMDC($ctxData)

        Format a context as a space separated key=value string.

        :type $ctxData: array
        :param $ctxData: Context data
        :returns: string Formatted data

    .. php:method:: defaultMDC()

        Get the "default" shared MDC.

        Php can typically be considered a shared-nothing, single-threaded
        container. As such you usually don't need to worry about all of the
        thread-local isolation issues that you would have in a Java Servlet
        container or another multitenant hosting container.

        :returns: MDC Shared context
