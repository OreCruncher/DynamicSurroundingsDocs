Biome Traits
============

During configuration, Dynamic Surroundings will map Dynamic Surroundings biome tags to traits. Dynamic Surroundings biome tags are of the form "dsurround:is\_<trait name>" (example: "dsurround:is_forest).
The choice of tag name mirrors that of the conventional tags utilized by Fabric/Neoforge. For the purposes of scripting the engine simplifies tags to simple trait names (example: FOREST).

Definitions for Dynamic Surroundings biome tags can be found `in this folder <https://github.com/OreCruncher/DynamicSurroundingsFabric/tree/main/common/src/main/resources/assets/dsurround/dsconfigs/tags/worldgen/biome>`_.

From a scripting perspective, these traits show up as boolean value with names matching the trait. Dynamic Surroundings will set the boolean state of these
traits every tick so that scripts will have up-to-date information.

.. seealso::

    `BiomeTraits enum <https://github.com/OreCruncher/DynamicSurroundingsFabric/tree/main/common/src/main/java/org/orecruncher/dsurround/config/BiomeTrait.java#L11>`_