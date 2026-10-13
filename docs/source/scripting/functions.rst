Script Functions
================

The functions and constants available to scripts, grouped by namespace. For how scripts are written, see :doc:`scripting`.

The ``biome``, ``lib``, ``math``, and ``platform`` namespaces can be used in every script. The others describe the game as it is being played, so they are not
available to biome selector scripts, which run during configuration.

.. _namespace-biome:

biome
-----

These functions apply to biomes, and can be used in two different contexts:

* In game, these functions can be used to query information about the biome where the player is currently located.
* During configuration, these functions can be used in a biome condition filter to determine if a rule applies to a given biome.

Traits passed to ``is``, ``isAllOf``, and ``isOneOf`` are not case sensitive, and an unknown trait name is reported as an error.

For a list of possible :term:`biome traits <Biome Trait>` refer to :doc:`biometraits`.

.. js:function:: biome.getName()

    Returns the localized name of the biome.

    :return: The name of the biome
    :rtype: String

.. js:function:: biome.getModId()

    Returns the mod ID that the biome is associated with.

    :return: The biomes mod ID
    :rtype: String

.. js:function:: biome.getId()

    Returns the :term:`resource location <Resource Location>` ID of the biome.

    :return: The biome's resource location ID
    :rtype: String

.. js:function:: biome.getRainfall()

    Returns the average rainfall of the biome.

    :return: Biome's average rainfall
    :rtype: Float

.. js:function:: biome.getTemperature()

    Returns the average temperature of the biome.

    :return: Biome's average temperature
    :rtype: Float

.. js:function:: biome.getPrecipitationType()

    Returns the precipitation that occurs within the biome. Possible values are ``NONE``, ``RAIN``, and ``SNOW``. During configuration the value is based on the biome's own settings rather
    than the current world, so a rule gives the same answer regardless of where the player is.

    :return: The type of precipitation the biome usually has
    :rtype: String

.. js:function:: biome.getTraits()

    Gets the list of biome traits, as a string. Useful with ``/dsscript`` to see what traits a biome has.

    :return: Traits of the biome as a comma separated list in brackets (ex, ``[forest, overworld, temperate]``)
    :rtype: String

.. js:function:: biome.is(String trait)

    Checks to see if the biome has the specified trait.

    :param trait: The trait to check for
    :type trait: String
    :return: Returns ``true`` if the biome has the specified trait, ``false`` otherwise.
    :rtype: Boolean

.. js:function:: biome.isAllOf(String... traits)

    Checks to see if the biome has all the specified traits.

    :param traits: Array of traits to check for
    :type traits: String[]
    :return: Returns ``true`` if the biome has all the specified traits, ``false`` otherwise.
    :rtype: Boolean

.. js:function:: biome.isOneOf(String... traits)

    Checks to see if the biome has at least one of the specified traits.

    :param traits: Array of traits to check for
    :type traits: String[]
    :return: Returns ``true`` if the biome has one of the specified traits, ``false`` otherwise.
    :rtype: Boolean

.. _namespace-dim:

dim
---

Namespace containing functions related to the player's current dimension.

.. note::
    These functions are not available for biome condition scripts.

.. js:function:: dim.getId()

    Gets the ID of the dimension as a string.

    :return: The resource location ID of the dimension
    :rtype: String

.. js:function:: dim.getDimName()

    Gets the name of the dimension, which is the path portion of the dimension's :term:`resource location <Resource Location>` ID (for example, ``overworld`` for ``minecraft:overworld``).

    :return: The dimension name
    :rtype: String

.. js:function:: dim.hasSky()

    Returns whether the dimension has a sky.

    :return: Returns ``true`` if the dimension has a sky, ``false`` otherwise.
    :rtype: Boolean

.. js:function:: dim.isSuperFlat()

    Returns whether the dimension is super flat.

    :return: Returns ``true`` if the current dimension is super flat, ``false`` otherwise.
    :rtype: Boolean

.. _namespace-diurnal:

diurnal
-------

Functions related to the time of day and the moon.

.. note::
    These functions are not available for biome condition scripts.

.. js:function:: diurnal.isDay()

    Indicates whether it is currently daytime in the player dimension.

    :return: Returns ``true`` if it is day, ``false`` otherwise.
    :rtype: Boolean

.. js:function:: diurnal.isNight()

    Indicates whether it is currently nighttime in the player dimension.

    :return: Returns ``true`` if it is nighttime, ``false`` otherwise.
    :rtype: Boolean

