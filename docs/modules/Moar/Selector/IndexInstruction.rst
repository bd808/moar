--------------------------------
Moar\\Selector\\IndexInstruction
--------------------------------

.. php:namespace: Moar\\Selector

.. php:class:: IndexInstruction

    Selector instruction which retrieves data from an array.

    .. php:attr:: idx

        protected mixed

        Array index.

    .. php:method:: __construct($name)

        Constructor.

        :type $name: mixed
        :param $name: Index label

    .. php:method:: apply($node)

        Select array member by index.

        :type $node: mixed
        :param $node: Current graph node
        :returns: mixed Next traversal value or null if not present
