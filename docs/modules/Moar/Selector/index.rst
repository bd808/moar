.. _module-moar-selector:
.. namespace:: Moar\Selector

=============
Moar-Selector
=============

Select a target value from an object, object graph or array.

Installation
------------

Usage
-----

.. code-block:: php

    use Moar\Selector\Selector;

    $something = new Selector('...');
    $foo = $something->select($o);

Classes
-------

.. class:: Selector

  Select a target value from an object, object graph or array.

  The selector is configured using a language that uses periods (``.``) to
  indicate member selection and brackets (``[]``) for array indexing. It also
  provides a CSS3-inspired mechanism to select array members that have content
  matching a specified value. See :class:`Parser` for full
  language grammar and examples.

  .. method:: __construct($statement)

    :param string $statement: Selector statement

.. class:: Parser

  Parser for selector statements.
