*weather* Namespace
===================

This namespace has all functions related to weather.

.. note::
    These functions are not available for biome condition scripts.

.. js:function:: Boolean weather.isRaining()

    Evaluates if it is currently raining in the player's dimension.

    :return: Returns ``true`` if it is current raining, ``false`` otherwise.
    :rtype: Boolean

.. js:function:: Boolean weather.isThundering()

    Evaluates if a thunderstorm is occurring.

    :return: Returns ``true`` if the current weather is a thunderstorm, ``false`` otherwise.
    :rtype: Boolean

.. js:function:: Boolean weather.isNotRaining()

    Evaluates if it is not currently raining in the player's dimension.

    :return: Returns ``true`` if it is not raining, ``false`` otherwise.
    :rtype: Boolean

.. js:function:: Boolean weather.isNotThundering()

    Evaluates if it is not currently thundering in the player's dimension.

    :return: Returns ``true`` if the current weather is not a thunder storm, ``false`` otherwise.
    :rtype: Boolean

.. js:function:: Float weather.getRainIntensity()

    Returns the intensity of the rainfall in the player's dimension.

    :return: Returns the current rain intensity as a ``float``. When it is raining, this value will be 0.0. If it is raining, the value will be 0.0 - 1.0 depending on where Minecraft is with the startup of rain.
    :rtype: Float

.. js:function:: Float weather.getThunderIntensity()

    Returns the intensity of thunder in the player's dimension.

    :return: Returns the current intensity of thunder storm as a ``float``.
    :rtype: Float

.. js:function:: Float weather.getTemperature()

    Returns the current temperature at the players location.

    :return: The temperature at the player's location
    :rtype: Float

.. js:function:: Boolean weather.isFrosty()

    Evaluates if it is cold enough for frost.

    :return: Returns ``true`` if the current temperature is low enough for breath effects, ``false`` otherwise.
    :rtype: Boolean

.. js:function:: Boolean weather.canWaterFreeze()

    Evaluates if water can freeze at the player's location.

    :return: Returns ``true`` if the temperature is low enough for water to freeze, ``false`` otherwise.
    :rtype: Boolean