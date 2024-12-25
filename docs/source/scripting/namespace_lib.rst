*lib* Namespace
===============

The functions in this namespace provide support for common things that a script may do. This namespace is available for biome conditions, acoustic filtering, and chance percentages.

.. js:function:: Object lib.iif(boolean result, Object trueResult, Object falseResult)

    Selects an object based on a boolean result.

    :param result: A boolean valuethat is used to make a result selection
    :type result: Boolean
    :param trueResult: The object to return if the result is ``true``
    :type trueResult: Object
    :param falseResult: The object to return if the result is ``false``
    :type falseResult: Object
    :return: ``trueResult`` or ``falseResult`` depending on the value of ``result``.
    :rtype: Object

.. js:function:: Boolean lib.match(String pattern, String input)

    Determines if the input matches the regular expression.

    :param pattern: Regular expression to use for matching
    :type pattern: String
    :param input: The input to tapestry
    :type input: String
    :return: Applies the provided regular expression ``pattern`` to determine if ``input`` is a match.
    :rtype: Boolean

.. js:function:: Boolean lib.oneof(Object input, Object... possibles)

    Determines of the input object is contained within the possible array.

    :param input: The input object of interest
    :type input: Object
    :param possibles: The possible values to check for
    :type possibles: Array
    :return: ``true`` if ``input`` matches one of the possible objects, ``false`` otherwise
    :rtype: Boolean

.. js:function:: Boolean lib.isBetween(Double value, Double min, Double max)

    Determines if the value is in between the min and max values, inclusive.

    :param value: The value to check for
    :type value: Double
    :param min: The minimum value of the interval
    :type min: Double
    :param max: The maximum value of the interval
    :type max: Double
    :return: ``true`` if ``value`` is between ``min`` and ``max``, inclusive.
    :rtype: Boolean

.. js:function:: Boolean lib.isModLoaded(String modId)

    Indicates whether the specified mod is loaded.

    :param modId: The ID of the mod to test for
    :type modId: String
    :return: ``true`` if the mod is present, ``false`` otherwise
    :rtype: Boolean