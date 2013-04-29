.. _Moar-Selector:
.. php:namespace: Moar\\Selector

::::::::::::::
Moar\\Selector
::::::::::::::

Select a target value from an object, object graph or array.

A :php:class:`Selector` is configured using a graph traversal language that
uses periods (``.``) to indicate member selection and brackets (``[]``) for
array indexing. It also provides a CSS3-inspired mechanism to select array
members that have content matching a specified value. The language allows:

- selecting a member of an object
- selecting an array element by index
- selecting an array element by key
- selecting array elements by content
- any combination of the above actions

Selector Grammar (in EBNF_ notation)::

    statement        = selector
                     | index , [ "." , selector ] ;
    selector         = member , { ( "." , member ) | index } ;
    member           = identifier
                     | variable-member ;
    identifier       = start-char , { ident-char } ;
    variable-member  = "{" , ws , literal , ws , "}" ;
    index            = "[" , ws , expression , ws , "]" ;
    expression       = value
                     | rule ;
    value            = number
                     | literal ;
    rule             = selector , ws , op , ws , value ;
    literal          = '"' , { all - '"' } , '"'
                     | "'" , { all - "'" } , "'" ;
    number           = [ "-" ] , { digit } , [ "." , { digit } ] ;
    ws               = ? /\s*/ ? ;
    op               = "=" ;
    start-char       = ? /[a-zA-Z_\x7f-\xff]/ ? ;
    ident-char       = ? /[a-zA-Z0-9_\x7f-\xff]/ ? ;
    digit            = ? /[0-9]/ ? ;
    all              = ? all visible characters ?

Example selectors:
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

.. _EBNF: https://en.wikipedia.org/wiki/Extended_Backus%E2%80%93Naur_Form

Classes
-------
.. toctree::

  Selector
  ParseException
  TraversalException
  TypeException
  UndefinedIndexException
  UndefinedPropertyException
  IndexRule
  Parser
  Instruction
  IndexInstruction
  MemberInstruction
