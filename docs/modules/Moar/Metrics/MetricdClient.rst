----------------------------
Moar\\Metrics\\MetricdClient
----------------------------

.. php:namespace: Moar\\Metrics

.. php:class:: MetricdClient

    Client for sending data collected by Moar\Metrics\Track to a Kount MetricD
    aggregation server.

    MetricD accepts UDP datagrams with a json payload. This payload includes some metadata about the client that is sending the information and collections of counter and timer metrics.

    Example Payload:
    <pre>
     {
       "meta": {
         "host": "dev31.boi.keynetics.com",
         "app": "kaptcha",
         "merc": 999999
       },
       "metrics": {
         "fizz": "3|c",
         "buzz": "5|c",
         "foo": "9|ms",
         "bar": "1;2;3|ms"
       }
     }
    </pre>

    .. php:attr:: logger

        protected LoggerInterface

        Logger.

    .. php:attr:: host

        protected string

        Metricd host to send data to.

    .. php:attr:: port

        protected int

        Metricd port to send data to.

    .. php:attr:: hostname

        protected string

        Client hostname.

    .. php:attr:: app

        protected string

        Client application name.

    .. php:method:: __construct($host = null, $port = null, $logger = null)

        Constructor.

        :type $host: string
        :param $host: MetricD hostname/ip address. Null for default `127.0.0.1`.
        :type $port: int
        :param $port: MetricD port number. Null for default `8125`.
        :type $logger: LoggerInterface
        :param $logger: Logger instance.

    .. php:method:: setLogger(LoggerInterface $logger)

        Sets a logger instance on the object

        :type $logger: LoggerInterface
        :param $logger:
        :returns: void

    .. php:method:: setHost($host)

        Set the MetricD host.

        :type $host: string
        :param $host: Hostname or ip address
        :returns: MetricdClient Self, for message chaining.

    .. php:method:: setPort($port)

        Set the MetricD port.

        :type $port: int
        :param $port: Port number
        :returns: MetricdClient Self, for message chaining.

    .. php:method:: setHostname($hostname)

        Host on who's behalf metrics are being submitted.

        :type $hostname: string
        :param $hostname: Fully qualified domain name of host
        :returns: MetricdClient Self, for message chaining.

    .. php:method:: setApp($app)

        Application that is submitting metrics.

        :type $app: string
        :param $app: Application name
        :returns: MetricdClient Self, for message chaining.

    .. php:method:: send($metrics, $extraMeta = null)

        Send metrics to metricd host.

        :type $metrics: array
        :param $metrics: Metrics to send.
        :type $extraMeta: array
        :param $extraMeta: Additional meta information to send along with metrics.
        :returns: MetricdClient Self, for method chaining.
