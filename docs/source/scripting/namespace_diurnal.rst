*diurnal* Namespace
===================

.. code-block:: javascript

    Boolean isDay()
    Boolean isNight()
    Boolean isSunrise()
    Boolean isSunset()

Returns ``true`` if the current time of day is consider day, night, sunrise, or sunset.

.. code-block:: javascript

    Float getMoonPhaseFactor()

Returns the current phase of the moon as a ``float``, with 0.0 being the new moon, and 1.0 as a full moon.

.. code-block:: javascript

    Float getCelestialAngle()

Returns the current angle of the sun, in radians (if I recall correctly).