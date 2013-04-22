---------------------------------
Moar\\Selector\\MemberInstruction
---------------------------------

.. php:namespace: Moar\\Selector

.. php:class:: MemberInstruction

    Selector instruction which selects a member from an object.

    .. php:attr:: member

        protected string

        Member to select.

    .. php:method:: __construct($name)

        Constructor.

        :type $name: string
        :param $name: Member name

    .. php:method:: apply($node)

        Select member property value from an object.

        :type $node: mixed
        :param $node: Current graph node
        :returns: mixed Next traversal value