.. js:function:: diurnal.isSunrise()

    Indicates whether it is currently sunrise in the player dimension.

    :return: Returns ``true`` if it is sunrise, ``false`` otherwise.
    :rtype: Boolean

.. js:function:: diurnal.isSunset()

    Indicates whether it is currently sunset in the player dimension.

    :return: Returns ``true`` if it is sunset, ``false`` otherwise.
    :rtype: Boolean

.. js:function:: diurnal.getMoonPhaseFactor()

    Gets the current phase of the moon as a ``float``.

    :return: 0.0 - 1.0, with 0.0 being the new moon, and 1.0 as a full moon.
    :rtype: Float

.. js:function:: diurnal.getCelestialAngle()

    Gets the current celestial angle of the sun, as a fraction of a full day cycle. 0.0 is noon, 0.25 is sunset, 0.5 is midnight, and 0.75 is sunrise.

    :return: Celestial angle of the sun, 0.0 - 1.0
    :rtype: Float

.. _namespace-global:

global
------

.. note::
    These functions are not available for biome condition scripts.

.. js:function:: global.allowScary()

    Indicates whether scary effects are eligable for activation.

    :return: Returns the current flag from the configuration file. ``true`` if scary sounds are permitted, ``false`` otherwise.
    :rtype: Boolean

.. _namespace-lib:

lib
---

The functions in this namespace provide support for common things that a script may do. This namespace is available for biome conditions, :term:`acoustic <Acoustic>` filtering, and chance percentages.

.. js:function:: lib.iif(boolean result, Object trueResult, Object falseResult)

    Selects an object based on a boolean result.

    :param result: A boolean value that is used to make a result selection
    :type result: Boolean
    :param trueResult: The object to return if the result is ``true``
    :type trueResult: Object
    :param falseResult: The object to return if the result is ``false``
    :type falseResult: Object
    :return: ``trueResult`` or ``falseResult`` depending on the value of ``result``.
    :rtype: Object

.. js:function:: lib.match(String pattern, String input)

    Determines if the entire input matches the regular expression.

    :param pattern: Regular expression to use for matching
    :type pattern: String
    :param input: The input to test
    :type input: String
    :return: Applies the provided regular expression ``pattern`` to determine if ``input`` is a match.
    :rtype: Boolean

.. js:function:: lib.oneOf(Object input, Object... possibles)

    Determines if the input object is contained within the possible array.

    :param input: The input object of interest
    :type input: Object
    :param possibles: The possible values to check for
    :type possibles: Array
    :return: ``true`` if ``input`` matches one of the possible objects, ``false`` otherwise
    :rtype: Boolean

.. js:function:: lib.isBetween(Double value, Double min, Double max)

    Determines if the value is in between the min and max values, inclusive.

    :param value: The value to check for
    :type value: Double
    :param min: The minimum value of the interval
    :type min: Double
    :param max: The maximum value of the interval
    :type max: Double
    :return: ``true`` if ``value`` is between ``min`` and ``max``, inclusive.
    :rtype: Boolean

.. js:function:: lib.isModLoaded(String modId)

    Indicates whether the specified mod is loaded. Use :js:func:`platform.isModLoaded` instead. (*Removed 1.21.1-0.4.3*)

.. _namespace-math:

math
----

The functions in this namespace provide support for common math functions. This namespace is available for biome conditions, :term:`acoustic <Acoustic>` filtering, and chance percentages.

.. js:data:: math.pi

    Returns the value of π (pi).

    :type: Double

.. js:data:: math.tau

    Returns the value of 2π (tau).

    :type: Double

