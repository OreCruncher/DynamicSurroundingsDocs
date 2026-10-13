Sound Events and Sound Factories
================================

Dynamic Surroundings configuration refers to sounds in two ways: by sound event, and by sound factory.

Sound Events
------------

A sound event is the standard Minecraft way of identifying a sound, such as ``minecraft:entity.sheep.ambient`` or ``dsurround:biome.wind``. Sound events are defined in the ``sounds.json``
file of a mod or resource pack, which lists the ogg files that make up the sound. Dynamic Surroundings reads every ``sounds.json`` file it can find, including ones from resource packs, so a
sound event does not need to be registered with Minecraft to be used. See :doc:`../schemas/sounds`.

A sound event on its own only says *what* to play. How loud it is, its pitch, whether it repeats, and so on are left to whatever plays it.

Sound Factories
---------------

A sound factory wraps a sound event with the properties to use when Dynamic Surroundings plays it: volume, pitch (either of which can be a random range), sound category, whether it repeats,
and attenuation. Several factories can use the same sound event with different properties. Factories are defined in ``sound_factories.json``. See :doc:`../schemas/sound_factories`.

Which One to Use
----------------

Configuration that plays a sound, such as an :term:`acoustic <Acoustic>` (see :doc:`acoustic`) or a :term:`sound mapping <Sound Mapping>` rule (see :doc:`../schemas/sound_mappings`), takes a sound factory ID. If there is no factory with
that ID, the ID is treated as a sound event and played with default settings. Define a factory when the default settings are not suitable, for example to vary the pitch or lower the volume.

Configuration that changes how an existing sound is handled, such as ``soundconfig.json`` (see :doc:`../config/individual_sound_config`) or the sound being replaced in a sound mapping,
refers to the sound event.

IDs
---

In acoustics, ``sound_factories.json`` factory locations, and ``sound_mappings.json``, a sound or factory ID without a namespace is in the ``dsurround`` namespace (ex, ``rockfall`` is
``dsurround:rockfall``), and an ID prefixed with ``@`` is in the ``minecraft`` namespace (ex, ``@entity.sheep.ambient`` is ``minecraft:entity.sheep.ambient``). Elsewhere, such as
``soundconfig.json``, the standard Minecraft rule applies: an ID without a namespace is in the ``minecraft`` namespace. It is recommended to always specify the namespace.
