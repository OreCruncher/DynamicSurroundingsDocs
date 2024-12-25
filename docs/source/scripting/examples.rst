Scripting Examples
==================

The following are some examples from the configuration used by Dynamic Surroundings.

.. code-block:: JSON

    {
        "factory": "player.tummy",
        "conditions": "player.getFoodLevel() <= 4 || player.hasEffect('minecraft:hunger')",
        "type": "addition"
    }

The conditions script checks to see if the current food level of the player is <= to 4, or if the player has the effect ``minecraft:hunger``. If true, the stomach rumble sound can play.

.. code-block:: JSON

    {
        "biomeSelector": "biome.getRainfall() < 0.1 && (DESERT || (WASTELAND && !(COLD || SNOWY || SWAMP)))",
        "_comment": "Dust for desert like biomes",
        "fogColor": "#FFEA97"
    }

This biome configuration rule sets the fog color of a biome if the average rainfall is < 0.1, and is a DESERT or WASTELAND but not COLD, SNOWY, or SWAMP.

.. code-block:: JSON

    {
        "biomeSelector": "lib.oneof(biome.id, 'minecraft:frozen_ocean', 'minecraft:deep_frozen_ocean')",
        "_comment": "Frozen Ocean/Deep Frozen Ocean explicit set",
        "fogColor": "#DCDBDF"
    }

This is similar to the previous example, but sets the fog color if the biome is either ``minecraft::frozen_ocean`` or ``minecraft:deep_frozen_ocean``.

.. code-block:: JSON

    {
        "factory": "wolf",
        "conditions": "weather.isNotRaining() && diurnal.isNight() && global.allowScary()",
        "type": "mood"
    }

This rule is for an acoustic applied to a biome. In this case, "wolf" is considered a scary sound. The sound can play if it is not raining, and is nighttime, and scary sounds are not disabled.