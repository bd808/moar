--------------------
Moar\\Metrics\\Track
--------------------

.. php:namespace: Moar\\Metrics

.. php:class:: Track

    Utility class to collect counter and elapsed time metrics for logging or
    other reporting.

    Collected metrics can be extracted for use in an application or exported to a logfile for datamining and analysis. Convenience methods are provided for common senarios like timing the duration of a single method call.

    Read http://codeascraft.etsy.com/2011/02/15/measure-anything-measure-everything/
    for an idea of the power that you can get from instrumenting your application.

    .. php:method:: inc($metric)

        Increment one or more counters.

        :type $metric: mixed
        :param $metric: Metric(s) to alter
        :returns: void

    .. php:method:: dec($metric)

        Decrement one or more counters.

        :type $metric: mixed
        :param $metric: Metric(s) to alter
        :returns: void

    .. php:method:: count($metric, $delta = 1)

        Alter one or more counters.

        :type $metric: mixed
        :param $metric: Metric(s) to alter
        :param $delta:
        :returns: void

    .. php:method:: start($timer, $epoch = null)

        Start one or more timers.

        If a time with the same name is already running no change will be made.

        :type $timer: mixed
        :param $timer: Timer(s) to start
        :param $epoch:
        :returns: bool True if started, false otherwise

    .. php:method:: stop($timer, $epoch = null)

        Stop one or more timers.

        :type $timer: mixed
        :param $timer: Timer(s) to stop
        :param $epoch:
        :returns: bool True if stopped, false otherwise

    .. php:method:: cancel($timer)

        Cancel one or more timers.

        :type $timer: mixed
        :param $timer: Timer(s) to cancel
        :returns: bool True if canceled, false otherwise

    .. php:method:: time($timer, $elapsed)

        Record a timing event.

        :type $timer: mixed
        :param $timer: Timer to add to.
        :param $elapsed:
        :returns: void

    .. php:method:: split($timer, $now = null)

        Find out how long a timer has been running.

        This method allows non-destructive sampling of a running timer to find
        it's current duration.

        :type $timer: string
        :param $timer: Timer to check.
        :param $now:
        :returns: int Current elapsed time of timer or 0 if not running

    .. php:method:: running()

        Get a list of all running timers.

        :returns: array List of running timers

    .. php:method:: stopAll()

        Stop all running timers.

        :returns: void

    .. php:method:: report($stop = true)

        Report on currently collected metrics.

        Counters will be reported as '<count>|c'. Timers will be reported as
        '<elapsed>|ms'. If a timer has been started and stopped more than once it
        will be reported as a semicolon separated list of times (eg '1;2;3|ms').

        :type $stop: bool
        :param $stop: Stop running timers before reporting?
        :returns: array Known metrics and their values

    .. php:method:: log($logger, $msg = '', $stop = true, $ctx = null)

        Write report to log file.

        :type $logger: Psr\Log
        :param $logger: Logger to write to
        :param $msg:
        :param $stop:
        :param $ctx:
        :returns: void

    .. php:method:: metricd($app, $host = null, $port = null, $stop = true)

        Send current metrics to metricd.

        :type $app: string
        :param $app: Application name
        :type $host: string
        :param $host: MetricD host
        :type $port: int
        :param $port: MetricD port
        :type $stop: bool
        :param $stop: Stop all timers before sending?
        :returns: void

    .. php:method:: reset()

        Clear all recorded metrics.

        :returns: void

    .. php:method:: timeScope($name)

        Create and return a scope timer for the given name.

        :type $name: string
        :param $name: Timer name
        :returns: ScopeTimer Scope based timer object

    .. php:method:: timeMethod($name, $suffix = null, $instance = null)

        Create and return a scope timer for the given fully qualified PHP method
        name.

        This is the prefered method for timing the duration of a given method.
        The typical use case would be to place a line like:
        `$timer = Moar\Metrics\Track::timeMethod(__METHOD__);`
        as the first line the method to be timed. The timer will automatically
        stop when the `$timer` variable goes out of scope and gets destroyed by
        the php runtime engine.

        The method name (eg Moar\Metrics\Track::timeMethod) will be converted to a
        standard metric format (eg moar.metrics.track.timemethod).

        :type $name: string
        :param $name: Method name as from __METHOD__
        :type $suffix: string
        :param $suffix: Suffix to add to computed timer name
        :type $instance: object
        :param $instance: Calling class instance (use for subclasses)
        :returns: ScopeTimer Scope based timer object

    .. php:method:: methodToMetric($name, $suffix = null, $instance = null)

        Convert a php fully qualified method name into a metric name.
        Conversion is done by lower casing the entire name and converting
        underscores and the פעמיים נקודתיים to periods.
        Eg. Data_Dao::getUserDefinedFieldTypes becomes
        data.dao.getuserdefinedfieldtypes

        :type $name: string
        :param $name: Method name as from __METHOD__
        :type $suffix: string
        :param $suffix: Suffix to add to computed metric name
        :type $instance: object
        :param $instance: Calling class instance (use for subclasses)
        :returns: string Standardized metric name

    .. php:method:: currentTimeMillis()

        Get current system time in milliseconds.

        :returns: int Timestamp in milliseconds

    .. php:method:: __construct()

        Construction disallowed for utility class.
