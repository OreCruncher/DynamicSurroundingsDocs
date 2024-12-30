.. role:: sectiontitle
.. role:: underlined

Commands
========

:sectiontitle:`/dsmm \<command>`

Alters the behavior of the Music Manager.

.. list-table:: Music Manager Subcommands
    :widths: auto
    :align: center
    :header-rows: 1

    *   - Command
        - Version Added
        - Comment
    *   - reset
        -
        - Resets the Minecraft Music manager. Causes the current music to terminate, and changes the internal timers so that another music selection will be made in the very near future.
    *   - pause
        - 0.4.1
        - Pauses the music manager, stopping any current music and will block further playing until it is unpaused or reset.
    *   - unpause
        - 0.4.1
        - Allows the music manager to play music.

:sectiontitle:`/dsreload`

Causes Dynamic Surroundings to clear internal caches and rescan registries, mod assets, resource packs, and disk configuration locations. Useful when developing resource packs where changes are made and
need to be hot loaded without exiting the Minecraft client. Can also be used if a desync is suspected.

:sectiontitle:`/dsscript \<script>`

Executes an arbitrary JavaScript entry and displays the result. For example, ``/dsscript Math.sqrt(9) * 6`` should respond with ``18``. Useful for performing calculations on the side as well as testing.

:sectiontitle:`/dsbiome \<biome ID> \<script>`

Executes an arbitrary JavaScript entry using the specified biome configured in the JavaScript execution environment. Useful for testing biome selector script fragments. For example, ``/dsbiome minecraft:plains OVERWORLD && PLAINS``
should return ``true``.

:sectiontitle:`/dsdump \<subcommand>`

Dumps out cached information to the ``minecraftinstance/config/dsurround/dumps`` folder. Useful when creating a resource pack and the final cached result needs to be analyzed.

.. list-table:: Dump Subcommands
    :widths: auto
    :align: center
    :header-rows: 1

    *   - Subcommand
        - Comment
    *   - biomes
        - Lists all biomes and associated configuration information.
    *   - sounds
        - A list of all sound events known by Dynamic Surroundings, both registered in the sound event registry as well as defined with mods and resource packs.
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
    *   - diregistrations
        - Dumps all component registrations in the dependency container; only makes sense to me. :)
