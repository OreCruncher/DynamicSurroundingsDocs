Biome Traits
============

During configuration, Dynamic Surroundings will map Dynamic Surroundings biome tags to traits. Dynamic Surroundings biome tags are of the form "dsurround:is\_<trait name>" (example: "dsurround:is_forest").
The choice of tag name mirrors that of the conventional tags utilized by Fabric/Neoforge. For the purposes of scripting the engine simplifies tags to simple trait names (example: FOREST).

Definitions for Dynamic Surroundings biome tags can be found :source-dir:`in this folder <common/src/main/resources/assets/dsurround/dsconfigs/tags/worldgen/biome>`.

From a scripting perspective, these traits show up as boolean value with names matching the trait. Dynamic Surroundings will set the boolean state of these
traits every tick so that scripts will have up-to-date information.

The traits available for scripting are:

``AQUATIC``, ``AQUATIC_ICY``, ``BADLANDS``, ``BEACH``, ``BIRCH_FOREST``, ``CAVE``, ``COLD``, ``DARK_FOREST``, ``DEAD``, ``DEEP_OCEAN``, ``DENSE_VEGETATION``, ``DESERT``, ``DRY``, ``END``,
``FLORAL``, ``FLOWER_FOREST``, ``FOREST``, ``HILL``, ``HOT``, ``ICY``, ``JUNGLE``, ``LUSH``, ``MAGICAL``, ``MOUNTAIN``, ``MUSHROOM``, ``NETHER``, ``NETHER_FOREST``, ``OCEAN``, ``OLD_GROWTH``,
``OUTER_END_ISLAND``, ``OVERWORLD``, ``PLAINS``, ``PLATEAU``, ``RARE``, ``RIVER``, ``SANDY``, ``SAVANNA``, ``SHALLOW_OCEAN``, ``SNOWY``, ``SNOWY_PLAINS``, ``SPARSE_VEGETATION``, ``SPOOKY``,
``STONY_SHORES``, ``SWAMP``, ``TAIGA``, ``TEMPERATE``, ``UNDERGROUND``, ``VOID``, ``WASTELAND``

.. seealso::

    :source:`BiomeTraits enum <common/src/main/java/org/orecruncher/dsurround/config/BiomeTrait.java>`