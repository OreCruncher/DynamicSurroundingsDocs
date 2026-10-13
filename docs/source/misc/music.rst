Music
=====

In Vanilla, Minecraft makes its music selection based on biome. A mod or resource pack author would configure a property for background music. A player notices this
mostly in the Nether dimension where each biome has a different theme.

Dynamic Surroundings modifies the biome property, enabling the ability of choosing from multiple different selections. Further, these selections can have criteria that
evaluates whether a given piece of music can play. For example, a music selection can be configured to be eligible for play at specific times of day, certain biomes,
or any other criteria that can be made.

If there happens to be background music configured for a biome *natively*, that music is also added to the possible list of candidates.

Any music that is eligible for play are gathered into a weight table. A random selection is made from this table, and the result is what is provided to the music
manager for play. The selection is kept until it is time to start the next track, or the player moves to a different biome.

For more information on adding music in a resource pack, see :doc:`../concepts/acoustic`.

How Often Music Plays
---------------------

Minecraft does not play music continuously. When a track finishes, the music manager waits before starting the next one. The wait is a random number of ticks between the
*minimum delay* and *maximum delay* of the music that was selected (20 ticks is 1 second). If nothing is playing and the selected music changes to one with a shorter maximum
delay, such as when moving into a different biome, the wait is shortened to that maximum.

The delays come from the music's :term:`sound factory <Sound Factory>` (see :doc:`../schemas/sound_factories`):

.. list-table::
    :widths: auto
    :align: center
    :header-rows: 1

    *   - Property
        - Default
        - Comment
    *   - ``min_delay``
        - ``6000`` (5 minutes)
        - The shortest wait after this music finishes before the next track starts.
    *   - ``max_delay``
        - ``24000`` (20 minutes)
        - The longest wait after this music finishes before the next track starts.
    *   - ``replace_current_music``
        - ``false``
        - If ``true``, when this music is selected while a different track is playing, the current track is stopped, and this one starts after a wait of up to half its
          ``min_delay``, instead of waiting for the current track to finish.

Music that Minecraft provides for a biome natively uses Minecraft's own delays, which for most biomes are 10 - 20 minutes.

For example, a resource pack that wants its music to play more often could define its music factories with shorter delays:

.. code-block:: JSON

    {
        "location": "mypack:music.forest",
        "soundEvent": "mypack:music.forest",
        "category": "MUSIC",
        "attenuation": "NONE",
        "music": {
            "min_delay": 1200,
            "max_delay": 3600
        }
    }

With these settings there will be a pause of 1 to 3 minutes between tracks.

Configuration Settings
----------------------

These settings in the mod configuration affect music. See :doc:`../config/modconfiguration`.

.. list-table::
    :widths: auto
    :align: center
    :header-rows: 1

    *   - Setting
        - Comment
    *   - :confval:`musicManagerOptions.reduceWaitTime`
        - Shortens the wait between tracks by a percentage, for all music including Minecraft's own. Both the minimum and maximum delay are reduced, so at ``50`` a wait
          of 5 - 20 minutes becomes 2.5 - 10 minutes, and at ``100`` the next track starts almost immediately. Default is ``0`` (no reduction). This setting works whether or not
          the music manager is replaced.
    *   - :confval:`musicManagerOptions.replaceMusicManager`
        - Replaces Minecraft's music manager with the Dynamic Surroundings version. This is needed for the ``/dsmm`` commands. With Minecraft's music manager, Dynamic Surroundings
          music is still selected, but a new selection is made each time the music manager asks rather than being kept until the next track starts. Requires a restart.
          Default is ``true``.
    *   - :confval:`soundOptions.playBiomeMusicWhileCreative`
        - In creative mode Minecraft plays its creative music instead of biome music. Enabling this plays biome music, including Dynamic Surroundings music, as if the player
          were not in creative mode. Default is ``false``.
    *   - :confval:`soundOptions.displayToastMessagesForMusic`
        - Displays a toast with the title and author of a track when it starts, if a title and credits are defined for it in ``sounds.json`` (see :doc:`../schemas/sounds`). Requires the
          music manager to be replaced. Default is ``true``.

The volume of music is controlled by the *Music* slider in Minecraft's *Music & Sounds* options.

Commands
--------

The ``/dsmm`` commands control the music manager. They require ``replaceMusicManager`` to be enabled. See :doc:`../commands/commands`.

* ``/dsmm reset`` stops the current music and resets the timers so that another selection will be made in a few seconds. This is useful during pack development, and can also be used
  during game play to change the current music.
* ``/dsmm pause`` stops the current music and prevents more from playing until ``/dsmm unpause`` or ``/dsmm reset``.
* ``/dsmm whatsplaying`` reports the music that is playing, with its title and author if they are defined.
