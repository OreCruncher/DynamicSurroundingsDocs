..	role:: underlined

Mod Configuration
=================

Configuration files for Dynamic Surroundings can be found in the modpack config folder with the name of ``dsurround``. Within this folder There
will be two Json files:

* ``soundconfig.json`` - configuration related to how sounds should be handled
* ``dsurround.json`` - contains the runtime configuration settings for the mod

It is recommended that settings be changed using the in-game menus. This will minimize the chances of typos in the config. If you need to modify directly, make sure Minecraft is not running to avoid the chance
of the Minecraft client overwriting any changes that have been made.

To be able to access the mod configuration menu, Cloth-Config needs to be installed with the modpack. This applies to Fabric as well as NeoForge. Additionally, Fabric does not provide
a mod listing feature out of the box. The mod ModMenu can be installed to provide this functionality.

soundconfig.json
----------------
This document is an array of Json entities with the form of:

.. code-block:: JSON

    [
        {
            "soundEventId": "namespace:path1",
            "startup": false,
            "volumeScale": 100,
            "block": false,
            "cull": false,
        },
        {
            "soundEventId": "namespace:path2",
            "startup": false,
            "volumeScale": 100,
            "block": false,
            "cull": false,
        }
    ]

By default a small handful of sounds can be found within the configuration file. These sounds are either marked for culling (such as animal sounds), or for volume control
(in the case of Wither and Ender Dragon). This file can be modified manually in a text editor, or can be updated using the **Individual Sound Configuration** menu from within
the game.

.. list-table:: soundconfig.json Properties
    :widths: auto
    :align: center
    :header-rows: 1

    *   - Property
        - Description
    *   - soundEventId
        - The resource location of the sound in question. For example, the sheep bleating sound effect has the ID of ``minecraft:entity.sheep.ambient``. This is a *required* field.
    *   - startup
        - Flag indicating whether the sound should be included in the startup sound selection list. Default is ``false``, and is not required.
    *   - volumeScale
        - Scaling factor to apply when playing a sound instance with that resource ID. Default is ``100``, and is not rquired. The value can be 0 - 400 where 0 mutes the sound entirely.
    *   - block
        - Flag indicating that the sound should be blocked from playing. Usually this is applied to sounds and effects that are considered annoying. Default is ``false`` and is not required.
    *   - cull
        - Flag indicating that the sound should be culled. Culling limits the number of sound plays for a given resource ID over a short period of time. For example, if you have a farm with a lot of animals, culling sounds will reduce the overall sound load on the Minecraft sound engine as well as your ears.  Default is ``false`` and is not required.

dsurround.json
--------------

This Json file is comprised of multiple sections, with related options grouped within. These settings can be changed in the mod configuration menu, assuming the appropriate mod support is available.

In each section below the value of a setting is the default.

logging
+++++++

.. code-block:: JSON

    {
        "logging": {
            "enableDebugLogging": false,
            "traceMask": 0,
            "enableModUpdateChatMessage": true,
            "filteredTagView": false,
            "registerCommands": true
        }
    }

.. list-table::
    :widths: auto
    :align: center
    :header-rows: 1

    *   - Property
        - Description
    *   - enableDebugLogging
        - Turns on detailed diagnostic trace from the mod.
    *   - traceMask
        - Set of bits that control which detail is desired.
    *   - enableModUpdateChatMessage
        - Enables display of version check results in the chat window when the player joins a world.
    *   - filteredTagView
        - Controls the amount of tag information to display within the mods diagnostics overlay.
    *   - registerCommands
        - Enables/disables registration of client side commands.

soundSystem
+++++++++++

.. code-block:: JSON

    {
        "soundSystem": {
            "streamingChannels": 12,
            "cullInterval": 20,
            "enableSoundPruning": true
        }
    }

.. list-table::
    :widths: auto
    :align: center
    :header-rows: 1

    *   - Property
        - Description
    *   - streamingChannels
        - The number of sound channels to reserve for streaming. Sounds that are typically streamed are music and background sound tracks for biomes. Streaming means that sound information is read from disk throughout the sound play, whereas non-streaming the sound information is read all at once before sending to the engine. Recommendation is not touch this setting unless there is a real need.
    *   - cullInterval
        - The number of ticks over which sounds are culled. The default of ``20`` means that a sound will be culled over a 1 second interval. Setting to 0 disables sound culling.
    *   - enableSoundPruning
        - Determines if Dynamic Surroundings will automatically prevent sounds from playing that are too far away for the player to hear. Intent is to reduce needless load in the Minecraft sound engine.

enhancedSounds
++++++++++++++

