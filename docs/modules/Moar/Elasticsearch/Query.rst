--------------------------
Moar\\Elasticsearch\\Query
--------------------------

.. php:namespace: Moar\\Elasticsearch

.. php:class:: Query

    Fluent ElasticSearch query builder.

    The json format used by Elastic Search for requests and php's default stdClass object behavior work very nicely together for creation of queries,
    but there are some boring boilerplate parts that this class can help out with.

    This class (ab)uses the `__get` and `__set` magic functions and
    \ArrayAccess::offsetSet() to provide \stdClass like automatic member creation functionality. A call to get an non-existant member will add a new Query instance in that member slot and return it via `__get`. `__set`
    detects addition of Query members and provides them with information about the parent object and member name where they have been stored.
    `offsetSet()` uses the stored parent and member name data to replace the current object with a native PHP array in the parent object. When used in concert, these methods allow chained syntax for manipulating deeply nested object structures common in ElasticSearch query language while simultaneously providing convenience functions at any depth.

    .. php:const:: SORT_ASC

        Sort order: ascending.

    .. php:const:: SORT_DESC

        Sort order: ascending.

    .. php:attr:: _parent

        protected object

        Pointer to parent object.

    .. php:attr:: _slot

        protected string

        Property name we are stored under in parent.

    .. php:attr:: _server

        protected string

        Server to contact.

    .. php:attr:: _index

        protected string

        Index to query.

    .. php:attr:: _type

        protected string

        Document type to query.

    .. php:attr:: _listNames

        protected array

        List prefixes that will trigger `__call` magic handling.

    .. php:method:: __construct($svr = null, $idx = null, $type = null, $props = array())

        Constructor.

        :type $svr: string
        :param $svr: Server URL (including scheme and port)
        :type $idx: string
        :param $idx: Index name(s)
        :type $type: string
        :param $type: Document type
        :type $props: array
        :param $props: Initial properties

    .. php:method:: server($url)

        Set server to query.

        :type $url: string
        :param $url: Server URL (including scheme and port)
        :returns: Query Self, for message chaining

    .. php:method:: index($idx)

        Set index to query.

        :type $idx: string
        :param $idx: Index name(s)
        :returns: Query Self, for message chaining

    .. php:method:: type($type)

        Set document type to query.

        :type $type: string
        :param $type: Document type
        :returns: Query Self, for message chaining

    .. php:method:: getInstance($props = array())

        Instance factory.

        :type $props: array
        :param $props: Initial properties
        :returns: Query New instance

    .. php:method:: andTerms($termMap)

        Create a node with non-empty search parameters AND'd
        together as termFilters.

        :type $termMap: array
        :param $termMap: Term keys to search value
        :returns: Query Node with ->and[] of non-empty search terms.

    .. php:method:: orTerms($termMap)

        Create a node with non-empty search parameters OR'd
        together as termFilters.

        :type $termMap: array
        :param $termMap: Term keys to search value
        :returns: Query Node with ->or[] of non-empty search terms.

    .. php:method:: hasParent()

        Does this node have a parent?

        :returns: bool True if parent is set, false otherwise

    .. php:method:: has($name)

        Do we have a property with the given name?

        :type $name: string
        :param $name: Property name
        :returns: bool True if instance has property, false otherwise

    .. php:method:: json()

        Convert graph rooted at this node to a json string.

        :returns: string Json encoding of graph

    .. php:method:: search($opts = null)

        Execute query.

        :param $opts:
        :returns: Response ElasticSearch response

    .. php:method:: scan($fetch = 50, $keepAlive = '1m', $opts = null)

        Execute scan query.

        :type $fetch: int
        :param $fetch: Number of records to fetch per request
        :type $keepAlive: string
        :param $keepAlive: Duration to keep cursor alive between requests
        :param $opts:
        :returns: Response ElasticSearch response

    .. php:method:: _buildUrl($action)

        Build the URL for a given action.

        :type $action: string
        :param $action: ElasticSearch action

    .. php:method:: sort($field, $order = self::SORT_ASC)

        Add sort criteria to this node.

        :type $field: string
        :param $field: Field to sort on
        :type $order: string
        :param $order: Sort order
        :returns: Query Self, for message chaining

    .. php:method:: scriptSort($script, $type, $params = array(), $order = self::SORT_ASC)

        Add a script sort criteria to this node.

        :type $script: string
        :param $script: Script source or stored script name
        :type $type: string
        :param $type: Data type returned by script
        :type $params: array
        :param $params: Script parameters
        :type $order: string
        :param $order: Sort order
        :returns: Query Self, for message chaining

    .. php:method:: unsorted()

        Clear any sorting that has been set on this node.

        :returns: Query Self, for message chaining

    .. php:method:: queryString($query, $field = null, $op = null)

        Add a query string to this node.
        This method supports the full query string functionality of elastic
        search:
        http://www.elasticsearch.org/guide/reference/query-dsl/query-string-query.html
        https://lucene.apache.org/core/3_6_1/queryparsersyntax.html

        :type $query: string
        :param $query: The Query String to add
        :type $field: string
        :param $field: Default field to search
        :type $op: string
        :param $op: Default operator if no explicit operator is specified
        :returns: Query Self, for message chaining

    .. php:method:: termFilter($field, $term)

        Add a term filter to this node.

        A term filter matches documents having an exact match in the given field.

        :type $field: string
        :param $field: Field to check for term
        :type $term: mixed
        :param $term: Term to require
        :returns: Query Self, for message chaining

    .. php:method:: missingFilter($field)

        Add a missing filter to this node.

        A missing filter matches documents that do not contain the given field.

        :type $field: string
        :param $field: Field to check
        :returns: Query Self, for message chaining

    .. php:method:: rangeFilter($field, $from, $to, $includeLower = true, $includeUpper = true)

        Add a range filter to this node.

        :type $field: string
        :param $field: Field to check for range
        :type $from: mixed
        :param $from: Range start
        :type $to: mixed
        :param $to: Range end
        :type $includeLower: bool
        :param $includeLower: Should lower bound be inclusive? (>=)
        :type $includeUpper: bool
        :param $includeUpper: Should upper bound be inclusive? (<=)
        :returns: Query Self, for message chaining

    .. php:method:: rangeFacet($name, $field, $ranges)

        Add a range facet to this node.

        :type $name: string
        :param $name: Facet name
        :type $field: string
        :param $field: Field to compute facet on
        :type $ranges: array
        :param $ranges: Range limits as (low, high) pairs
        :returns: Query Self, for message chaining

    .. php:method:: termsFacet($name, $field, $size = null, $parms = array())

        Add a terms facet to this node.

        :type $name: string
        :param $name: Facet name
        :type $field: string
        :param $field: Field to compute facet on
        :type $size: int
        :param $size: Return top N terms (null for all)
        :type $parms: array
        :param $parms: Additional parameters to add to facet
        :returns: Query Self, for message chaining

    .. php:method:: dateHistogramFacet($name, $field, $interval = 'hour', $parms = array())

        Add a date histogram facet to this node.

        :type $name: string
        :param $name: Facet name
        :type $field: string
        :param $field: Field to compute facet on
        :type $interval: string
        :param $interval: Histogram bucket width
        :type $parms: array
        :param $parms: Additional parameters to add to facet
        :returns: Query Self, for message chaining

    .. php:method:: statsFacet($name, $field)

        Add a statistical facet to this node.

        :type $name: string
        :param $name: Facet name
        :type $field: string
        :param $field: Field to compute facet on
        :returns: Query Self, for message chaining

    .. php:method:: _range($from, $to, $includeLower = true, $includeUpper = true)

        Add a range clause to this node.

        :type $from: mixed
        :param $from: Range start
        :type $to: mixed
        :param $to: Range end
        :type $includeLower: bool
        :param $includeLower: Should lower bound be inclusive? (>=)
        :type $includeUpper: bool
        :param $includeUpper: Should upper bound be inclusive? (<=)
        :returns: Query Self, for message chaining

    .. php:method:: _cast($val)

        Cast a value for inclusion in a query.

        :type $val: mixed
        :param $val: Value to cast
        :returns: mixed Cast value

    .. php:method:: _listAppend($list, $method, $args)

        Append the result of a dynamic method call to an array property of this
        instance.

        :type $list: string
        :param $list: List to append to
        :type $method: string
        :param $method: Method to call for value
        :type $args: array
        :param $args: Call arguments
        :returns: Query Self, for message chaining

    .. php:method:: __get($name)

        Abuse the magic helper for reading inaccessible properties.

        Default php behavior is to prentend as though a stdClass instance exists
        when an assignment call includes one or more undefined properties in it's
        variable name. By overloading this method we can tweak this behavior to
        return another Query object instead which will keep our helper methods
        available as we build the object graph.

        :type $name: string
        :param $name: Property name
        :returns: Query Newly allocated Query instance

    .. php:method:: __set($name, $value)

        Abuse the magic helper for writing inaccessible properties.

        If value being set is an Query instance, decorate it with a pointer to the
        parent object it is being added to and the name of the property slot it is
        being stored in.

        :type $name: string
        :param $name: Property name
        :type $value: mixed
        :param $value: Value to store
        :returns: void

    .. php:method:: __call($name, $args)

        Attempt to resolve undefined method calls as list creation helper
        methods.

        :type $name: string
        :param $name: Method name
        :type $args: array
        :param $args: Call arguments
        :returns: mixed Call result

    .. php:method:: offsetSet($offset, $value)

        Abuse the ArrayAccess::offsetSet method to replace ourself in our parent
        object with a native php array.

        Why would we want to do this? Well because we are trying to keep some
        seriously sneaky magic that php does for stdClass type objects working
        while implementing a custom type that can do some other good things.
        Assigning to an unset variable as though it is an array is perfectly legal
        php syntax, but our `__get` magic trips it up. This hack puts that
        behavior back in place via some slightly sneaky slight of hand.

        :type $offset: mixed
        :param $offset: Array index to populate
        :type $value: mixed
        :param $value: Value to assign to array slot
        :returns: void

    .. php:method:: offsetExists($offset)

        Stub to complete ArrayAccess interface.

        :type $offset: mixed
        :param $offset: Ignored
        :returns: bool Always returns false.

    .. php:method:: offsetGet($offset)

        Stub to complete ArrayAccess interface.

        :type $offset: mixed
        :param $offset: Ignored
        :returns: mixed Always returns null.

    .. php:method:: offsetUnset($offset)

        Stub to complete ArrayAccess interface.

        :type $offset: mixed
        :param $offset: Ignored
        :returns: void
