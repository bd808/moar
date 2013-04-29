------------------------
Moar\\Selector\\Selector
------------------------

.. php:namespace: Moar\\Selector

.. php:class:: Selector

    Select a target value from an object, object graph or array.

    The selector is configured using a language that uses periods (``.``) to
    indicate member selection and brackets (``[]``) for array indexing. It
    also provides a CSS3-inspired mechanism to select array members that have
    content matching a specified value. See :php:class:`Parser` for full
    language grammar and examples.

    .. php:method:: __construct($statement)

        Constructor.

        :type $statement: string
        :param $statement: Selector statement

    .. php:method:: select($node)

        Apply selector to a node and return selected value.

        :type $node: mixed
        :param $node: Graph node
        :returns: mixed Selected value or null if not found

    .. php:method:: throwErrors($b)

        Should this instance throw traversal errors when they are encountered or
        not?

        :type $b: bool
        :param $b: Flag
        :returns: void

    .. php:method:: getError()

        Get the last error.

        :returns: Moar\Selector\TraversalException Last error

    .. php:method:: failed()

        Did the last traversal fail?

        :returns: bool True if most recient traversal failed, false otherwise
