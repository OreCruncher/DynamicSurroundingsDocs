.. role:: sectiontitle

Sound Mapping
=============

*Added 1.21.1-0.4.2*

`Source reference <https://github.com/OreCruncher/DynamicSurroundingsFabric/blob/main/common/src/main/resources/assets/dsurround/dsconfigs/sound_mappings.json>`_

Sound mapping is the process of converting one sound resource location into another during sound play, effectively replacing the sound. For example, replacing
Minecraft's thunder sound with the vesion from Dynamic Surroundings happens due to remap.

A lot of mods (and Minecraft as well) utilize the default block step sound ``minecraft:block.wood.step`` rather than using a custom sound. To account for this, 
a remap entry will have one or more rules associated. These entries can have 0 or more blockstate matchers, where an entry not having any matchers would be
considered the *default* rule.

When a sound is played, and if there is a remap entry for the resource location ID, Dynamic Surroundings will use the block position of the sound to obtain
a block state value. In most cases the sound being played is positioned just above the block. Logic will use the coordinates of the sound to generate the
block position below that location to get the block state. In some cases the location of the sound play is off the edge of a block, meaning the block below
the sound position is AIR. When this happens, Dynamic Surroundings will search adjacent blocks looking for a suitable surrogate.

This block state will be applied to all the rules, *in order*, for an entry until a match is determined. If there is a match, the sound associated with
that entry is selected for play. If there are no specific matches, the default rule be applied, if one is defined. If there isn't a default rule, the
mapping will not succeed and the original sound is permitted to play.

The schema for a sound mapping entry is as follows:

.. code-block:: JSON

    {
        "soundEvent": "<sound ID to remap>",
        "rules": [ ]
    }

.. list-table:: Sound Mapping Configuration
    :widths: auto
    :align: center
    :header-rows: 1

    *   - Property
        - Value Type
        - Comment
    *   - soundEvent
        - ResourceLocation
        - The sound event ID to be remapped. This is a required field.
    *   - rules
        - Sound Mapping Rule
        - A list of 1 or more rules to apply during mapping. This is a required field.

.. code-block:: JSON

    {
        "blocks": [],
        "factory": "<sound event ID or sound factory ID>"
    }

.. list-table:: Sound Mapping Rule
    :widths: auto
    :align: center
    :header-rows: 1

    *   - Property
        - Value Type
        - Comment
    *   - blocks
        - Array of block Specifications
        - Block specification to which the rule will apply. An entry with no specifications is considered the default rule. This property is optional. See :doc:`block_spec`.
    *   - factory
        - ResourceLocation
        - The sound resource ID or factory ID to play instead of the original

:sectiontitle:`Examples`

.. code-block:: JSON

    {
        "soundEvent": "minecraft:entity.lightning_bolt.thunder",
        "rules": [
            {
                "factory": "dsurround:thunder"
            }
        ]
    }

This is a simple rule that will outright replace ``minecraft:entity.lightning_bolt.thunder`` with ``dsurround:thunder``. This will happen because the rule is the default rule
and will be used if any other rule was not successfully applied.

.. code-block:: JSON

    {
        "soundEvent": "minecraft:block.stone.step",
        "rules": [
            {
                "blocks": [
                    "#minecraft:cauldrons"
                ],
                "factory": "dsurround:footsteps.metalbox"
            },
            {
                "factory": "dsurround:footsteps.stone"
            }
        ]
    }

This is a slightly more complicated example. In Vanilla, the block step sound for the cauldron is ``minecraft:block.stone.step``. What this mapping will do is map the sound to
``dsurround:footsteps.metalbox`` if the block state for the sound has the tag ``minecraft:cauldrons``. Otherwise, it will play the default sound ``dsurround:footsteps.stone``.

.. code-block:: JSON

    {
        "soundEvent": "minecraft:block.wood.step",
        "rules": [
            {
                "blocks": [
                    "#minecraft:logs",
                    "#c:logs"
                ],
                "factory": "dsurround:footsteps.log"
            },
            {
                "blocks": [
                    "#minecraft:fences",
                    "#c:fences"
                ],
                "factory": "dsurround:footsteps.bluntwood"
            },
            {
                "blocks": [
                    "#minecraft:beehives",
                    "minecraft:red_mushroom_block",
                    "minecraft:brown_mushroom_block",
                    "minecraft:mushroom_stem",
                    "minecraft:pumpkin",
                    "minecraft:carved_pumpkin",
                    "minecraft:melon",
                    "minecraft:cocoa"
                ],
                "factory": "dsurround:footsteps.organic"
            },
            {
                "factory": "dsurround:footsteps.wood"
            }
        ]
    }

The mapping rule for ``minecraft:block.wood.step`` has more definitions. The default step sound turns out to be that of stepping on wood. This mapping will tease apart the various block states
that have this default sound and map to a more appropriate one.