.. role:: underlined

Resource Layout
===============

.. sidebar::

    .. image:: images/modlayout.png

    Mod

    .. image:: images/packlayout.png
        
    Resource Pack

    .. image:: images/disklayout.png

    On Disk

The layout of Dynamic Surroundings configuration files is similar between resource packs, mods, and disk configuration. All Dynamic Surroundings related configuration will be in a
folder named ``dsconfigs``. The ``tags`` folder is for configuring Dynamic Surroundings tags, and is entirely separate from Minecraft tags. See :doc:`tagging` for more
information.

``biomes.json``, ``blocks.json``, ``dimensions.json``, ``sound_factories.json``, and ``sound_mappings.json`` are placed in the ``dsconfigs`` folder, which is in a namespace
folder under ``assets`` (``assets/<namespace>/dsconfigs``). Every namespace's ``dsconfigs`` folder is read, and the files from all of them are combined.

Though it's not specifically required, mod specific enhancements should be placed into a folder specific to the mod. You can see this in the Mod image where ``biomesoplenty``
is concerned. In a mod, a namespace folder is only read if a mod with that ID is installed, so configuration for a mod that is not present is skipped. Resource packs in the
player's resource packs folder are the exception: their folders are read whatever the namespace, so a pack can use a namespace of its own. The example resource packs
below do this with ``dsurround_seasons`` and ``dsurround_ex``.

``sounds.json`` is placed in the regular location required by Minecraft (``assets/<namespace>/sounds.json``).

For Resource packs I recommend adding a ``CREDITS.md`` file that contains any attribution and license information related to the sounds within. This ensures that attribution information
will be included within the resource pack distribution. If the resource pack is checked into GitHub or some other resource control system, the documentation will be immediately
available for viewing. Additionally, make sure to add the extended markup to ``sounds.json`` so that this information would be viewable in game using the **Individual Sound Configuration** menu.
See :doc:`../schemas/sounds` for more information.

The on disk configuration layout is a bit different than resource pack or mod. Configuration files would be placed into the ``./minecraftinstance/config/dsurround/configs`` directory. Within
that folder, there will be subfolders using the name of a mod. In the image to the left, the mod in question is ``dsurround``. A given subfolder will only be processed if that mod is loaded.
(I use ``dsurround`` because it will always be loaded at runtime - go figure.) Within the mod folder there isn't a ``dsconfigs`` folder - it is flattened. Configuration files, and the ``tags`` folder, go directly
into the mod folder.

On disk configuration is loaded after mods and resource packs. Where a later setting wins, such as a property set by more than one dimension rule, the on disk configuration
takes priority.

Changes made to the on disk configuration do not immediately get applied. To pick up any changes "on the fly", execute the command ``/dsreload`` from within the game. This tells Dynamic Surroundings
to reinitialize its caches based on the current state of resource packs and on disk configurations. This behavior allows a player to make incremental changes to configurations and load them for
testing without exiting the client. Once a set of changes have been completed, they can be moved into a resource pack or mod and distributed. See :doc:`../commands/commands` for more information
on commands that are available.

.. note::

    In the images, folders that contain only one folder are shown on one line, as the IDE displays them. For example, ``biomesoplenty.dsconfigs`` is the folder
    ``biomesoplenty`` containing the folder ``dsconfigs``, and ``entity_type.effects`` is ``entity_type/effects``.

Example Resource Packs
----------------------

I have created two example resource packs. They can be found :source-dir:`here <packs>`.

* :underlined:`Dynamic Surroundings - Seasons` - This pack provides in game music based on the current season. The music scores are from `Vivaldi's Four Seasons <https://en.wikipedia.org/wiki/The_Four_Seasons_(Vivaldi)>`_. To get the most out of the pack, install Serene Seasons.
* :underlined:`Dynamic Surroundings Extended` - This pack provides in game music of a variety of different types. This music is conditional based on biome, time of day, etc.

For more information on how Dynamic Surroundings does music, refer to the :doc:`../misc/music` documentation.