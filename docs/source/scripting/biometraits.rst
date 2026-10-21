Biome Traits
============

During configuration, Dynamic Surroundings will map Dynamic Surroundings biome tags to traits. Dynamic Surroundings biome tags are of the form "dsurround:is\_<trait name>" (example: "dsurround:is_forest").
The choice of tag name mirrors that of the conventional tags utilized by Fabric/Neoforge. For the purposes of scripting the engine simplifies tags to simple trait names (example: FOREST).

Definitions for Dynamic Surroundings biome tags can be found :source-dir:`in this folder <common/src/main/resources/assets/dsurround/dsconfigs/tags/worldgen/biome>`, and those for
other mods' biomes in each mod's folder (for example :source-dir:`Regions Unexplored's <common/src/main/resources/assets/regions_unexplored/dsconfigs/tags/worldgen/biome>`).

From a scripting perspective, these traits show up as boolean value with names matching the trait. Dynamic Surroundings will set the boolean state of these
traits every tick so that scripts will have up-to-date information.

The traits available for scripting are:

``AQUATIC``, ``AQUATIC_ICY``, ``BADLANDS``, ``BEACH``, ``BIRCH_FOREST``, ``CAVE``, ``COLD``, ``DARK_FOREST``, ``DEAD``, ``DEEP_OCEAN``, ``DENSE_VEGETATION``, ``DESERT``, ``DRY``, ``END``,
``FLORAL``, ``FLOWER_FOREST``, ``FOREST``, ``HILL``, ``HOT``, ``ICY``, ``JUNGLE``, ``LUSH``, ``MAGICAL``, ``MOUNTAIN``, ``MUSHROOM``, ``NETHER``, ``NETHER_FOREST``, ``OCEAN``, ``OLD_GROWTH``,
``OUTER_END_ISLAND``, ``OVERWORLD``, ``PLAINS``, ``PLATEAU``, ``RARE``, ``RIVER``, ``SANDY``, ``SAVANNA``, ``SHALLOW_OCEAN``, ``SNOWY``, ``SNOWY_PLAINS``, ``SPARSE_VEGETATION``, ``SPOOKY``,
``STONY_SHORES``, ``SWAMP``, ``TAIGA``, ``TEMPERATE``, ``UNDERGROUND``, ``VOID``, ``WASTELAND``

Where Traits Come From
----------------------

A biome's tags are the most trusted source of its traits, but many modded biomes are missing some, and a vanilla server only sends Minecraft's own tags. So
Dynamic Surroundings works out a biome's traits from several sources, most trusted first (*Added 1.21.1-0.4.7*):

.. list-table::
    :widths: auto
    :header-rows: 1

    *   - Source
        - Shown as
        - What it gives
    *   - Biome tags
        - ``tags``
        - The ``dsurround:is_<trait>`` tags, which include the conventional ``c:`` tags. See :doc:`../packs/tagging`.
    *   - Vanilla table
        - ``vanilla table``
        - For Minecraft's own biomes, Dynamic Surroundings' table settles the dimension, temperature, moisture, and vegetation, so a vanilla biome has the same
          traits on every server, even where Fabric's and NeoForge's tags disagree.
    *   - Biome definition
        - ``definition``
        - The biome's definition file in its mod's jar says how many trees it grows: many trees make dense vegetation and a forest, a few make sparse vegetation.
          This works on servers too, since a mod that adds biomes is installed on the client. Water biomes with many trees are dense, but not forests, and caves,
          oceans, and rivers don't count their trees at all.
    *   - Effects
        - ``effects``
        - The vanilla music, ambient sound, or grass the biome uses (a biome playing the desert's music is likely a desert). Only used for a biome nothing has
          given a kind yet, since mods choose music for its mood as much as its place.
    *   - Climate
        - ``climate``
        - The biome's temperature and downfall.
    *   - Name
        - ``name``
        - Words in the biome's name, matched whole: "taiga", "swamp", "bog", "fields", and so on.
    *   - Derived
        - ``derived``, ``derived from guesses``
        - What follows from other traits (snowy is cold, an ocean is aquatic).

Most traits belong to a group: the **dimension** (``OVERWORLD``, ``NETHER``, ``END``, ``VOID``), **temperature** (``COLD``, ``TEMPERATE``, ``HOT``),
**moisture** (``DRY``, ``WET``), **vegetation** (``SPARSE_VEGETATION``, ``DENSE_VEGETATION``), and **kind** (``FOREST``, ``DESERT``, ``SWAMP``, ``CAVE``,
``PLAINS``, and the other kinds of place). A source can only add a trait to a group that the sources before it left empty. For example, a biome tagged cold stays
cold, even if its temperature looks temperate. Traits outside the groups (``SNOWY``, ``SPOOKY``, ``LUSH``, ``RARE``, ...) can be added by any source.

The definition settles a biome's vegetation before the guesses, but it only makes the biome a forest after them. A biome with many trees that plays swamp music,
or is named a bog, is a swamp.

Checking a Biome's Traits
-------------------------

``/dsdump biomes`` writes every biome's traits to the ``dumps`` folder, with the source of each, for example
``FOREST, OVERWORLD (tags); DENSE_VEGETATION (definition); TEMPERATE (climate)``. It ends with **Biomes to check**: the biomes whose traits were guessed from
their music, grass, or name, or that have no dimension or kind at all. A tag file settles them. In single player, it also checks each biome's dimension against
the dimensions the world generates it in. A biome found only in modded dimensions is not listed for having no kind, since it is often its dimension's only biome.
See :doc:`../commands/commands`.

When you tag a biome's kind, also tag the other traits it should have: once a biome has a kind, its music and grass are no longer used, so the ``SPOOKY`` or
``LUSH`` they gave is lost.

.. seealso::

    :source:`BiomeTraits enum <common/src/main/java/org/orecruncher/dsurround/config/BiomeTrait.java>`