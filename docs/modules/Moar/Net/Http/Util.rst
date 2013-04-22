---------------------
Moar\\Net\\Http\\Util
---------------------

.. php:namespace: Moar\\Net\\Http

.. php:class:: Util

    HTTP utilities.

    .. php:method:: urlEncode($parms)

        Make a URL-encoded string from a key=>value array

        :type $parms: array
        :param $parms: Parameter array
        :returns: string URL-encoded message body

    .. php:method:: mergeCurlOptions($base, $additional)

        Merge two arrays of curl options together into a new array.

        Values in the additional array will override values in the base array
        except in the case of CURLOPT_HTTPHEADER where values from the additional
        array will be merged with values from the base array if any exist.

        The additional array can be keyed with either ints which will be assumed
        to be CURLOPT_* values or strings such as 'CURLOPT_USERPWD' which will be
        turned into ints via constant(). This makes setting up options in a DI or
        other non-php scripted senario easier to implement.

        :type $base: array
        :param $base: Base options
        :type $additional: array
        :param $additional: Additional options
        :returns: array New array of base options with additional options overlayed

    .. php:method:: ensureCurlErrorConstants()

        Ensure that constants are available for useful cURL error codes.

        :returns: void

    .. php:method:: addQueryData($url, $parms)

        Append a query string to the given URL.

        :type $url: string
        :param $url: URL to append to
        :type $parms: string|array
        :param $parms: Parameters to add as query string to url
        :returns: string Composed URL

    .. php:method:: assembleUrl($parts)

        Assemble a URL from a array of components as would be returned by
        parse_url().

        :type $parts: array
        :param $parts: URL parts
        :returns: string URL

    .. php:method:: parseCookieHeader($hdr)

        Parse a "Set-Cookie" header to get the component cookie data.

        :type $hdr: string
        :param $hdr: Header data
        :returns: array Collection of cookies specified by the header

    .. php:method:: parseCookieElement($elm)

        Parse a single cookie setting.

        :type $elm: string
        :param $elm: Cookie element
        :returns: array Associative array of cookie data

    .. php:method:: __construct()

        Construction disallowed.