.. code-block:: JSON

    {
        "enhancedSounds": {
            "enableEnhancedSounds": true,
            "backgroundThreadWorkers": 0,
            "enableMonoConversion": true,
            "enableOcclusionProcessing": false,
            "reverbRays": 32,
            "reverbBounces": 4,
            "reverbRayTraceDistance": 256
        }    
    }

.. list-table::
    :widths: auto
    :align: center
    :header-rows: 1

    *   - Property
        - Description
    *   - enableEnhancedSounds
        - Enables/disables enhanced sound processing by Dynamic Surroundings. Enhanced sound processing is what provides reverb in caves.
    *   - backgroundThreadWorkers
        - This is the number of compute threads that run in the background to perform calculations for enhanced sounds. Recommendation is to not change this setting.
    *   - enableMonoConversion
        - For 3D spacial sounds to work they have to be encoded using mono format. Dynamic Surroundings will convert stereo sounds to mono on the fly to allow this to happen.
    *   - enableOcclusionProcessing
        - Occlusion processing is an advanced feature of the sound processing system. If enabled, Dynamic Surroundings will perform calculations to "muffle" a sound that is behind blocks from the perspective of the player. This processing will require additional horsepower so it is disabled by default.
    *   - reverbRays
        - As part of the calculation process of the enhanced sound engine, logic will cast a number of "rays" away from the player to get a sense of the space the player is located within. Increasing this value will improve fidelity at the expense of processing power. Recommendation is to leave at the default.
    *   - reverbBounces
        - When casting out a ray, if the ray intesects with the block surface it will be reflected at an angle, or bounced. This setting controls the number of bounces that are permitted before a given ray path trace is terminated. Increasing this value will improve fidelity at the expense of processing power. Recommendation is to leave at the default.
    *   - reverbRayTraceDistance
        - The maximum number of blocks a ray will be traced before termination. Note that this is not actual distance from the player, its the total distance travelled which includes bounces. Recommendation is to leave at the default.

soundOptions
++++++++++++

.. code-block:: JSON

    {
        "soundOptions": {
            "ambientVolumeScaling": 100,
            "replaceThunderSounds": true,
            "allowScarySounds": true,
            "playBiomeMusicWhileCreative": false,
            "displayToastMessagesForMusic": true
        }
    }

.. list-table::
    :widths: auto
    :align: center
    :header-rows: 1

    *   - Property
        - Description
    *   - ambientVolumeScaling
        - Scaling factor to apply to all ambient sounds that are played. This factor is on top of the sound slider scaling of Minecraft. This value can be 0 - 400.
    *   - replaceThunderSound
        - Flag indicating whether to replace Minecraft's thunder sounds with the ones from Dynamic Surroundings.
    *   - allowScarySounds
        - Flag indicating whether scary sounds should be enabled within the mod. Some of the sounds I have added to the mod are considered scary to younger audiences. This will allow a parent to control which sounds can be played.
    *   - playBiomeMusicWhileCreative
        - Normally when a player is in creative mode the music that is played is for the creative session. Enabling this feature will allow the regular biome music to play as if the player was not in creative mode.
    *   - displayToastMessagesForMusic
        - Controls whether a toast popout will be displayed when playing music that required atribution.

blockEffects
++++++++++++

.. code-block:: JSON

    {
        "blockEffects": {
            "blockEffectRange": 32,
            "steamColumnEnabled": true,
            "flameJetEnabled": true,
            "bubbleColumnEnabled": true,
            "firefliesEnabled": true,
            "waterfallsEnabled": true,
            "enableWaterfallSounds": true,
            "enableWaterfallParticles": true,
            "waterRippleStyle": "PIXELATED_CIRCLE"
        }
    }

.. list-table::
    :widths: auto
    :align: center
    :header-rows: 1

    *   - Property
        - Description
    *   - blockEffectRange
        - The range for which block effects will be determined. This range is a square around the player. This value can be 16 - 64 blocks. Increasing the distance will increase the load within the client tick. It is recommended that this value be left at the default.
    *   - steamColumnEnabled
        - Enables the steam effect for when water is close to a hot block (ie, something like lava or magma).
    *   - flameJetEnabled
        - Enables the flame jet effect from lava sources as well as lava cauldrons and max age nether wart.
    *   - bubbleColumnEnabled
        - Enables the bubble effect when under water.
    *   - firefliesEnabled
        - Enables the firefly effect around flowers at night.
    *   - waterfallsEnabled
        - Enables the waterfall effect feature. Sounds and particles can be individually controlled by the following settings.
    *   - enableWaterfallSounds
        - Enables generation of sounds for a water fall.
    *   - enableWaterfallParticles
        - Enables generation of waterfall splash particles.
    *   - waterRippleStyle
        - The style of water ripple for when rain hits a liquid surface. Currently ``PIXELATED_CIRCLE`` is the only option.

