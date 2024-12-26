.. role:: underlined
.. role:: sectiontitle

Acoustic
========

An acoustic combines a sound factory reference with other properties that determine when a sound is eligble for play. The acoustic
definition has the following schema:

.. code-block:: JSON

    {
        "factory": "sound factory ID",
        "conditions": "true",
        "weight": 10,
        "type": "loop"
    }

* :underlined:`factory` - The resource location ID of the sound factory that will be used to create the sound instance. This is a required property.
* :underlined:`conditions` - Script that evaluates the conditions where the sound will be played. Default is ``true``.
* :underlined:`weight` - Relative weight of the entry as compared to it's peers. It is used by the weight table selection process when determining a random sound. Default is ``10``.
* :underlined:`type` - The type of acoustic the entry represents. Default is ``loop``.

The type of acoustic that can be defined are ``loop``, ``mood``, ``music``, and ``addition``. Each behaves differently within the game:

* :underlined:`loop` - The sound is non-attenuated and will play on a loop. It will terminate when the operating conditions are no longer met.
* :underlined:`mood` - The sound has a chance of periodically playing at a random location around the player. This random location gives directionality where the sound can be heard someplace around the player.
* :underlined:`music` - The sound is configured to be utilized by Minecraft music manager. Whenever Minecraft plays a music track, a selection can be made from music related acoustics.
* :underlined:`addition` - The sound has a chance of randomly playing in a non-attenuated (non-directional) configuration.

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
of ``monstergrowl`` is different from the other two loop sounds.

During play, the first acoustic is played if the player is considered inside and of sufficient depth beneath the surface. Since it is of type ``loop`` it will continually play while the player is insided and
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