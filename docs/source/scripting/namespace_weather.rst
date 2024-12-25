*weather* Namespace
===================

This namespace has all functions related to weather.

.. note::
    These functions are not available for biome condition scripts.

.. code-block:: javascript

    Boolean isRaining()

Returns ``true`` if it is current raining, ``false`` otherwise.

.. code-block:: javascript

    Boolean isThundering()

Returns ``true`` if the current weather is a thunderstorm, ``false`` otherwise.

.. code-block:: javascript

    Boolean isNotRaining()

Returns ``true`` if it is not raining, ``false`` otherwise.

.. code-block:: javascript

    Boolean isNotThundering()

Returns ``true`` if the current weather is not a thunder storm, ``false`` otherwise.

.. code-block:: javascript

    Float getRainIntensity()

Returns the current rain intensity as a ``float``. When it is raining, this value will be 0.0. If it is raining, the value will be 0.0 - 1.0 depending on where Minecraft is with the startup of rain.

.. code-block:: javascript

    Float getThunderIntensity()

Returns the current intensity of thunder storm as a ``float``.

.. code-block:: javascript

    Float getTemperature()

Returns the current temperature at the players location.

.. code-block:: javascript

    Boolean isFrosty()

Returns ``true`` if the current temperature is low enough for breath effects, ``false`` otherwise.

.. code-block:: javascript

    Boolean canWaterFreeze()

Returns ``true`` if the temperature is low enough for water to freeze, ``false`` otherwise.