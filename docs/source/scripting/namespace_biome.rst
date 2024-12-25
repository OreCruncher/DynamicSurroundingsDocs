*biome* Namespace
=================

These functions apply to biomes, and can be used in two different contexts:

* In game, these functions can be used to query information about the biome where the player is currently located.
* During configuration, these functions can be used in a biome condition filter to determine if a rule applies to a given biome.

For a list of possible biome traits refer to :doc:`biometraits`.

.. js:function:: String biome.getName()

    Returns the localized name of the biome.

    :return: The name of the biome
    :rtype: String

.. js:function:: String biome.getModId()

    Returns the mod ID that the biome is associated with.

    :return: The biomes mod ID
    :rtype: String

.. js:function:: String biome.getId()

    Returns the resource location ID of the biome.

    :return: The biome's resource location ID
    :rtype: String

.. js:function:: Float biome.getRainfall()

    Returns the average rainfall of the biome.

    :return: Biome's average rainfall
    :rtype: Float

.. js:function:: Float biome.getTemperature()

    Returns the average temperature of the biome.

    :return: Biome's average temperature
    :rtype: Float

.. js:function:: String biome.getPrecipitationType()

    Returns the precipitation that occurs within the biome.

    :return: The type of precipitation the biome usually has
    :rtype: String

.. js:function:: String biome.getTraits()

    Gets the list of biome trats, as a string.

    :return: Traits of the biome in a comma separated string
    :rtype: String

.. js:function:: Boolean biome.is(String trait)

    Checks to see if the biome has the specified trait.

    :param trait: The trait to check for
    :type trait: String
    :return: Returns ``true`` if the biome has the specified trait, ``false`` otherwise.
    :rtype: Boolean

.. js:function:: Boolean biome.isAllOf(String... traits)

    Checks to see if the biome has all the specified traits.

    :param traits: Array of traits to check for
    :type traits: String[]
    :return: Returns ``true`` if the biome has all the specified traits, ``false`` otherwise.
    :rtype: Boolean

.. js:function:: Boolean biome.isOneOf(String... traits)

    Checks to see if the biome has at least one of the specified traits.

    :param traits: Array of traits to check for
    :type traits: String[]
    :return: Returns ``true`` if the biome has one of the specified traits, ``false`` otherwise.
    :rtype: Boolean
