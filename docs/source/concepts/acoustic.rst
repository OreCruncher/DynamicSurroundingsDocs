.. role:: underlined

Acoustics
=========

An acoustic combines a :term:`sound factory <Sound Factory>` reference with other properties that determine when a sound is eligible for play. The acoustic
definition has the following schema:

.. code-block:: JSON

    {
        "factory": "sound factory ID",
        "conditions": "true",
        "weight": 10,
        "type": "loop"
    }

.. list-table:: Acoustic Configuration
    :widths: auto
    :align: center
    :header-rows: 1

    *   - Property
        - Value Type
        - Comment
    *   - factory
        - ResourceLocation
        - The :term:`resource location <Resource Location>` ID of the sound factory that will be used to create the sound instance. If there is no sound factory with the ID, it is treated as a :term:`sound event <Sound Event>` ID and
          played with default settings. An ID without a namespace is in the ``dsurround`` namespace (ex, ``rockfall`` is ``dsurround:rockfall``). See :doc:`sounds`. This is a required property.
    *   - conditions
        - String
        - Script that evaluates the conditions where the sound will be played. Default is ``true``. See :doc:`../scripting/scripting`.
    *   - weight
        - Integer
        - Relative weight of the entry as compared to its peers. It is used by the weight table selection process when determining a random sound. Default is ``10``.
    *   - type
        - String
        - The type of acoustic the entry represents. Possible values are ``loop``, ``mood``, ``music``, and ``addition``. Default is ``loop``.

.. list-table:: Acoustic types
    :widths: auto
    :align: center
    :header-rows: 1

    *   - Type
        - Comment
    *   - loop
        - The sound is non-attenuated and will play on a loop. It will terminate when the operating conditions are no longer met.
    *   - mood
        - The sound has a chance of periodically playing at a random location around the player. This random location gives directionality where the sound can be heard someplace around the player.
          The chance is set by the biome's ``moodSoundChance``.
    *   - music
        - The sound is configured to be utilized by Minecraft music manager. Whenever Minecraft plays a music track, a selection can be made from music related acoustics.
    *   - addition
        - The sound has a chance of randomly playing in a non-attenuated (non-directional) configuration. The chance is set by the biome's ``additionalSoundChance``.

The ``moodSoundChance`` and ``additionalSoundChance`` properties are described in :doc:`../schemas/biomes`.

It is worth noting that *any* sound factory can be used as an acoustic. Practically, though, the actual sound should be suitable for the acoustic type. For example, it would be strange to create a music acoustic
from ``minecraft:entity.zombie.ambient`` or a mood acoustic from ``minecraft:ui.button.click``.

Here is an example from the Dynamic Surroundings configuration:

.. code-block:: JSON

    "acoustics": [
      {
        "factory": "biome.underground",
        "conditions": "state.isInside()"
      },
      {
        "factory": "rockfall",
        "type": "mood",
        "weight": 30
      },
      {
        "factory": "bigrockfall",
        "type": "mood",
        "weight": 15
      },
      {
        "factory": "monstergrowl",
        "conditions": "diurnal.isNight() && global.allowScary()",
        "type": "mood",
        "weight": 10
      }
    ]

This configuration defines 4 acoustics for the underground biome effect. The first is of type ``loop`` since it uses the default. The other three are ``mood`` effects with different weights.  The conditions
of ``monstergrowl`` are different from the other two mood sounds.

During play, the first acoustic is played if the player is considered inside and of sufficient depth beneath the surface. Since it is of type ``loop`` it will continually play while the player is inside and
below the surface.

The other three are ``mood``, meaning they will randomly play somewhere around the player. Per tick, Dynamic Surroundings will determine if a ``mood`` acoustic should play.  If it does, it will make a selection
from one of the three entries.

Assuming it is night and scary sounds are enabled, the three entries have a combined weight of 55.  When making a random selection, because the weights are different, ``rockfall`` will play more frequently
than either ``bigrockfall`` or ``monstergrowl``. If it is day, only two entries will be eligible with a combined weight of 45.  ``rockfall`` will still play more frequently than ``bigrockfall``.

For music, here is an example from the ``Dynamic Surroundings - Seasons`` resource pack example:

.. code-block:: JSON

    {
        "biomeSelector": "OVERWORLD && (FOREST || PLAINS)",
        "_comment": "Music for Seasons",
        "acoustics": [
            {
                "factory": "dsurround_seasons:music/season/spring",
                "type": "music",
                "conditions": "season.isSpring()"
            },
            {
                "factory": "dsurround_seasons:music/season/summer",
                "type": "music",
                "conditions": "season.isSummer()"
            },
            {
                "factory": "dsurround_seasons:music/season/autumn",
                "type": "music",
                "conditions": "season.isAutumn()"
            },
            {
                "factory": "dsurround_seasons:music/season/winter",
                "type": "music",
                "conditions": "season.isWinter()"
            }
        ]
    }

This configuration adds music to overworld forest and plains biomes. There are 4 different acoustics, one for each season.