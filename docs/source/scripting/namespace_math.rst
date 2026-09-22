*math* Namespace
================

The functions in this namespace provide support for common math functions. This namespace is available for biome conditions, acoustic filtering, and chance percentages.

.. js:data:: Double math.PI

    Returns the value of π (pi).

    :type: Double

.. js:data:: Double math.TAU

    Returns the value of 2π (tau).

    :type: Double

.. js:data:: Double math.e

    Returns the value of e (Euler's number).

    :type: Double

.. js:function:: Double math.sin(Double value)

    Returns the sine of the specified value.

    :param value: The value to calculate the sign of
    :type value: Double
    :return: The sign of the specified value
    :rtype: Double

.. js:function:: Double math.cos(Double value)

    Returns the cosine of the specified value.

    :param value: The value to calculate the cosine of
    :type value: Double
    :return: The cosine of the specified value
    :rtype: Double

.. js:function:: Double math.tan(Double value)

    Returns the tangent of the specified value.

    :param value: The value to calculate the tangent of
    :type value: Double
    :return: The tangent of the specified value
    :rtype: Double

.. js:function:: Double math.toDegrees(Double radians)

    Converts the radians value to degrees.

    :param radians: The radians value to convert to degrees
    :type radians: Double
    :return: The number of degrees equivalent to the specified radians value
    :rtype: Double

.. js:function:: Double math.toRadians(Double degrees)

    Converts the degrees value to radians.

    :param degrees: The degrees value to convert to radians
    :type degrees: Double
    :return: The number of radians equivalent to the specified degrees value
    :rtype: Double

.. js:function:: Double math.pow(Double base, Double exponent)

    Returns the value of a base expression taken to a specified power.

    :param base: The base value
    :type base: Double
    :param exponent: The exponent value
    :type exponent: Double
    :return: The result of the base raised to the specified power
    :rtype: Double

.. js:function:: Double math.log(Double value)

    Returns the natural logarithm of a specified value.

    :param value: The value to calculate the natural logarithm of
    :type value: Double
    :return: The natural logarithm of the specified value
    :rtype: Double

.. js:function:: Double math.exp(Double value)

    Returns e raised to the specified power.

    :param value: The exponent to raise e to
    :type value: Double
    :return: The result of e raised to the specified power
    :rtype: Double

.. js:function:: Double math.sqrt(Double value)

    Returns the square root of a specified value.

    :param value: The value to calculate the square root of
    :type value: Double
    :return: The square root of the specified value
    :rtype: Double

.. js:function:: Double math.round(Double value [, Integer places])

    Rounds a double value to a specified number of decimal places. If the number of decimal places is not specified, the value will be rounded to the nearest whole number.

    :param value: The value to round
    :type value: Double
    :param places: The number of decimal places to round to
    :type places: Integer
    :return: The rounded value
    :rtype: Double

.. js:function:: Double math.abs(Double value)

    Returns the absolute value of a double.

    :param value: The value to calculate the absolute value of
    :type value: Double
    :return: The absolute value of the specified value
    :rtype: Double

.. js:function:: Double math.random()

    Returns a random double greater than or equal to 0.0 and less than 1.0.

    :return: A random double
    :rtype: Double
