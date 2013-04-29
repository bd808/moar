--------------------------------
Moar\\Selector\\IndexInstruction
--------------------------------

.. php:namespace: Moar\\Selector

.. php:class:: IndexInstruction

    extends :php:class:`Instruction`

    Selector instruction which retrieves data from an array.

    .. php:method:: __construct($name)

        Constructor.

        :type $name: mixed
        :param $name: Index label

    .. php:method:: apply($node)

        Select array member by index.

        :type $node: mixed
        :param $node: Current graph node
        :returns: mixed Next traversal value or null if not present
