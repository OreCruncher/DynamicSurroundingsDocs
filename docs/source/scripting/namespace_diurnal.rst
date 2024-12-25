*diurnal* Namespace
===================

Functions related to the time of day and the moon.

.. note::
    These functions are not available for biome condition scripts.

.. js:function:: Boolean diurnal.isDay()

    Indicates whether it is currently daytime in the player dimension.

    :return: Returns ``true`` if it is day, ``false`` otherwise.
    :rtype: Boolean

.. js:function:: Boolean diurnal.isNight()

    Indicates whether it is currently nighttime in the player dimension.

    :return: Returns ``true`` if it is nighttime, ``false`` otherwise.
    :rtype: Boolean

.. js:function:: Boolean diurnal.isSunrise()

    Indicates whether it is currently sunrise in the player dimension.

    :return: Returns ``true`` if it is sunrise, ``false`` otherwise.
    :rtype: Boolean

.. js:function:: Boolean diurnal.isSunset()

    Indicates whether it is currently sunset in the player dimension.

    :return: Returns ``true`` if it is sunset, ``false`` otherwise.
    :rtype: Boolean

.. js:function:: Float diurnal.getMoonPhaseFactor()

    Gets the current phase of the moon as a ``float``.

    :return: 0.0 - 1.0, with 0.0 being the new moon, and 1.0 as a full moon.
    :rtype: Float

.. js:function:: Float diurnal.getCelestialAngle()

    Gets the current celestial angle of the sun, in radians (if I recall correctly).

    :return: Celestial angle of the sun
    :rtype: Float