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
        "factory": "player.heartbeat",
        "conditions": "!player.isCreative() && global.allowScary() && player.getHealth() <= player.getMaxHealth() * 0.3"
    }

With no ``type`` this is a loop: the heartbeat plays for as long as the conditions are true, here while the player is not in creative mode, scary content is allowed
(``global.allowScary()``, the :confval:`scaryContent.allowScaryContent` option), and their health is at 30% of its maximum or less. It fades out when the
player heals.

.. code-block:: JSON

    {
        "biomeSelector": "biome.getRainfall() < 0.1 && (DESERT || (WASTELAND && !(COLD || SNOWY || SWAMP)))",
        "_comment": "Dust for desert like biomes",
        "fogColor": "#FFEA97"
    }

This biome configuration rule sets the fog color of a biome if the average rainfall is < 0.1, and is a DESERT or WASTELAND but not COLD, SNOWY, or SWAMP.

.. code-block:: JSON

    {
        "biomeSelector": "lib.oneof(biome.getId(), 'minecraft:frozen_ocean', 'minecraft:deep_frozen_ocean')",
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

This rule is for an :term:`acoustic <Acoustic>` applied to any biome. In this case, "wolf" is considered a scary sound. The sound can play if it is not raining, and is nighttime, and scary sounds are not disabled.

.. code-block:: JSON

    {
        "blocks": [
            "#dsurround:effects/frog_croaks"
        ],
        "soundChance": "diurnal.isNight() ? 0.04 : 0.02",
        "acoustics": [
            {
                "factory": "dsurround:lilypad.frog",
                "conditions": "!state.isInside() && !weather.canWaterFreeze()",
                "weight": 30
            },
            {
                "factory": "dsurround:lilypad.bullfrog",
                "conditions": "!state.isInside() && !weather.canWaterFreeze()",
                "weight": 10
            }
        ]
    }

This :doc:`block configuration rule <../schemas/blocks>` makes lily pads, and any other block tagged ``dsurround:effects/frog_croaks``, croak. The ``soundChance`` script
uses the conditional operator to pick a chance: 0.04 at night and 0.02 during the day, so frogs are heard twice as often after dark. Each acoustic plays only when the player is not inside and it is not cold enough for water to freeze. When a sound plays, the weights pick which: a frog croak
three times as often as a bullfrog call. (*Added 1.21.1-0.4.8*)
