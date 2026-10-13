sound_mappings.json
===================

*Added 1.21.1-0.4.2*

:asset:`Source reference <dsconfigs/sound_mappings.json>`

Sound mapping is the process of converting one sound :term:`resource location <Resource Location>` into another during sound play, effectively replacing the sound. For example, replacing
Minecraft's thunder sound with the version from Dynamic Surroundings happens due to remap.

Remapping of thunder is controlled by the :confval:`soundOptions.replaceThunderSounds` setting, and all other remapping by the :confval:`soundOptions.remapSounds` setting. See
:doc:`../config/modconfiguration`. Sounds played with the **Play** button of the :doc:`../config/individual_sound_config` screen are never remapped.

A lot of mods (and Minecraft as well) utilize the default block step sound ``minecraft:block.wood.step`` rather than using a custom sound. To account for this, 
a remap entry will have one or more rules associated. These entries can have 0 or more blockstate matchers, where an entry not having any matchers would be
considered the *default* rule.

When a sound is played, and if there is a remap entry for the resource location ID, Dynamic Surroundings will use the block position of the sound to obtain
a block state value. In most cases the sound being played is positioned just above the block. Logic will use the coordinates of the sound to generate the
block position below that location to get the block state. In some cases the location of the sound play is off the edge of a block, meaning the block below
the sound position is not solid (such as AIR). When this happens, Dynamic Surroundings will check the four blocks to the north, south, east, and west of it, and use the
first solid one it finds as a surrogate. If an entry only has a default rule, no block state lookup is performed.

This block state will be applied to all the rules, *in order*, for an entry until a match is determined. If there is a match, the sound associated with
that entry is selected for play. If there are no specific matches, the default rule will be applied, if one is defined. If there isn't a default rule, the
mapping will not succeed and the original sound is permitted to play. The replacement sound plays at the same location and with the same volume as the original.

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
        - The :term:`sound event <Sound Event>` ID to be remapped. This is a required field.
    *   - rules
        - Sound Mapping Rule
        - A list of 1 or more rules to apply during mapping. This is a required field. At most one rule can be a default rule (a rule without ``blocks``), and it must be the last rule
          in the list. An entry that breaks these requirements is ignored and a warning is written to the log. (*Validation added 1.21.1-0.4.6*)

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
        - Array of :term:`block Specifications <Block Specification>`
        - Block specification to which the rule will apply. An entry with no specifications is considered the default rule. This property is optional. See :doc:`../concepts/block_spec`.
    *   - factory
        - ResourceLocation
        - The :term:`sound factory <Sound Factory>` ID or sound event ID to play instead of the original. If there is no sound factory with the ID, it is treated as a sound event ID and played with default
          settings. See :doc:`sound_factories`. This is a required field.

Combining Mappings
------------------

More than one mod or resource pack can provide a mapping for the same ``soundEvent``. When this happens the rules are combined rather than replaced:

* If an added rule has the same ``factory`` as an existing rule with blocks, the added rule's blocks are added to the existing rule.
* Otherwise the added rule is placed after the existing rules, but before the default rule, so the default remains last.
* An added default rule never replaces the existing default rule. When adding rules to an existing mapping, it is best not to include a default rule.

This means a resource pack can add block specific rules to one of Dynamic Surroundings' mappings without having to repeat it.

Examples
--------

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