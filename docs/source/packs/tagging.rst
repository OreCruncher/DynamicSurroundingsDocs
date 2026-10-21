Tagging
=======

Many Dynamic Surroundings effects are driven by tags: which blocks squeak when walked on, which fluids form waterfalls, which items make a sword sound when
swung, and so on. Out of the box Dynamic Surroundings tags vanilla content, and content from some popular mods. A mod or resource pack author can add their own
blocks, fluids, entities, items, and particles to these tags so the effects work with their content as well.

Dynamic Surroundings tags are *client side* tags. They use the same Json format as Minecraft tags, but they are read by the client from mods and resource packs
rather than sent by the server, so they work when playing on a vanilla server. They are entirely separate from Minecraft tags, though they can refer to Minecraft
and conventional (``c:``) tags.

Where Tag Files Go
------------------

Every Dynamic Surroundings tag has an ID in the ``dsurround`` namespace, such as ``dsurround:effects/floor_squeaks``. The file for a tag is found by the type of thing
being tagged (``block``, ``fluid``, ``entity_type``, ``item``, ``particle_type``, or ``worldgen/biome``) and the path of the tag ID. For example, the block tag ``dsurround:effects/floor_squeaks``
is in the file ``tags/block/effects/floor_squeaks.json``.

That file can be placed in any of these locations, and all of them are used:

.. list-table::
    :widths: auto
    :align: center
    :header-rows: 1

    *   - Location
        - Path
        - Notes
    *   - Mod or resource pack
        - ``assets/<namespace>/dsconfigs/tags/block/effects/floor_squeaks.json``
        - The recommended location. ``<namespace>`` is normally your mod ID. The folder is only read if a mod with that ID is installed, so configuration for a mod that is
          not present is skipped. Resource packs in the player's resource packs folder are always read, whatever the namespace.
    *   - Mod data
        - ``data/dsurround/tags/block/effects/floor_squeaks.json``
        - The standard Minecraft location for a tag, inside a mod jar.
    *   - Disk
        - ``config/dsurround/configs/<mod ID>/tags/block/effects/floor_squeaks.json``
        - For players and pack makers testing changes. See :doc:`layout`.

Because every location is used, you do not need to repeat what Dynamic Surroundings already tags. List only your own content, and it is added to the tag.

The tag files Dynamic Surroundings ships can be found :source-dir:`here <common/src/main/resources/assets/dsurround/dsconfigs/tags>`, and are a good place to see what is
already tagged.

Tag File Format
---------------

A tag file has the same format as a Minecraft tag:

.. code-block:: JSON

    {
        "values": [
            "mymod:oak_planks_floor",
            "#mymod:creaky_floors",
            { "id": "#c:barrels/wooden", "required": false }
        ]
    }

* An entry is a block, fluid, entity type, item, or particle type ID.
* An entry starting with ``#`` includes every member of another tag. This can be a Minecraft tag, a conventional ``c:`` tag, another mod's tag, or another Dynamic Surroundings tag.
* ``{ "id": ..., "required": false }`` can be used for an entry that may not exist, such as a tag from another mod.
* Entries from all files for a tag are merged. ``"replace": true`` does not remove entries from other files.

Example
-------

A mod ``mymod`` that adds a creaky wooden floor block, a cattail plant, and a hot coals block could ship these files:

``assets/mymod/dsconfigs/tags/block/effects/floor_squeaks.json``

.. code-block:: JSON

    {
        "values": [ "mymod:creaky_floor" ]
    }

``assets/mymod/dsconfigs/tags/block/effects/straw_step.json``

.. code-block:: JSON

    {
        "values": [ "mymod:cattail" ]
    }

``assets/mymod/dsconfigs/tags/block/effects/heat_producers.json``

.. code-block:: JSON

    {
        "values": [ "mymod:hot_coals" ]
    }

The creaky floor will now squeak when walked on, walking through cattails makes a rustling sound, and water next to hot coals will steam.

Block Tags
----------

