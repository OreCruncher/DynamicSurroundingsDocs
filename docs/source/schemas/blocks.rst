.. role:: sectiontitle

blocks.json
===========

`Source reference <https://github.com/OreCruncher/DynamicSurroundingsFabric/blob/main/common/src/main/resources/assets/dsurround/dsconfigs/blocks.json>`_

.. code-block:: JSON

    {
        "blocks": [
            "blockSpec"
        ],
        "clearSounds": false,
        "soundChance": "0.01",
        "acoustics": null,
        "effects": null
    }

.. list-table:: Block Configuration
    :widths: auto
    :align: center
    :header-rows: 1

    *   - Property
        - Value Type
        - Comment
    *   - blocks
        - String Array
        - The block states for which the configuration options apply. At least one entry is required. See `Block Specification`_ below.
    *   - clearSounds
        - Boolean
        - Clears existing sound configuration for the blocks. Default is ``false``.
    *   - soundChance
        - String
        - Script that provides the chance that a sound will be emitted. Default is ``0.01``.  See :doc:`../scripting/scripting`.
    *   - acoustics
        - Acoustic Array
        - An array of acoustics that can play. Default is ``null``. See :doc:`acoustic`.
    *   - effects
        - Effect Array
        - An array of effects that can generate. Default is ``null``. See `Effect Configuration`_ below.

.. code-block:: JSON

    {
        "effect": "effect",
        "conditions": "script",
        "spawnChance": null
    }

.. _Effect Configuration:

:sectiontitle:`Effect Configuration`

.. list-table:: Effect Configuration
    :widths: auto
    :align: center
    :header-rows: 1

    *   - Property
        - Value Type
        - Comment
    *   - effect
        - String
        - The type of effect. Possible values are ``FLAME_JET``, ``BUBBLE_COLUMN``, or ``FIRE_FLY``.
    *   - conditions
        - String
        - Script that determines if the effect is eligible for activation.  See :doc:`../scripting/scripting`.
    *   - spawnChance
        - String
        - Script that provides the spawn chance of the effect. Default is ``0.01``. See :doc:`../scripting/scripting`.

.. _Block Specification:

:sectiontitle:`Block Specification`

Target blocks can be specified in one of 3 different ways:

* Direct - Explicit using the resource location ID of the block (ex, ``minecraft:cobblestone``).
* Tag - Block tag (ex, ``#minecraft:wood``). The ``#`` prefix tells the config parser that it should be interpreted as a tag. The tag can be from any mod.
* BlockState match - Block plus additional block state values (ex, ``minecraft:nether_wart[age=3]``). The specification can do partial matches, meaning a subset of block state properies need to be specified.

:sectiontitle:`Examples`

.. code-block:: JSON

    {
        "blocks": [
            "#dsurround:effects/fireflies"
        ],
        "effects": [
            {
                "effect": "firefly",
                "conditions": "weather.isNotRaining() && (diurnal.isNight() || diurnal.isSunset()) && !(HOT || weather.canWaterFreeze())",
                "spawnChance": "0.035"
            }
        ]
    }

Firefly effect for any blocks that have the tag ``dsurround:effects/fireflies``.

.. code-block:: JSON

    {
        "blocks": [
            "minecraft:nether_wart[age=3]"
        ],
        "effects": [
            {
                "effect": "fire_jet",
                "spawnChance": "0.005"
            }
        ]
    }

Full grown Nether Wart spawning small flames on top.

.. code-block:: JSON

    {
        "blocks": [
            "minecraft:soul_sand"
        ],
        "soundChance": "0.000125",
        "acoustics": [
            {
                "factory": "dsurround:soulsand.laughter",
                "conditions": "dim.getId() == 'minecraft:the_nether'"
            }
        ]
    }

Randomly play laughter sound for a Soul Sand block when in the Nether dimension.