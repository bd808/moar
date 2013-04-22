.. _Moar-Template-Block:
---------------------
Moar\\Template\\Block
---------------------

.. php:namespace: Moar\\Template

.. php:class:: Block

    Block based, inheritance driven template engine.

    Based on Adam Shaw's phpti template engine (http://phpti.com/).

    .. php:attr:: root

        protected array

        Base template information.

    .. php:attr:: partials

        protected array

        Blocks that have been started but not yet closed.

    .. php:attr:: blocks

        protected array

        List of named blocks.

    .. php:attr:: end

        protected int

        Position of last block end in buffered output.

    .. php:method:: block($name, $filters = null)

        Start a block.

        A block defines a section of replacable content. The last definition of a
        named block will be output by the script. All prior instances of the same
        block (and any sub blocks) will be discarded.

        :type $name: string
        :param $name: Block name
        :type $filters: array|string
        :param $filters: Filters to apply to block output
        :returns: void

    .. php:method:: endblock($name = null)

        End a block.

        :type $name: string
        :param $name: Block name
        :returns: void

    .. php:method:: emptyblock($name)

        Define an empty block.

        An empty block has no contents in the template in which it is defined but
        can be overloaded in a descendant template to output content.

        :type $name: string
        :param $name: Block name
        :returns: void

    .. php:method:: super()

        Output the content of the parent block.

        Used within a block to include the complete content of the parent block.

        :returns: void

    .. php:method:: superAsString()

        Get the content of the parent block as a string.

        :returns: string Block content

    .. php:method:: flush()

        Flush all output buffers.

        :returns: void

    .. php:method:: init($trace = null)

        Initialize template engine.

        :type $trace: array
        :param $trace: Backtrace
        :returns: array Backtrace

    .. php:method:: create($name, $filters, $trace)

        Create a block.

        :type $name: string
        :param $name: Block name
        :type $filters: mixed
        :param $filters: Filters to apply to block output
        :type $trace: array
        :param $trace: Backtrace of block declaration
        :returns: object Block header

    .. php:method:: insertBlock($block)

        Insert a block into the template stack.

        :type $block: object
        :param $block: Block header
        :returns: void

    .. php:method:: bufferCallback($buffer)

        Output buffering callback.

        Triggered when the template's master buffer is flushed.

        :type $buffer: string
        :param $buffer: Buffered content
        :returns: string Buffer content

    .. php:method:: compile($block, $buffer)

        Compile a block.

        :type $block: object
        :param $block: Block header
        :type $buffer: string
        :param $buffer: Output buffer contents
        :returns: array Block contents

    .. php:method:: warning($message, $trace, $loc = null)

        Log a compilation warning.

        :type $message: string
        :param $message: Warning message
        :type $trace: array
        :param $trace: Backtrace of interpreter
        :type $loc: array
        :param $loc: Backtrace of error
        :returns: void

    .. php:method:: bt()

        Get the backtrace minus calls local to this class.

        :returns: array Backtrace

    .. php:method:: inRoot($trace)

        Is the trace from the same file as the root template?

        :type $trace: array
        :param $trace: Backtrace
        :returns: bool True if trace is from same file as root template.

    .. php:method:: inRootOrChild($trace)

        :param $trace:

    .. php:method:: sameFile($trace1, $trace2)

        Are the two traces from the same file?

        :type $trace1: array
        :param $trace1: Backtrace
        :type $trace2: array
        :param $trace2: Backtrace
        :returns: bool True if both traces are from the same php file.

    .. php:method:: isSubtrace($trace1, $trace2)

        Is one trace a subset of another?

        :param $trace1:
        :param $trace2:
