-----------------------------
Moar\\Elasticsearch\\Response
-----------------------------

.. php:namespace: Moar\\Elasticsearch

.. php:class:: Response

    Elastic Search response wrapper.

    .. php:attr:: isError

        protected bool

        Was this an error response?

    .. php:attr:: results

        protected array

        Convenience pointer to returned documents.

    .. php:attr:: ptr

        protected int

        Iteration pointer.

    .. php:attr:: offset

        protected int

        Offset in scrolling result set.

    .. php:attr:: scrollUrl

        protected string

        Url for scroll requests.

    .. php:attr:: keepAlive

        protected string

        Keep alive time for scroll requests.

    .. php:method:: __construct($body, $status = 200, $url = null, $keepAlive = null)

        Constructor.

        :type $body: string|object
        :param $body: ES response body
        :type $status: int
        :param $status: HTTP response status code
        :type $url: string
        :param $url: ElasticSearch server URL for scroll requests
        :type $keepAlive: string
        :param $keepAlive: Duration to keep cursor alive between requests

    .. php:method:: processResponse($body, $status)

        Process an HTTP response.

        :type $body: string|object
        :param $body: ES response body
        :type $status: int
        :param $status: HTTP response status code

    .. php:method:: isError()

        Is this an error response?

        :returns: bool True if response encodes an error, false otherwise

    .. php:method:: getResults()

        Get the collection of results from the request.

        :returns: array Results

    .. php:method:: hasFacets()

        Does this response have facet information?

        :returns: bool True if facets are present, false otehrwise

    .. php:method:: getFacets()

        Get facets.

        :returns: array Facets

    .. php:method:: getTotalHits()

        Get the total number of matches for the request.

        :returns: int Total number of documents matched by request

    .. php:method:: getElapsed()

        Get the amount of time that elapsed to perform request according to
        Elastic Search cluster.

        :returns: int Elapsed time in milliseconds

    .. php:method:: count()

        Get count of results.

        :returns: int Count of results in this response

    .. php:method:: current()

        Return the current iterator object.

        :returns: object Result

    .. php:method:: key()

        Return the current iterator slot key.

        :returns: int Key

    .. php:method:: next()

        Advance the iterator to the next slot.

        :returns: void

    .. php:method:: rewind()

        Reset iterator to begenning of collection.

        :returns: void

    .. php:method:: valid()

        Check to see if current iterator position is valid.

        :returns: bool True if pointing to valid member, false otherwise

    .. php:method:: scroll()

        Scroll to the next chunk of response data.

        This will be called automatically under iteration (eg foreach) when the
        current results are exhausted if _scroll_id is present.

        :returns: void
