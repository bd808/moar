---------------------------
Moar\\Selector\\Instruction
---------------------------

.. php:namespace: Moar\\Selector

.. php:class:: Instruction

    Selector instructions are used to traverse an object graph.

    .. php:method:: apply($node)

        Apply instruction to graph.

        :type $node: mixed
        :param $node: Current graph node
        :returns: mixed Next traversal value
