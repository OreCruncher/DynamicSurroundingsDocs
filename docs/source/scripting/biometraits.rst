Biome Traits
============

During configuration, Dynamic Surroundings will map the biome tags for the biome to traits. As Minecraft and modding evolves this mappings may change.
The tag to trait mapping can be found `here <https://github.com/OreCruncher/DynamicSurroundingsFabric/blob/0eed352bab5312cc605c0dbdf3296713e8fc3363/common/src/main/java/org/orecruncher/dsurround/config/biome/biometraits/BiomeTagAnalyzer.java#L20>`_.

The tags being mapped are Dynamic Surroundings biome tags. These tags have been configured with references for common tags ("c" tags), NeoForge tags, and Forge tags. Definitions for
these tags can be found `in this folder <https://github.com/OreCruncher/DynamicSurroundingsFabric/tree/main/common/src/main/resources/assets/dsurround/dsconfigs/tags/worldgen/biome>`_.

From a scripting perspective, these traits show up as boolean value with names matching the trait. Dynamic Surroundings will set the boolean state of these
traits every tick so that scripts will have up-to-date information.

.. seealso::

    `BiomeTraits enum <https://github.com/OreCruncher/DynamicSurroundingsFabric/blob/0eed352bab5312cc605c0dbdf3296713e8fc3363/common/src/main/java/org/orecruncher/dsurround/config/BiomeTrait.java#L11>`_