.. role:: underlined

Commands
========

/dsmm <command>
---------------

Alters the behavior of the Music Manager.

.. list-table:: Music Manager Subcommands
    :widths: auto
    :align: center
    :header-rows: 1

    *   - Command
        - Comment
    *   - reset
        - Resets the Minecraft Music manager. Causes the current music to terminate, and changes the internal timers so that another music selection will be made in the very near future.
    *   - pause
        - Pauses the music manager, stopping any current music and will block further playing until it is unpaused or reset. (*Added 1.21.1-0.4.1*)
    *   - unpause
        - Allows the music manager to play music. (*Added 1.21.1-0.4.1*)
    *   - whatsplaying
        - Reports which sound is being played by the Music Manager. (*Added 1.21.1-0.4.2*)

/dsreload
---------

Causes Dynamic Surroundings to clear internal caches and rescan registries, mod assets, resource packs, and disk configuration locations. Useful when developing resource packs where changes are made and
need to be hot loaded without exiting the Minecraft client. Can also be used if a desync is suspected.

/dsscript <script>
------------------

Executes an arbitrary script and displays the result. For example, ``/dsscript Math.sqrt(9) * 6`` should respond with ``18.0``. Useful for performing calculations on the side as well as testing.

/dsbiome <biome ID> <script>
----------------------------

Executes an arbitrary script entry using the specified biome configured in the execution environment. Useful for testing :term:`biome selector <Biome Selector>` script fragments. For example, ``/dsbiome minecraft:plains OVERWORLD && PLAINS``
should return ``true``.

/dsweather <subcommand>
-----------------------

Shows and overrides the simulated storm strength, wind, ground fog, and window frost. Intended for testing and for seeing how weather of a given strength looks; it only changes
what the client sees and hears, and does not affect game mechanics. Overrides stay in place until cleared or the player disconnects. Running ``/dsweather`` with no
subcommand reports the current storm: its strength band, its strength as a percent of full strength, and the game's own rain level. (*Added 1.21.1-0.4.7*)

.. list-table:: Weather Subcommands
    :widths: auto
    :align: center
    :header-rows: 1

    *   - Subcommand
        - Comment
    *   - strength \<0-100>
        - Holds storms at the given percent of full strength. If it is not raining, the strength takes effect once it rains (for example, after ``/weather rain``).
    *   - clear
        - Removes the storm strength override so storms are simulated again.
    *   - wind
        - Reports the wind's speed, as a percent of a full storm's wind, and the direction it is blowing toward.
    *   - wind speed \<0-300>
        - Holds the wind at the given percent of a full storm's wind. Values over 100 match the stronger winds of thunderstorms and dust storms.
    *   - wind direction \<0-359 | compass point>
        - Holds the direction the wind blows toward, given as degrees clockwise from north or as one of the compass points ``N``, ``NE``, ``E``, ``SE``, ``S``, ``SW``, ``W``, ``NW``.
    *   - wind clear
        - Removes the wind speed and direction overrides so the wind is simulated again.
    *   - groundfog
        - Reports whether ground fog thickness is overridden or comes from the biomes.
    *   - groundfog \<0-100>
        - Sets ground fog to the given thickness everywhere, as a percent of the thickest.
    *   - groundfog clear
        - Removes the ground fog override so each biome's own ground fog is used again.
    *   - frost
        - Reports whether window frost is overridden or follows the weather.
    *   - frost \<0-100>
        - Gives every window the given amount of frost, as a percent of the most, at once and whatever the weather or temperature.
    *   - frost clear
        - Removes the frost override so window frost follows the weather again; it then grows or melts toward what the weather calls for.

/dsconflicts
------------

Lists in chat the Dynamic Surroundings features that are turned off in this session because another mod is installed, and which mod each one stands aside for;
for example, particle rain and snow when Particle Rain is installed. If nothing is turned off, it says so. The same list is written to the log at startup and shown
in the diagnostic overlay. See :ref:`mods-that-replace-a-feature` for the mods involved. (*Added 1.21.1-0.4.7*)

/dsprofile [scene] [seconds]
----------------------------

Records a performance profile of the game with Java Flight Recorder, to attach to an issue when something seems slow. With no scene, it records two minutes of the
game as it is; a scene shows one effect at its heaviest while it records, and the number of seconds (10 to 600) sets the length. The recording is saved zipped in
``config/dsurround/profiles``, without personal information. See :doc:`../troubleshooting/jfr` for how to use it, the scenes, and what is in a recording.
(*Added 1.21.1-0.4.7*)

.. list-table:: Profile Scenes
    :widths: auto
    :align: center
    :header-rows: 1

    *   - Scene
        - Comment
    *   - general
        - The game as it is; nothing is changed. The default.
    *   - ground_fog
        - Ground fog at its thickest, everywhere. In single player it also clears the weather.
    *   - weather
        - A thunderstorm at full strength. In single player it also starts the thunderstorm.
    *   - frost
        - The most frost on every window.

/dsdump <subcommand>
--------------------

Dumps out cached information to the ``minecraftinstance/config/dsurround/dumps`` folder. Useful when creating a resource pack and the final cached result needs to be analyzed.

.. list-table:: Dump Subcommands
    :widths: auto
    :align: center
    :header-rows: 1

    *   - Subcommand
        - Comment
    *   - biomes
        - Lists all biomes and associated configuration information, with where each biome trait came from, and ends with the biomes whose traits were guessed, to
          check (*added 1.21.1-0.4.7*). See :doc:`../scripting/biometraits`.
    *   - sounds
        - A list of all :term:`sound events <Sound Event>` known by Dynamic Surroundings, both registered in the sound event registry as well as defined with mods and resource packs.
    *   - dimensions
        - All cached dimension information defined for Dynamic Surroundings.
    *   - blocks
        - List of all blocks, tags, and blockstates. ``nostates`` can be specified to not emit blockstate information.
    *   - blocksbytag
        - List all blocks, organized by tag.
    *   - blockconfigrules
        - Lists cached block config rules.
    *   - blockstates
        - Dumps all possible block states.
    *   - items
        - A dump of the item registry and the tags associated with each item.
    *   - tags
        - Lists all Dynamic Surroundings tags along with their members.
    *   - entities
        - Lists the entity types and the Dynamic Surroundings effects (frost breath, item swing, and so on) each one gets.
    *   - diregistrations
        - Dumps all component registrations in the dependency container; only makes sense to me. :)

/dsversion
----------

Checks whether a newer version of Dynamic Surroundings is available and reports the result in chat, with links to the download and other information. The
check runs in the background, so the result arrives a moment after the command. This works even if the version check when joining a world has been turned off with
:confval:`logging.enableModUpdateChatMessage`. (*Added 1.21.1-0.4.6*)
