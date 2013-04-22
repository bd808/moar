-------------------------
Moar\\Selector\\IndexRule
-------------------------

.. php:namespace: Moar\\Selector

.. php:class:: IndexRule

    Selector instruction which examines a target array and selects elements
    that satisfy the comparison operation.

    .. php:attr:: lhs

        protected array

        Left hand side of comparison.
        Used to find the value from each array member that will be compared.

    .. php:attr:: op

        protected string

        Comparison operation.

    .. php:attr:: rhs

        protected mixed

        Right hand side of comparison.

    .. php:method:: addInstruction($stmt)

        Add an instruction to the LHS selector chain.

        :type $stmt: Instruction
        :param $stmt: Selection instruction
        :returns: void

    .. php:method:: operator($op)

        Set the comparison operator.

        :type $op: string
        :param $op: Operator name
        :returns: void

    .. php:method:: value($val)

        Set the RHS of the comparison.

        :type $val: mixed
        :param $val: Comparison RHS
        :returns: void

    .. php:method:: checkMatch($node)

        Evaluate an array element against this instruction's comparison.

        :type $node: mixed
        :param $node: Array element to compare
        :returns: bool True if element matches, false otherwise

    .. php:method:: apply($node)

        Select array members matching our condition.

        :type $node: mixed
        :param $node: Current graph node
        :returns: array Matched values (possibly empty)
