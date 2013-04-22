----------------------
Moar\\Selector\\Parser
----------------------

.. php:namespace: Moar\\Selector

.. php:class:: Parser

    Parse a graph traversal statement into a list of executable instructions.

    The graph traversal language described here allows:
    - selecting a member of an object
    - selecting an array element by index
    - selecting an array element by key
    - selecting array elements by content
    - any combination of the above actions

    Grammar (in psudo-EBNF notation):
    <pre><code>
      statement        = selector | index, [ '.', selector ] ;
      selector         = member, { ( '.', member ) | index } ;
      member           = identifier | complex ;
      complex          = '{', ws, literal, ws, '}' ;
      identifier       = start_char, { ident_char } ;
      literal          = '"', { not_quote }, '"' |
                         '\'', { not_single_quote }, '\'' ;
      index            = '[', ws, expression, ws, ']' ;
      expression       = value | rule ;
      value            = number | literal ;
      number           = [ '-' ], { digit }, [ '.', { digit } ] ;
      rule             = selector, ws, op, ws, value ;
      ws               =  /\s*?/
      op               = '=' ;
      start_char       = /[a-zA-Z_\x7f-\xff]/ ;
      ident_char       = /[a-zA-Z0-9_\x7f-\xff]/ ;
      not_quote        = /[^"]/
      not_single_quote = /[^']/
      digit            = /[0-9]/ ;
    </code></pre>

    Example paths:
     - foo
     - {"something"}
     - [1]
     - foo.bar
     - foo.bar[child="val"].baz
     - foo.bar[0]
     - foo.bar[0].baz
     - foo.bar["blah"]
     - foo.bar["blah"].baz
     - foo.bar["blah"][0]
     - foo.{"any random string"}
     - foo.{"any random string"}.bar
     - foo.{"any random string"}[sel="val"].bar
     - foo.{"any random string"}[{"blah"}.xyzzy="val"].bar

    .. php:const:: START_CHAR

        Regex for identifier start character.

    .. php:const:: IDENT_CHAR

        Regex for identifier body character.

    .. php:const:: ANY_CHAR

        Regex for any character.

    .. php:const:: START_NUMBER

        Regex for a character that can start a number.

    .. php:const:: DIGIT

        Regex for a digit.

    .. php:const:: ANY_QUOTE

        Regex for any quote.

    .. php:const:: WHITESPACE

        Regex for whitespace.

    .. php:const:: START_OPERATOR

        Regex for rule operators.

    .. php:attr:: src

        protected string

        Statement to parse.

    .. php:attr:: ptr

        protected int

        Current parser position.

    .. php:attr:: maxPtr

        protected int

        Maximum parser position.

    .. php:method:: __construct($statement)

        Constructor.

        :type $statement: string
        :param $statement: Statement to parse

    .. php:method:: reset()

        Reset the parser.

        :returns: void

    .. php:method:: parse()

        Parse the statement.

        :returns: array Collection of path traversal instructions

    .. php:method:: nextInstruction()

        Get the next traversal instruction.

        :returns: Moar\Selector\Instruction Traversal instruction

    .. php:method:: parseMember()

        Parse a member identifier.

        :returns: Moar\Selector\Instruction Traversal instruction

    .. php:method:: parseIndex()

        Parse an array index instruction.

        :returns: Moar\Selector\Instruction Traversal instruction

    .. php:method:: parseIndexRule()

        Parse an index selector rule.

        :returns: Moar\Selector\Instruction Traversal instruction

    .. php:method:: parseLiteral()

        Parse a literal (quoted) string.

        :returns: string Literal string

    .. php:method:: parseNumber()

        Parse a numeric value.

        :returns: number Number

    .. php:method:: parseChar($onlyMatch = self::ANY_CHAR)

        Parse the next character in the stream.

        :type $onlyMatch: string
        :param $onlyMatch: Regex that character must match
        :returns: string Next character or null if regex fails

    .. php:method:: atEnd()

        Are we at the end of the input?

        :returns: bool True if at end, false otherwise

    .. php:method:: peek($len = 1, $offset = 0)

        Peek at the input stream.

        :type $len: int|string
        :param $len: How far to look ahead
        :type $offset: int|string
        :param $offset: How far to skip before looking
        :returns: string Input chunk

    .. php:method:: expect($str, $offset = 0)

        Does the given string come next in the input stream?

        :type $str: string
        :param $str: String to expect
        :type $offset: int|string
        :param $offset: How far to skip before looking
        :returns: bool True if expected string is in input, false otherwise

    .. php:method:: expectMatch($pattern, $len = 1, $offset = 0)

        Does the given pattern come next in the input stream?

        :type $pattern: string
        :param $pattern: Regex or single char to match
        :type $len: int
        :param $len: How far to look ahead
        :type $offset: int
        :param $offset: How far to skip before looking
        :returns: bool True if expected pattern matches input, false otherwise

    .. php:method:: consume($what = 1)

        Consume and return the next N chars or expected string.

        :type $what: int|string
        :param $what: Number of chars to consume or string to expect
        :returns: string Consumed chars

    .. php:method:: consumeWhitespace()

        Consume any number of whitespace characters from the input stream.

        :returns: void

    .. php:method:: makeException($msg)

        Build and return a Moar\Selector\ParseException with the current parser
        position.

        :type $msg: string
        :param $msg: Error message
        :returns: Moar\Selector\ParseException Exception
