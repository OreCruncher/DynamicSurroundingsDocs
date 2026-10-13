Glossary
========

.. glossary::
    :sorted:

    Acoustic
        A sound factory together with the conditions under which it can play, its weight, and its type (loop, mood, addition, or music). Biomes and blocks are
        given acoustics to make their sounds. See :doc:`acoustic`.

    Biome Selector
        A script in a ``biomes.json`` rule that decides which biomes the rule applies to. It evaluates to ``true`` for a biome the rule should apply to. See
        :doc:`../schemas/biomes`.

    Biome Trait
        A characteristic of a biome, such as ``FOREST`` or ``COLD``, that biome selector scripts can test. Traits come from Dynamic Surroundings biome tags. See
        :doc:`../scripting/biometraits`.

    Block Specification
        A string that matches blocks: a block ID (``minecraft:stone``), a block tag (``#minecraft:logs``), or a block with specific properties
        (``minecraft:nether_wart[age=3]``). See :doc:`block_spec`.

    Condition
        A script that decides whether something, such as an acoustic, is currently allowed to play or happen. It evaluates to ``true`` or ``false``.
        See :doc:`../scripting/scripting`.

    Resource Location
        An ID of the form ``namespace:path``, such as ``minecraft:entity.sheep.ambient``. Minecraft uses them to identify blocks, items, sounds, and other
        resources. Also called a resource ID.

    Sound Event
        Minecraft's way of identifying a sound, such as ``minecraft:entity.sheep.ambient``. Sound events are defined in ``sounds.json``. See :doc:`sounds`.

    Sound Factory
        A sound event together with the volume, pitch, category, and other settings Dynamic Surroundings uses to play it. Defined in ``sound_factories.json``.
        See :doc:`sounds` and :doc:`../schemas/sound_factories`.

    Sound Mapping
        A rule that replaces one sound with another when it is played, optionally depending on the block it is played on. See :doc:`../schemas/sound_mappings`.

    Tag
        A named group of blocks, items, fluids, entity types, or biomes. Dynamic Surroundings tags are client side tags in the ``dsurround`` namespace that control
        which content gets an effect. See :doc:`../packs/tagging`.
