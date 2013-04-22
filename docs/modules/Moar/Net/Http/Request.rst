------------------------
Moar\\Net\\Http\\Request
------------------------

.. php:namespace: Moar\\Net\\Http

.. php:class:: Request

    HTTP request handler that attempts to make using cURL easy.

    Static convenience methods are provided to performing typical requests such as GET and POST. Several variations of POST are available for
    "application/x-www-form-urlencoded", "multipart/form-data" and raw body encodings.

    More complicated requests can be configured via direct use of the class.
    Helper methods are provided for common operations such as authenticating with a a username/password pair or an x509 certificate.

    Requests are sent by calling the submit() method directly or by passing an array of prepared requests to the static parallelSubmit() method.
    Either method of executing a request will result in the provided Request being updated to contain response codes, headers and body data returned by the server processing the URL.

    .. php:const:: DEFAULT_USERAGENT

        Default user-agent string.

    .. php:const:: DEFAULT_MAXREDIRS

        Default maximum redirects.

    .. php:const:: METHOD_GET

        HTTP GET.

    .. php:const:: METHOD_POST

        HTTP POST.

    .. php:attr:: defaultCurlOpts

        protected array

        Default curlopts.

    .. php:attr:: url

        protected string

        URL to request.

    .. php:attr:: method

        protected string

        HTTP request method.

    .. php:attr:: headers

        protected array

        HTTP request headers.

    .. php:attr:: postBody

        protected string

        POST body.

    .. php:attr:: userAgent

        protected string

        User-Agent header value.

    .. php:attr:: curlOptions

        protected array

        Curl options.

    .. php:attr:: defaultFailIfNot200

        protected bool

        Default behavior for non-200 status responses.

    .. php:attr:: responseHttpCode

        protected int

        Response code.

    .. php:attr:: responseHeaders

        protected array

        Response headers.

    .. php:attr:: responseBody

        protected string

        Response body.

    .. php:attr:: responseCurlInfo

        protected array

        Curl response information.

    .. php:attr:: responseCurlErr

        protected int

        Curl error status.

    .. php:attr:: responseCurlErrMessage

        protected string

        Curl error message.

    .. php:method:: __construct($url = null, $method = self::METHOD_GET, $data = null, $headers = null, $opts = null)

        Constructor.

        :type $url: string
        :param $url: URL to request
        :type $method: string
        :param $method: HTTP request verb
        :param $data:
        :param $headers:
        :param $opts:

    .. php:method:: setUrl($url)

        Set the url for this request.

        :type $url: string
        :param $url: URL to request
        :returns: Request Self, for message chaining

    .. php:method:: getUrl()

        Get the url for this request.

        :returns: string URL of request

    .. php:method:: setMethod($method)

        Set the method for this request.

        :type $method: string
        :param $method: HTTP request verb
        :returns: Request Self, for message chaining

    .. php:method:: getMethod()

        Get the method for this request.

        :returns: string HTTP request verb

    .. php:method:: setHeaders($headers)

        Set the headers for this request.

        :type $headers: array
        :param $headers: Custom headers to set on request
        :returns: Request Self, for message chaining

    .. php:method:: addHeader($header)

        Add a header for this request.

        :type $header: string
        :param $header: Header to send with request
        :returns: Request Self, for message chaining

    .. php:method:: getHeaders()

        Get the custom headers for this request.

        :returns: array Collection of custom headers

    .. php:method:: setPostBody($postBody)

        Set the postBody for this request.

        :type $postBody: mixed
        :param $postBody: Either literal payload for request or array of key=>value pairs to encode as "multipart/form-data" on submission.
        :returns: Request Self, for message chaining

    .. php:method:: getPostBody()

        Get the postBody for this request.

        :returns: string HTTP request verb

    .. php:method:: addQueryData($parms)

        Append a query string to the current URL.

        :type $parms: string|array
        :param $parms: Parameters to add as query string to url
        :returns: Request Self, for message chaining

    .. php:method:: setCurlOptions($opts)

        Set cURL options for this request.

        :type $opts: array
        :param $opts: Curl options
        :returns: Request Self, for message chaining

    .. php:method:: addCurlOption($key, $value)

        Add a cURL option for this request.

        :type $key: mixed
        :param $key: Curl option identifier
        :type $value: mixed
        :param $value: Curl option value
        :returns: Request Self, for message chaining

    .. php:method:: getCurlOptions()

        Get the cURL options for this request.

        :returns: array Curl configuration options

    .. php:method:: setUserAgent($userAgent)

        Set the value of the User-Agent header for this request.

        :type $userAgent: string
        :param $userAgent: The User-Agent
        :returns: Request Self, for message chaining

    .. php:method:: getUserAgent()

        Get the value of the User-Agent header for this request.

        :returns: string The User-Agent

    .. php:method:: setReferrer($ref)

        Set the referring URL that this request is realted to.

        :type $ref: string
        :param $ref: URL to report to server in "Referer" header
        :returns: Request Self, for message chaining

    .. php:method:: setReferer($ref)

        Synonym for setReferrer().

        :type $ref: string
        :param $ref: URL to report to server in "Referer" header
        :returns: Request Self, for message chaining

    .. php:method:: setConnectTimeout($ms)

        Set HTTP connect timeout (in milliseconds).

        :type $ms: int
        :param $ms: Connect timeout in millseconds
        :returns: Request Self, for message chaining

    .. php:method:: setTimeout($ms)

        Set HTTP timeout (in milliseconds).

        :type $ms: int
        :param $ms: Timeout in millseconds
        :returns: Request Self, for message chaining

    .. php:method:: setCredentials($user, $password, $type = CURLAUTH_ANYSAFE)

        Set credentials for authenticating to remote host.

        :type $user: string
        :param $user: Username
        :type $password: string
        :param $password: Password
        :param $type:
        :returns: Request Self, for message chaining

    .. php:method:: setX509Credentials($cert, $key, $keypass, $type = 'PEM')

        Set x509 credentials for authenticating to remote host.

        :type $cert: string
        :param $cert: Path to x509 certificate
        :type $key: string
        :param $key: Patch to x509 private key
        :type $keypass: string
        :param $keypass: Passphrase to decrypt private key
        :type $type: string
        :param $type: Certificate encoding (PEM|DER|ENG)
        :returns: Request Self, for message chaining

    .. php:method:: setCookieJar($file)

        Read and store cookies in the provided file.

        :type $file: string
        :param $file: Path to cookie storage file
        :returns: Request Self, for message chaining

    .. php:method:: failIfNot200($flag)

        Set the default behavior when a request returns a non-200 status code.

        :type $flag: bool
        :param $flag: True to throw an exception, false otherwise
        :returns: Request Self, for message chaining

    .. php:method:: wasSubmitted()

        Check to see if this request has been submitted yet.

        :returns: bool True if request has been submitted, false otherwise.

    .. php:method:: throwIfNotSubmitted()

        Throw a \RuntimeException if this request has not been submitted
        yet.

        :returns: void

    .. php:method:: getResponseHttpCode()

        Get the HTTP response code sent by the server.

        :returns: int HTTP response code

    .. php:method:: setResponseHttpCode($code)

        Set the HTTP response code sent by the server.

        :type $code: int
        :param $code: HTTP response code
        :returns: Request Self, for message chaining

    .. php:method:: getResponseHeaders()

        Get the HTTP response headers sent by the server.

        Keys in the header array are the header names. The value is either the raw
        header contents or an array of raw header contents if that particular
        header appeared more than once in the response.

        :returns: array HTTP response headers

    .. php:method:: getResponseHeader($name)

        Get a particular HTTP response header sent by the server.

        :type $name: string
        :param $name: Header name
        :returns: mixed Header value or null if not found. Value may be an array if the named header occured more than once in the server's response.

    .. php:method:: setResponseHeaders($headers)

        Set the HTTP response headers sent by the server.

        :type $headers: array
        :param $headers: HTTP response headers
        :returns: Request Self, for message chaining

    .. php:method:: getResponseBody()

        Get the HTTP response body sent by the server.

        :returns: string HTTP response body

    .. php:method:: setResponseBody($body)

        Set the HTTP response body sent by the server.

        :type $body: array
        :param $body: HTTP response body
        :returns: Request Self, for message chaining

    .. php:method:: getResponseCurlInfo()

        Get the cURL response information.

        :returns: string HTTP response body

    .. php:method:: setResponseCurlInfo($info)

        Set the cURL response information.

        :type $info: array
        :param $info: Curl info
        :returns: Request Self, for message chaining

    .. php:method:: submit($failIfNot200 = null)

        Submit this request.

        This request will be updated with the results of the request which can
        then be retrieved using getResponseHttpCode() and releated methods.

        :type $failIfNot200: bool
        :param $failIfNot200: Throw an exception if a non-200 status was sent?
        :returns: Request Request with response data populated

    .. php:method:: createCurlRequest()

        Prepare a cURL handle for this request.

        :returns: resource Curl handle ready to be submitted

    .. php:method:: processCurlResponse($ch, $errCode, $errMsg, $rawResp)

        Process an submitted cURL response.

        :type $ch: resource
        :param $ch: Curl handle
        :param $errCode:
        :param $errMsg:
        :param $rawResp:
        :returns: Request Request with response data populated

    .. php:method:: validateResponse($failIfNot200 = null)

        Check the cURL response code and throw an exception if it is an error.

        :type $failIfNot200: bool
        :param $failIfNot200: Throw an exception if a non-200 status was sent?
        :returns: void

    .. php:method:: parallelSubmit($requests)

        Submit a group of requests in parallel.

        Uses the curl_multi_exec engine to fire off several requests in parallel
        and waits for all responses to finish before returing the collective
        results.

        :type $requests: array
        :param $requests: List of requests to submit
        :returns: array List of submitted requests

    .. php:method:: handleMultiResponse($info, $mh, $handles)

        Handle a curl_multi_info_read() response message.

        :type $info: array
        :param $info: Status message from Curl
        :type $mh: resource
        :param $mh: Curl multi handle
        :param $handles:
        :returns: void

    .. php:method:: get($url, $parms = null, $options = null)

        Convenience method to perform a GET request.

        Provided parameters will be "application/x-www-form-urlencoded" encoded
        and appended to the provided URL.

        :type $url: string
        :param $url: URL to get (eg https://www.keynetics.com/page.php)
        :type $parms: array
        :param $parms: Array of key => value pairs to send
        :type $options: array
        :param $options: Array of extra options to pass to cURL
        :returns: Request Submitted request

    .. php:method:: post($url, $parms, $options = null)

        Convenience method to POST data to a URL and retrieve the results.

        Provided parms will be encoded as "application/x-www-form-urlencoded"
        data before being sent.

        :type $url: string
        :param $url: Full URL to post to (eg https://www.keynetics.com/page.php)
        :type $parms: array
        :param $parms: Array of key => value pairs to post
        :type $options: array
        :param $options: Array of extra options to pass to cURL
        :returns: Request Submitted request

    .. php:method:: postContent($url, $content, $contentType = 'text/xml', $options = null)

        Convenience method to POST content in the form of a raw string to a URL.

        This is useful for manually constructed SOAP requests and other document
        body type operations. Default content type is text/xml.

        :type $url: string
        :param $url: Full URL to post to (eg https://www.keynetics.com/page.php)
        :type $content: string
        :param $content: Raw HTTP request body to be posted
        :type $contentType: string
        :param $contentType: Value of the HTTP Content-Type header
        :type $options: array
        :param $options: Array of extra options to pass to cURL
        :returns: Request Submitted request

    .. php:method:: postMultipart($url, $parms, $options = null)

        Convenience method to POST data to a URL and retrieve the results.

        Provided parms will be encoded as "multipart/form-data" data before being
        sent.

        :type $url: string
        :param $url: Full URL to post to (eg https://www.keynetics.com/page.php)
        :type $parms: array
        :param $parms: Array of key => value pairs to post
        :type $options: array
        :param $options: Array of extra options to pass to cURL
        :returns: Request Submitted request
