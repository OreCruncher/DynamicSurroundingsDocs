*biome* Namespace
=================

These functions apply to biomes, and can be used in two different contexts:

* In game, these functions can be used to query information about the biome where the player is currently located.
* During configuration, these functions can be used in a biome condition filter to determine if a rule applies to a given biome.

For a list of possible biome traits refer to :doc:`biometraits`.

.. code-block:: javascript

    String getName()

Returns the localized name of the biome.

.. code-block:: javascript

    String getModId()

Returns the mod ID that the biome is associated with.

.. code-block:: javascript

    String getId()

Returns the resource location ID of the biome.

.. code-block:: javascript

    Float getRainfall()

Returns the average rainfall of the biome.

.. code-block:: javascript

    Float getTemperature()

Returns the average temperature of the biome.

.. code-block:: javascript

    String getPrecipitationType()

Returns the precipitation that occurs within the biome.

.. code-block:: javascript

    String getTraits()

Gets the list of biome trats, as a string.

.. code-block:: javascript

    Boolean is(String trait)

Returns ``true`` if the biome has the specified trait, ``false`` otherwise.

.. code-block:: javascript

    Boolean isAllOf(String... trait)

Returns ``true`` if the biome has all the specified traits, ``false`` otherwise.

.. code-block:: javascript

    Boolean isOneOf(String... trait)

Returns ``true`` if the biome has one of the specified traits, ``false`` otherwise.