entityEffects
+++++++++++++

.. code-block:: JSON

    {
        "entityEffects": {
            "entityEffectRange": 24,
            "enableBowPull": true,
            "enableBreathEffect": true,
            "enablePlayerToolbarEffect": true,
            "enableSwingEffect": true,
            "enableBrushStepEffect": true
        }
    }

.. list-table::
    :widths: auto
    :align: center
    :header-rows: 1

    *   - Property
        - Description
    *   - entityEffectRange
        - The maximum distance from the player that entity effects will be applied. This value can be 16 - 64. Recomendation is to leave at the default setting.
    *   - enableBowPull
        - Enables the sound effects related to pulling back on a bow.
    *   - enableBreathEffect
        - Enables frost breath particle generation when in a cold biome.
    *   - enablePlayerToolbarEffect
        - Enables sound play when selecting between different items on the hotbar.
    *   - enableSwingEffect
        - Enables sound effects when swinging an item, such as swords and axes.
    *   - enableBrushStepEffect
        - Enables sound effect when moving through blocks that are considered brush, such as tall flowers and grass.

footstepAccents
+++++++++++++++

.. code-block:: JSON

    {
        "footstepAccents": {
            "enableAccents": true,
            "enableArmorAccents": true,
            "enableWetSurfaceAccents": true,
            "enableFloorSqueaks": true,
            "enableLeafAccents": true
        }
    }

.. list-table::
    :widths: auto
    :align: center
    :header-rows: 1

    *   - Property
        - Description
    *   - enableAccents
        - Enables the footstep aound effects when moving.
    *   - enableArmorAccents
        - Enables armor sounds when moving. The sounds that are played are based on what the player is wearing.
    *   - enableWetSurfaceAccents
        - Enables water splash sounds when walking on blocks such as lily pads. Also, a splash sound will play when walking out in the open during a rain storm.
    *   - enableFloorSqueaks
        - Enables playing floor squeeks when walking on wooden floors.
    *   - enableLeafAccents
        - Enables playing sound effects when walking on leaf blocks.

particleTweaks
++++++++++++++

.. code-block:: JSON

    {
        "particleTweaks": {
            "suppressProjectileParticleTrails": false
        }
    }

.. list-table::
    :widths: auto
    :align: center
    :header-rows: 1

    *   - Property
        - Description
    *   - suppressProjectileParticleTrails
        - Enables suppression of the particle trail generated by shooting an arrow.

compassAndClockOptions
++++++++++++++++++++++

.. code-block:: JSON

    {
        "compassAndClockOptions": {
            "enableClock": true,
            "enableCompass": true,
            "compassStyle": "TRANSPARENT_WITH_INDICATOR",
            "scale": 1.0
        }
    }

.. list-table::
    :widths: auto
    :align: center
    :header-rows: 1

    *   - Property
        - Description
    *   - enableClock
        - Enables the display of World Time and season information when holding a clock. Additionally, if an item frame is placed with clock as the framed item, looking at the framed clock will also display time and season information.
    *   - enableCompass
        - Enables the display of a compass HUD when holding a compass.
    *   - compassStyle
        - The style of compass to display. Possible selections are ``OPAQUE``, ``TRANSPARENT``, ``OPAQUE_WITH_INDICATOR``, and ``TRANSPARENT_WITH_INDICATOR``.
    *   - scale
        - The scaling factor to apply when rendering the compass HUD.

fogOptions
++++++++++

.. versionadded:: 0.4.1

.. code-block:: JSON

    {
        "fogOptions": {
            "enableFogEffects": true,
            "enableMorningFog": true,
            "enableBiomeFog": true,
            "enableWeatherFog": true
        }
    }

.. list-table::
    :widths: auto
    :align: center
    :header-rows: 1

    *   - Property
        - Description
    *   - enableFogEffects
        - Enable/disable fog effect processing
    *   - enableMorningFog
        - Enable/disable morning fog effect. Fog will start rolling in early in the AM, and eventually burn off later in the morning.
    *   - enableBiomeFog
        - Enable/disable biome fog effect. Some biomes will be configured as foggy, and when the player is in those biomes the density of fog will increase.
    *   - enableWeatherFog
        - Enable/disable generation of fog when raining/snowing.

otherOptions
++++++++++++

.. code-block:: JSON

    {
        "otherOptions": {
            "playRandomSoundOnStartup": true
        }
    }

.. list-table::
    :widths: auto
    :align: center
    :header-rows: 1

    *   - Property
        - Description
    *   - playRandomSoundOnStartup
        - Enables the play of a random sound when the Minecraft client starts.
