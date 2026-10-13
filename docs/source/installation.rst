Installation
============

Dynamic Surroundings can be downloaded from two different locations:

* `Dynamic Surroundings on CurseForge <https://www.curseforge.com/minecraft/mc-mods/dynamic-surroundings/files>`_
* `Dynamic Surroundings on Modrinth <https://modrinth.com/mod/dynamicsurroundingsfabric/versions>`_

Dynamic Surroundings is 100% client side. It only needs to be installed on the client, and it works when connected to a Vanilla server.

Required Dependencies
---------------------

Both Fabric and NeoForge versions have a dependency on the Architectury mod. That mod can be found:

* `Architectury on CurseForge <https://www.curseforge.com/minecraft/mc-mods/architectury-api>`_
* `Architectury on Modrinth <https://modrinth.com/mod/architectury-api>`_

Core
~~~~

* Java 21+
* Architectury 13.0.8+

Fabric
~~~~~~

* Loader 0.16.9+
* Fabric API 0.110.0+1.21.1+

NeoForge
~~~~~~~~

* NeoForge 21.1.84+

Optional Dependencies
---------------------

None of these mods are required. Dynamic Surroundings detects them when the game starts.

Recommended
~~~~~~~~~~~

.. list-table::
    :widths: auto
    :align: center
    :header-rows: 1

    *   - Mod
        - What it adds
    *   - `Cloth Config <https://modrinth.com/mod/cloth-config>`_ (15.0.140+)
        - The in-game configuration menu. Without it, settings can only be changed by editing ``dsurround.json``. See :doc:`config/modconfiguration`.
    *   - `Mod Menu <https://modrinth.com/mod/modmenu>`_ (Fabric only)
        - Fabric has no mod list of its own. Mod Menu adds one, from which the Dynamic Surroundings configuration menu can be opened. When Mod Menu is installed, the
          Dynamic Surroundings key for opening its configuration menu is left unbound by default.

Works With
~~~~~~~~~~

.. list-table::
    :widths: auto
    :align: center
    :header-rows: 1

    *   - Mod
        - What changes
    *   - `Serene Seasons <https://modrinth.com/mod/serene-seasons>`_
        - Seasons change the temperature, and so effects that depend on it, such as frost breath, whether it rains or snows, and some biome sounds. The current season
          is available to scripts in the ``season`` namespace. See :doc:`scripting/functions`.
    *   - `Presence Footsteps <https://modrinth.com/mod/presence-footsteps>`_
        - Presence Footsteps provides detailed footstep sounds of its own, so Dynamic Surroundings' footstep accents and rustling when walking through plants are turned
          off to avoid playing twice.

Mods That Replace a Feature
~~~~~~~~~~~~~~~~~~~~~~~~~~~

These mods provide their own version of something Dynamic Surroundings does. When one is installed, Dynamic Surroundings turns its own version off, whatever its settings.

.. list-table::
    :widths: auto
    :align: center
    :header-rows: 1

    *   - Mod
        - What Dynamic Surroundings turns off
    *   - `Particle Rain <https://modrinth.com/mod/particle-rain>`_
        - Particle rain and snow, dust storms, and water ripples.
    *   - `Simple Weather (NeoForge) <https://www.curseforge.com/minecraft/mc-mods/simple-weather>`_
        - Particle rain and snow, and dust storms. Water ripples are kept.
    *   - `Sound Physics Remastered <https://modrinth.com/mod/sound-physics-remastered>`_
        - Enhanced sound processing (reverb and occlusion).
    *   - `Raise Sound Limit Simplified <https://www.curseforge.com/minecraft/mc-mods/rsls>`_
        - Discarding sounds to stay under Minecraft's sound limit, since the limit is raised.

Shader Packs
~~~~~~~~~~~~

With `Iris <https://modrinth.com/mod/iris>`_ (or Oculus on NeoForge), Dynamic Surroundings works as usual until a shader pack is turned on. While a shader pack
is in use, the effects that draw with Dynamic Surroundings' own shaders are not shown, because the shader pack replaces the drawing they rely on: particle rain and
snow, dust storms, ground fog, auroras, and the light cast by fireflies and flame jets.

Quilt
~~~~~

Dynamic Surroundings runs on Quilt, but its client side commands are not registered there. See :doc:`commands/commands`.

Built-in Support for Other Mods
-------------------------------

Dynamic Surroundings includes configuration for the following mods, such as biome sounds and block effects for the content they add. It is only loaded when the mod
is installed.

* Biomes O' Plenty
* Nature's Spirit
* Profundis
* Promenade
* Serene Seasons
* Twilight Forest

Other mods can be supported by a resource pack, or by the mod itself; see :doc:`packs/layout`.