.. list-table::
    :widths: auto
    :align: center
    :header-rows: 1

    *   - Tag
        - Effect
    *   - ``dsurround:effects/floor_squeaks``
        - Blocks that occasionally squeak when walked on, such as wooden floors. Not when waterlogged.
    *   - ``dsurround:effects/brush_step``
        - Blocks that make a rustling sound when walked through, such as tall grass and flowers. The entity must be tagged ``dsurround:effects/brush_step``.
    *   - ``dsurround:effects/straw_step``
        - Like ``brush_step``, but with a drier, straw-like sound. Used for blocks such as sugar cane, dead bushes, and hay. Takes priority over ``brush_step``.
    *   - ``dsurround:effects/watery_step``
        - Blocks that make a splashing sound when walked on, such as lily pads. Waterlogged blocks already do this and do not need to be tagged.
    *   - ``dsurround:effects/heat_producers``
        - Blocks that are hot enough to produce steam from nearby water, such as lava and magma blocks.
    *   - ``dsurround:effects/steam_producers``
        - Blocks that give off steam when next to a hot block, such as water and water cauldrons. Steam only forms when the block above is air.
    *   - ``dsurround:effects/rain_absorbing``
        - Blocks that show damp spots where particle rain lands, such as dirt, sand, wool, and hay. (*Added 1.21.1-0.4.7*)
    *   - ``dsurround:effects/dust_sources``
        - Blocks that dust storms pick up dust from. The dust takes the color of the block. (*Added 1.21.1-0.4.7*)
    *   - ``dsurround:effects/windows``
        - Windows: blocks that particle rain runs down the sides of in streaks, such as glass blocks and panes. (*Added 1.21.1-0.4.7*)
    *   - ``dsurround:effects/frosted_windows``
        - Windows that frost on the outside in the cold: clear glass blocks and panes. Frost is drawn where the block's shape is, so a pane frosts in the
          middle of its block. Tinted and stained glass are left out for now. (*Added 1.21.1-0.4.7*)

Sound Occlusion and Reflectance
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

These tags control how blocks affect sound when enhanced sound processing is enabled. *Occlusion* is how much a block muffles a sound that passes through it (used when
occlusion processing is enabled). *Reflectance* is how much sound a block reflects, which affects reverb. Each has seven levels:

``none``, ``very_low``, ``low``, ``medium``, ``high``, ``very_high``, ``max``

The tags are ``dsurround:occlusion/<level>`` and ``dsurround:reflectance/<level>``, in the files ``tags/block/occlusion/<level>.json`` and ``tags/block/reflectance/<level>.json``.
A block that is not in any of these tags has its values estimated from the block's properties, so only blocks that are estimated poorly need to be tagged. For example,
a block made of a soft material that is estimated to reflect a lot of sound could be added to ``dsurround:reflectance/low``.

Fluid Tags
----------

.. list-table::
    :widths: auto
    :align: center
    :header-rows: 1

    *   - Tag
        - Effect
    *   - ``dsurround:effects/waterfall_sources``
        - Fluids that form waterfall effects (splash particles, mist, and foam) where they fall and land.
    *   - ``dsurround:effects/waterfall_sounds``
        - Fluids whose waterfalls make sound.
    *   - ``dsurround:effects/water_ripples``
        - Fluids that show ripples when rain lands on a source block.

Particle Type Tags
------------------

*Added 1.21.1-0.4.7*

.. list-table::
    :widths: auto
    :align: center
    :header-rows: 1

    *   - Tag
        - Effect
    *   - ``dsurround:effects/wind_blown``
        - Particles that drift with the simulated wind when made out in the open, such as smoke, ash, falling leaves, and spores. Includes several Minecraft
          particles and the leaves from Biomes O' Plenty trees. Particles that fly toward a target, such as those from portals and enchanting tables, should
          not be tagged: they set their own position and are not moved. Dynamic Surroundings' own particles handle the wind themselves and are never tagged.

Entity Type Tags
----------------

These tags control which entities get an effect.

.. list-table::
    :widths: auto
    :align: center
    :header-rows: 1

    *   - Tag
        - Effect
    *   - ``dsurround:effects/frost_breath``
        - The entity's breath is visible in cold biomes, and bubbles are given off underwater. Includes players, villagers, and raiders.
    *   - ``dsurround:effects/item_swing``
        - A sound is played when the entity swings the item it is holding, such as a sword or axe.
    *   - ``dsurround:effects/bow_pull``
        - A sound is played when the entity draws a bow.
    *   - ``dsurround:effects/brush_step``
        - The entity makes a sound when moving through blocks tagged ``brush_step`` or ``straw_step``.
    *   - ``dsurround:effects/toolbar``
        - A sound is played when the entity changes the item selected on the hotbar. Intended for players.

Item Tags
---------

