.. role:: underlined
.. role:: sectiontitle

Resource Layout
===============

.. sidebar::

    .. image:: images/modlayout.png

    Mod

    .. image:: images/packlayout.png
        
    Resource Pack

    .. image:: images/disklayout.png

    On Disk

The layout of Dynamic Surroundings configuration files are similar between resource packs, mods, and disk configuration. All Dynamic Surroundings related configuration will be in a
folder named ``dsconfigs``. The ``tags`` folder is for configuring Dynamic Surroundings tags, and is entirely separate from Minecraft tags. See :doc:`tagging` for more
information.

``biomes.json``, ``blocks.json``, ``dimensions.json``, and ``sound_factories.json`` are placed in the ``dsconfigs`` folder. Though it's not specifically required, mod specific
enhancements should be placed into a folder specific to the mod. You can see this in the Mod image where ``biomesoplenty`` is concerned.

``sounds.json`` is placed placed in the regular location required by Minecraft.

For Resource packs I recommend adding a ``CREDITS.md`` file that contains any attribution and license information related to the sounds within. This ensure that attribution information
will be included within the resource pack distribution. If the resource pack is checked into GitHub or some other resource control system, the documentation will be immediately
available for viewing. Additionally, make sure to add the extended markup to ``sounds.json`` so that this information would be viewable ingame using the **Individual Sound Configuration** menu.
See :doc:`../schemas/sounds` for more information.

The on disk configuration layout is a bit different than resource pack or mod. Configuration files would be placed into the ``./minecraftinstance/config/dsurround/configs`` directory. Within
that folder, there will be subfolders using the name of a mod. In the image to the left, the mod in question is ``dsurround``. A given subfolder will only be processed if that mod is loaded.
(I use ``dsurround`` because it will always be loaded at runtime - go figure.) Within the mod folder there isn't a ``dsconfig`` folder - it is flattened. Configuration files go directly
into the mod folder.

Changes made to the on disk configuration do not immediately get applied. To pick up any changes "on the fly", execute the command ``/dsreload`` from within the game. This tells Dynamic Surroundings
to reinitialize it's caches based the current state of resource packs and on disk configurations. This behavior allows a player to make incremental changes to configurations and load them for
testing without exiting the client. Once a set of changes have been completed, they can be moved into a resource pack or mod and distributed. See :doc:`../commands/commands` for more information
on commands that are available.

:sectiontitle:`Example Resource Packs`

I have created two example resource packs. The can be found `here <https://github.com/OreCruncher/DynamicSurroundingsFabric/tree/main/packs>`_.

* :underlined:`Dynamic Surroundings - Seasons` - This pack provides ingame music based on the current season. The music scores are from `Vivaldi's Four Seasons <https://en.wikipedia.org/wiki/The_Four_Seasons_(Vivaldi)>`_. To get the most out of the pack, install Serene Seasons.
* :underlined:`Dynamic Surroundings Extended` - This pack provides ingame music of a variety of different types. This music is conditional based on biome, time of day, etc.

For more information on how Dynamic Surroundings does music, refer to the :doc:`../misc/music` documentation.