.. js:data:: math.e

    Returns the value of e (Euler's number).

    :type: Double

.. js:function:: math.sin(Double value)

    Returns the sine of the specified value.

    :param value: The value, in radians, to calculate the sine of
    :type value: Double
    :return: The sine of the specified value
    :rtype: Double

.. js:function:: math.cos(Double value)

    Returns the cosine of the specified value.

    :param value: The value, in radians, to calculate the cosine of
    :type value: Double
    :return: The cosine of the specified value
    :rtype: Double

.. js:function:: math.tan(Double value)

    Returns the tangent of the specified value.

    :param value: The value, in radians, to calculate the tangent of
    :type value: Double
    :return: The tangent of the specified value
    :rtype: Double

.. js:function:: math.toDegrees(Double radians)

    Converts the radians value to degrees.

    :param radians: The radians value to convert to degrees
    :type radians: Double
    :return: The number of degrees equivalent to the specified radians value
    :rtype: Double

.. js:function:: math.toRadians(Double degrees)

    Converts the degrees value to radians.

    :param degrees: The degrees value to convert to radians
    :type degrees: Double
    :return: The number of radians equivalent to the specified degrees value
    :rtype: Double

.. js:function:: math.pow(Double base, Double exponent)

    Returns the value of a base expression taken to a specified power.

    :param base: The base value
    :type base: Double
    :param exponent: The exponent value
    :type exponent: Double
    :return: The result of the base raised to the specified power
    :rtype: Double

.. js:function:: math.log(Double value)

    Returns the natural logarithm of a specified value.

    :param value: The value to calculate the natural logarithm of
    :type value: Double
    :return: The natural logarithm of the specified value
    :rtype: Double

.. js:function:: math.exp(Double value)

    Returns e raised to the specified power.

    :param value: The exponent to raise e to
    :type value: Double
    :return: The result of e raised to the specified power
    :rtype: Double

.. js:function:: math.sqrt(Double value)

    Returns the square root of a specified value.

    :param value: The value to calculate the square root of
    :type value: Double
    :return: The square root of the specified value
    :rtype: Double

.. js:function:: math.round(Double value [, Integer places])

    Rounds a double value to a specified number of decimal places. If the number of decimal places is not specified, the value will be rounded to the nearest whole number.

    :param value: The value to round
    :type value: Double
    :param places: The number of decimal places to round to. A negative value rounds to the left of the decimal point, so ``math.round(1234, -2)`` is ``1200``.
    :type places: Integer
    :return: The rounded value
    :rtype: Double

.. js:function:: math.abs(Double value)

    Returns the absolute value of a double.

    :param value: The value to calculate the absolute value of
    :type value: Double
    :return: The absolute value of the specified value
    :rtype: Double

.. js:function:: math.random()

    Returns a random double greater than or equal to 0.0 and less than 1.0.

    :return: A random double
    :rtype: Double

.. _namespace-platform:

platform
--------

*Added in 1.21.1-0.4.3*

These functions are related to the runtime environment of the Minecraft client. This namespace is available for biome conditions, :term:`acoustic <Acoustic>` filtering, and chance percentages.

.. js:function:: platform.isModLoaded(String modId)

    Indicates whether the specified mod is loaded.

    :param modId: The ID of the mod to test for
    :type modId: String
    :return: ``true`` if the mod is present, ``false`` otherwise
    :rtype: Boolean

.. js:function:: platform.isCurrentDateInRangeOf(Integer month, Integer day, Integer dayRange)

    Indicates whether today's date, in the player's local time zone, is within ``dayRange`` days of the specified month and day, in either direction. Useful for holiday effects. Ranges that
    cross the new year work as expected; for example, ``platform.isCurrentDateInRangeOf(1, 1, 3)`` is ``true`` from December 29 through January 4. An impossible date (such as month 13 or
    February 30) never matches.

    :param month: The month, 1 - 12
    :type month: Integer
    :param day: The day of the month
    :type day: Integer
    :param dayRange: The number of days before and after the date that are considered in range
    :type dayRange: Integer
    :return: ``true`` if the current date is within range, ``false`` otherwise
    :rtype: Boolean

.. _namespace-player:

player
------

Functions in this namespace are related to the state of the current player.

.. note::
    These functions are not available for biome condition scripts.

.. js:function:: player.isCreative()

    Evaluates whether the player is in creative mode.

    :return: ``true`` if the player is in creative mode, ``false`` otherwise.
    :rtype: Boolean

.. js:function:: player.isBurning()

    Evaluates whether the player is burning.

    :return: ``true`` if the player is burning, ``false`` otherwise.
    :rtype: Boolean

.. js:function:: player.isSuffocating()

    Evaluates whether the player is suffocating.

    :return: ``true`` if the player is suffocating, ``false`` otherwise.
    :rtype: Boolean

.. js:function:: player.isFlying()

    Evaluates whether the player is flying.

    :return: ``true`` if the player is flying, ``false`` otherwise.
    :rtype: Boolean

.. js:function:: player.isSprinting()

    Evaluates whether the player is sprinting.

    :return: ``true`` if the player is sprinting, ``false`` otherwise.
    :rtype: Boolean

.. js:function:: player.isInLava()

    Evaluates whether the player is located within lava.

    :return: ``true`` if the player is in lava, ``false`` otherwise.
    :rtype: Boolean

.. js:function:: player.isInvisible()

    Evaluates whether the player is invisible.

    :return: ``true`` if the player is invisible, ``false`` otherwise.
    :rtype: Boolean

.. js:function:: player.isInWater()

    Evaluates whether the player's head is under water.

    :return: ``true`` if the player is under water, ``false`` otherwise.
    :rtype: Boolean

.. js:function:: player.isMoving()

    Evaluates whether the player is moving horizontally.

    :return: ``true`` if the player is moving, ``false`` otherwise.
    :rtype: Boolean

.. js:function:: player.isWet()

    Evaluates whether the player is wet, either by being in water or standing in the rain.

    :return: ``true`` if the player is wet, ``false`` otherwise.
    :rtype: Boolean

.. js:function:: player.isRiding()

    Evaluates whether the player is riding an entity such as a horse or minecart.

    :return: ``true`` if the player is riding, ``false`` otherwise.
    :rtype: Boolean

.. js:function:: player.isOnGround()

    Evaluates whether the player is on the ground.

    :return: ``true`` if the player is on the ground, ``false`` otherwise.
    :rtype: Boolean

.. js:function:: player.canRainOn()

    Evaluates whether the player is in the open where rain can fall on them.

    :return: ``true`` if the player can be rained on, ``false`` otherwise.
    :rtype: Boolean

.. js:function:: player.canSeeSky()

    Evaluates whether the player is able to see the sky when looking up.

    :return: ``true`` if the player can see the sky, ``false`` otherwise.
    :rtype: Boolean

.. js:function:: player.getHealth()

    Gets the current health of the player.

    :return: Player's current health
    :rtype: Float

.. js:function:: player.getMaxHealth()

    Gets the players maximum possible health value.

    :return: Player's maximum health
    :rtype: Float

.. js:function:: player.getFoodLevel()

    Gets the players current food level.

    :return: Player's current food level
    :rtype: Float

.. js:function:: player.getFoodSaturationLevel()

    Gets the player's current food saturation level.

    :return: Player's current food saturation level.
    :rtype: Float

.. js:function:: player.getX()

    Gets the player's current X position.

    :return: X position of the player
    :rtype: Double

.. js:function:: player.getY()

    Gets the player's current Y position.

    :return: Y position of the player
    :rtype: Double

.. js:function:: player.getZ()

    Gets the player's current Z position.

    :return: Z position of the player
    :rtype: Double

.. js:function:: player.hasEffect(String effect)

    Evaluates whether the player has the specified effect. The effect is expressed as a :term:`resource location <Resource Location>` ID.

    :param effect: The effect to check for
    :type effect: String
    :return: Returns ``true`` if the player has the given effect, ``false`` otherwise.
    :rtype: Boolean

.. _namespace-season:

season
------

This namespace provides information about the current season, if any. If Serene Seasons is installed, this information will reflect the current season defined by Serene Seasons.
If Serene Seasons is not installed, the season will always be Spring.

.. note::
    These functions are not available for biome condition scripts.

.. js:function:: season.isSpring()

    Evaluates whether the current season is Spring

    :return: ``true`` if it is Spring, ``false`` otherwise.
    :rtype: Boolean

.. js:function:: season.isSummer()

    Evaluates whether the current season is Summer

    :return: ``true`` if it is Summer, ``false`` otherwise.
    :rtype: Boolean

.. js:function:: season.isAutumn()

    Evaluates whether the current season is Autumn

    :return: ``true`` if it is Autumn, ``false`` otherwise.
    :rtype: Boolean

.. js:function:: season.isWinter()

    Evaluates whether the current season is Winter

    :return: ``true`` if it is Winter, ``false`` otherwise.
    :rtype: Boolean

.. js:function:: season.isEarly()

    Evaluates whether the current period within a season is early. If a season mod is not installed it will always return ``true``. (*Added 1.21.1-0.4.4*)

    :return: ``true`` if it is early in the season, ``false`` otherwise.
    :rtype: Boolean

.. js:function:: season.isMiddle()

    Evaluates whether the current period within a season is the middle. If a season mod is not installed it will always return ``true``. (*Added 1.21.1-0.4.4*)

    :return: ``true`` if it is middle of the season, ``false`` otherwise.
    :rtype: Boolean

.. js:function:: season.isLate()

    Evaluates whether the current period within a season is late. If a season mod is not installed it will always return ``true``. (*Added 1.21.1-0.4.4*)

    :return: ``true`` if it is late in the season, ``false`` otherwise.
    :rtype: Boolean

.. _namespace-state:

state
-----

.. note::
    These functions are not available for biome condition scripts.

.. js:function:: state.isInVillage()

    Evaluates whether the player is within 64 blocks of a bell and villagers are present.

    :return: Returns ``true`` if the player is within 64 blocks of a bell and villagers are present, ``false`` otherwise.
    :rtype: Boolean

.. js:function:: state.isInside()

    Evaluates whether the player is under cover. Note that some blocks do not count as cover, such as leaf blocks and fences.

    :return: Returns ``true`` if the area scanner determines the player is under cover, ``false`` otherwise.
    :rtype: Boolean

.. js:function:: state.isUnderwater()

    Evaluates whether the player's head is inside a liquid block.

    :return: Returns ``true`` if the player's head is in water, ``false`` otherwise.
    :rtype: Boolean

.. _namespace-weather:

weather
-------

This namespace has all functions related to weather.

.. note::
    These functions are not available for biome condition scripts.

.. js:function:: weather.isRaining()

    Evaluates if it is currently raining in the player's dimension.

    :return: Returns ``true`` if it is current raining, ``false`` otherwise.
    :rtype: Boolean

.. js:function:: weather.isThundering()

    Evaluates if a thunderstorm is occurring.

    :return: Returns ``true`` if the current weather is a thunderstorm, ``false`` otherwise.
    :rtype: Boolean

.. js:function:: weather.isNotRaining()

    Evaluates if it is not currently raining in the player's dimension.

    :return: Returns ``true`` if it is not raining, ``false`` otherwise.
    :rtype: Boolean

.. js:function:: weather.isNotThundering()

    Evaluates if it is not currently thundering in the player's dimension. Use ``!weather.isThundering()`` instead. (*Removed 1.21.1-0.4.3*)

.. js:function:: weather.getRainIntensity()

    Returns the intensity of the rainfall in the player's dimension.

    :return: Returns the current rain intensity as a ``float``. When it is not raining, this value will be 0.0. If it is raining, the value will be 0.0 - 1.0 depending on where Minecraft is with the startup of rain. When storm simulation is enabled, the value reflects the simulated storm's strength rather than Minecraft's rain level. (*Storm strength used starting 1.21.1-0.4.7*)
    :rtype: Float

.. js:function:: weather.getThunderIntensity()

    Returns the intensity of thunder in the player's dimension.

    :return: Returns the current intensity of thunder storm as a ``float``.
    :rtype: Float

.. js:function:: weather.getTemperature()

    Returns the current temperature at the players location.

    :return: The temperature at the player's location
    :rtype: Float

.. js:function:: weather.isFrosty()

    Evaluates if it is cold enough for frost.

    :return: Returns ``true`` if the current temperature is low enough for breath effects, ``false`` otherwise.
    :rtype: Boolean

.. js:function:: weather.canWaterFreeze()

    Evaluates if water can freeze at the player's location.

    :return: Returns ``true`` if the temperature is low enough for water to freeze, ``false`` otherwise.
    :rtype: Boolean

.. js:function:: weather.getWindSpeed()

    Returns the speed of the simulated wind, as a percent of a full storm's wind. Values above 100 are possible, since thunderstorms and dust storms blow harder. Gusts are not included,
    so the value does not change rapidly. (*Added 1.21.1-0.4.7*)

    :return: The steady wind speed as a percent of a full storm's wind
    :rtype: Float

.. js:function:: weather.isWindy()

    Evaluates if the wind is blowing at 50% or more of a full storm's wind. (*Added 1.21.1-0.4.7*)

    :return: Returns ``true`` if it is windy, ``false`` otherwise.
    :rtype: Boolean

.. js:function:: weather.isStormWind()

    Evaluates if the wind is blowing as hard as a storm's. Becomes ``true`` when the wind reaches 70% of a full storm's wind, and does not become ``false`` again until it drops below 55%, so that
    sounds switched by it do not start and stop as the wind wavers. (*Added 1.21.1-0.4.7*)

    :return: Returns ``true`` if the wind is storm strength, ``false`` otherwise.
    :rtype: Boolean

.. js:function:: weather.isGusting()

    Evaluates if the wind is currently gusting. Gusts come and go within seconds. (*Added 1.21.1-0.4.7*)

    :return: Returns ``true`` if the wind is gusting, ``false`` otherwise.
    :rtype: Boolean