The item tags tell Dynamic Surroundings what kind of item something is, which determines the sound played when it is selected on the hotbar or swung. An item should
only be in one of these tags; if it is in more than one, the first in the table below is used.

.. note::

    Before 1.21.1-0.4.3 these tags had plural names, such as ``dsurround:effects/axes``. The old names still work, but new configuration should use the names below.

.. list-table::
    :widths: auto
    :align: center
    :header-rows: 1

    *   - Tag
        - Items
    *   - ``dsurround:effects/is_axe``
        - Axes
    *   - ``dsurround:effects/is_book``
        - Books
    *   - ``dsurround:effects/is_bow``
        - Bows. Items in this tag also get the bow pull sound.
    *   - ``dsurround:effects/is_mace``
        - Maces
    *   - ``dsurround:effects/is_potion``
        - Potions
    *   - ``dsurround:effects/is_crossbow``
        - Crossbows
    *   - ``dsurround:effects/is_shield``
        - Shields
    *   - ``dsurround:effects/is_spear``
        - Spears
    *   - ``dsurround:effects/is_sword``
        - Swords
    *   - ``dsurround:effects/is_tool``
        - Other tools, such as hoes, shovels, and fishing rods

These item tags control the compass and clock overlays (see :doc:`../config/modconfiguration`):

.. list-table::
    :widths: auto
    :align: center
    :header-rows: 1

    *   - Tag
        - Effect
    *   - ``dsurround:effects/is_compass``
        - Holding the item displays the compass overlay.
    *   - ``dsurround:effects/compass_wobble``
        - The compass overlay spins in dimensions where compasses do not work, such as the Nether and End. See ``compassWobble`` in :doc:`../schemas/dimensions`.
    *   - ``dsurround:effects/is_clock``
        - Holding the item displays the clock overlay.
    *   - ``dsurround:effects/clock_wobble``
        - The clock overlay spins, and its text leaves out the time, in dimensions where compasses do not work, such as the Nether and End. See ``compassWobble`` in :doc:`../schemas/dimensions`.

These item tags select the sound played when a bucket is selected on the hotbar:

.. list-table::
    :widths: auto
    :align: center
    :header-rows: 1

    *   - Tag
        - Sound
    *   - ``dsurround:lava_buckets``
        - Lava bucket fill sound
    *   - ``dsurround:water_buckets``
        - Bucket fill sound
    *   - ``dsurround:entity_water_buckets``
        - Fish bucket fill sound (buckets holding a fish, axolotl, tadpole, and so on)
    *   - ``dsurround:milk_buckets``
        - Bucket fill sound

Note that the bucket tags do not have ``effects/`` in their ID, so their files are ``tags/item/lava_buckets.json`` and so on.

Biome Tags
----------

Biome tags give biomes the traits used by :term:`biome selector <Biome Selector>` scripts. The tags have the form ``dsurround:is_<trait>`` (ex, ``dsurround:is_forest``), in the files
``tags/worldgen/biome/is_<trait>.json``. Most modded biomes get their traits from conventional biome tags, and Dynamic Surroundings works out what is missing from the biome's
definition, music, climate, and name, so these only need to be added to for biomes it gets wrong. ``/dsdump biomes`` lists the biomes whose traits were guessed.
See :doc:`../scripting/biometraits`.

Put a mod's biomes in that mod's folder, as Dynamic Surroundings does for the biome mods it supports: for example ``assets/regions_unexplored/dsconfigs/tags/worldgen/biome/is_swamp.json``.
The folder is only read when the mod is installed, and its entries are added to those of the same tag in every other folder. The file name must be exactly the tag's
(``is_swamp.json``, not ``swamp.json``), or the file is never read.

.. code-block:: JSON

    {
        "replace": false,
        "values": [
            { "id": "regions_unexplored:bayou", "required": false },
            { "id": "regions_unexplored:fen", "required": false }
        ]
    }

A trait from a tag settles its group: a biome tagged ``is_swamp`` gets no other kind from a guess. Tags are the way to correct a wrong guess. Traits added by a
``biomes.json`` rule cannot, and are deprecated (see :doc:`../schemas/biomes`).

Checking Your Tags
------------------

* ``/dsdump tags`` writes every Dynamic Surroundings tag and its members to the ``dumps`` folder. See :doc:`../commands/commands`.
* ``/dsreload`` reloads tags along with the rest of the configuration, so changes to files on disk can be tested without restarting.
* The Dynamic Surroundings debug overlay lists the tags of the block being looked at.
