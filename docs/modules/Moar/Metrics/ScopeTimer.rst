-------------------------
Moar\\Metrics\\ScopeTimer
-------------------------

.. php:namespace: Moar\\Metrics

.. php:class:: ScopeTimer

    Lightweight class for a scope based timer.

    Starts Moar\Metrics\Track on construction and stops timer on destruction.
    Useful when tracking method execution duration where the method has multiple exit points or does significant processing in the return statement.

    .. php:method:: __construct($name)

        Constructor.

        :type $name: string
        :param $name: Timer name

    .. php:method:: stop()

        Stop the timer.

        :returns: void

    .. php:method:: __destruct()

        Destructor.
        Stops timer on destruct.
