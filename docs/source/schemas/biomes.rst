.. role:: underlined
.. role:: sectiontitle

biomes.json
===========

`Source reference <https://github.com/OreCruncher/DynamicSurroundingsFabric/blob/main/common/src/main/resources/assets/dsurround/dsconfigs/biomes.json>`_

This ``biomes.json`` file is where all the rules for biome effects are configured. The file is a Json array of zero or more configuration rules. Any number of rules can be created
based on what is needed.

The schema for a rule entry is as follows:

.. code-block:: JSON

    {
        "biomeSelector": "true",
        "_comment": null,
        "priority": 0,
        "traits": [ "array", "of", "biome", "traits" ],
        "clearSounds": false,
        "fogColor": null,
        "additionalSoundChance": null,
        "moodSoundChance": null,
        "acoustics": [ ]
    }

* :underlined:`biomeSelector` - JavaScript which returns ``true`` to apply a rule to a biome, or ``false`` to not apply. Default is 'true'.
* :underlined:`_comment` - Single line comment to describe purpose of the rule. Default is ``null``, meaning no comment.
* :underlined:`priority` - The priority at which the rule will be applied. Default is ``0``. Lower priority rules are applied before higher priority rules, meaning higher priority rules can alter what a lower priority rule configured.
* :underlined:`traits` - Any array of 0 or more traits that are to be added to a biome. During configuration, Dynamic Surroundings will apply traits to all biomes before applying the ``biomeSelector`` script. This option is used to configure modded biomes that did not use biome tags.
* :underlined:`clearSounds` - Clears any sound effects that have been configured by prior rules. Default is ``false``.
* :underlined:`fogColor` - Fog tint color, if any. Default is ``null`` meaning no setting. The format of the color string is RGB hex code (ex, "#FFD700" for gold).
* :underlined:`additionalSoundChance` - The chance that a sound of type ADDITION will play per tick. Default is '0.004'.
* :underlined:`moodSoundChance` - The chance that a sound of type MOOD will play per tick. Default is '0.004'.
* :underlined:`acoustics` - A Json array of acoustic definitions for the biome. Default is ``null``.

Additional details can be found in other pages:

.. toctree::
    :titlesonly:

    ../scripting/biometraits
    ../scripting/namespace_biome
    acoustic

As mentioned above, the chance related properties are actually scripts. These scripts have to evaluate to a double value in the range of 0.0 - 1.0. Each tick Dynamic Surroundings will generate a
random double value in the range of 0.0 - 1.0. If this value is less than or equal to the chance value, the effect will be applied.

Usually these scripts are simple constants (ex, "0.05"). However, since it is a script more complex logic can be applied to determine the chance value. For example, if you want to alter the
chance if a certain mod is loaded it could look something like:

.. code-block:: JSON

    "moodSoundChance": "lib.iif(lib.isModLoaded('theModId'), 0.01, 0.004)"

This script increases the chance that a mood sound will play if the mod ``theModId`` is loaded. You can also create more complicated chance calculations based on game state, such as the phase of the
moon or player health.

During configuration, Dynamic Surroundings will combine all the biome configuration rules across all mods and resource packs where the biome selector evaluates to ``true``. There isn't any
specific best practice on how to approach the creation of rules. However, having rules that combine a lot of configuration changes may become unweildy, especially dealing with
exception cases.

:sectiontitle:`Example Biome Selectors`

.. code-block:: JSON

    "biomeSelector": "!MOUNTAIN && (WASTELAND && !SWAMP && !COLD)",
    "biomeSelector": "FOREST && !(DEAD || WASTELAND || SWAMP || SPOOKY) && lib.isBetween(biome.temperature, 0.2, 1.0)",
    "biomeSelector": "lib.oneof(biome.id, 'minecraft:frozen_ocean', 'minecraft:deep_frozen_ocean')",
    "biomeSelector": "biome.id == 'minecraft:deep_frozen_ocean'"

Because these selectors are applied during configuration, the only function namespace available is ``biome``. Note that this only applies to biome selectors - chance
calculations and acoustic filtering can utilize in-game state function namespaces.

:sectiontitle:`Example Biome Rules`

.. code-block:: JSON

    {
        "biomeSelector": "MOUNTAIN",
        "_comment": "Wind for Mountain",
        "acoustics": [
            {
                "factory": "biome.wind.mountains"
            }
        ]
    }

This is a fairly simple rule. It applies a wind background sound to any biome that has the trait ``MOUNTAIN``.

.. code-block:: JSON

    {
        "biomeSelector": "biome.id == 'natures_spirit:chaparral'",
        "_comment": "Missing traits for Chaparral",
        "traits": [
            "OVERWORLD",
            "FOREST",
            "HOT"
        ]
    }

This rule adds traits to the ``natures_spirit:chaparral`` biome since this biome did not have any biome tags.

.. code-block:: JSON

    {
        "biomeSelector": "SWAMP && !FOREST",
        "_comment": "Basic Swamp Fog",
        "fogColor": "#406040"
    }

This rule sets the fog color for biomes that have the trait SWAMP and are not FORESTs. When entering into such a biome the color will tint towards green.

.. code-block:: JSON

    {
        "biomeSelector": "THE_END || biome.name == 'The Void'",
        "_comment": "It's The End!",
        "priority": 100,
        "clearSounds": true
    }

This rule clears any sounds that may have been assigned to The End biome or The Void. Since it is priority 100, it should be applied last.
