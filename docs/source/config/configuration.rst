..	role:: underlined

Mod Configuration
=================

Configuration files for Dynamic Surroundings can be found in the modpack config folder with the name of ``dsurround``. Within this folder There
will be two Json files:

* ``soundconfig.json`` - configuration related to how sounds should be handled
* ``dsurround.json`` - contains the runtime configuration settings for the mod

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
(in the case of Wither and Ender Dragon). This file can be modified manually in a text editor, or can be updated using the Individual Sound Configuration menu from within
the game. Using the menu within the game is preferred as it reduces chance of errors. If you want to edit directly, do it when Minecraft is not running to avoid accidential
overwrite of your changes.

Entry properties:

* :underlined:`soundEventId` - The resource location of the sound in question. For example, the sheep bleating sound effect has the ID of ``minecraft:entity.sheep.ambient``. This is a *required* field.
* :underlined:`startup` - Flag indicating whether the sound should be included in the startup sound selection list. Default is ``false``, and is not required.
* :underlined:`volumeScale` - Scaling factor to apply when playing a sound instance with that resource ID. Default is ``100``, and is not rquired. The value can be 0 - 400 where 0 mutes the sound entirely.
* :underlined:`block` - Flag indicating that the sound should be blocked from playing. Usually this is applied to sounds and effects that are considered annoying. Default is ``false`` and is not required.
* :underlined:`cull` - Flag indicating that the sound should be culled. Culling limits the number of sound plays for a given resource ID over a short period of time. For example, if you have a farm with a lot of animals, culling sounds will reduce the overall sound load on the Minecraft sound engine as well as your ears.  Default is ``false`` and is not required.

dsurround.json
--------------

This Json file is comprised of multiple sections, with related options grouped within. It is recommended that settings be changed from within the game using the configuration dialogs.
If you want to modify directly, do it when Minecraft is not running to avoid accidential overwrite of your changes.

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

* :underlined:`enableDebugLogging` - Turns on details diagnostic trace from the mod.
* :underlined:`traceMask` - set of bits that control which detail is desired.
* :underlined:`enableModUpdateChatMessage` - Enables display of version check results in the chat window when the player logs in.
* :underlined:`filteredTagView` - Controls the amount of tag information to display within the mods diagnostics overlay.
* :underlined:`registerCommands` - Enables/disables registration of client side commands.

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

* :underlined:`streamingChannels` - The number of sound channels to reserve for streaming. Sounds that are typically streamed are music and background sound tracks for biomes. Streaming means that sound information is read from disk throughout the sound play, whereas non-streaming the sound information is read all at once before sending to the engine. Recommendation is not touch this setting unless there is a real need.
* :underlined:`cullInterval` - The number of ticks over which sounds are culled. The default of ``20`` means that a sound will be culled over a 1 second interval. Setting to 0 disables sound culling.
* :underlined:`enableSoundPruning` - Determines if Dynamic Surroundings will automatically prevent sounds from playing that are too far away for the player to hear. Intent is to reduce needless load in the Minecraft sound engine.

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

* :underlined:`enableEnhancedSounds` - Enables/disables enhanced sound processing by Dynamic Surroundings. Enhanced sound processing is what provides reverb in caves.
* :underlined:`backgroundThreadWorkers` - This is the number of compute threads that run in the background to perform calculations for enhanced sounds. Recommendation is to not change this setting.
* :underlined:`enableMonoConversion` - For 3D spacial sounds to work they have to be encoded using mono format. Dynamic Surroundings will convert stereo sounds to mono on the fly to allow this to happen.
* :underlined:`enableOcclusionProcessing` - Occlusion processing is an advanced feature of the sound processing system. If enabled, Dynamic Surroundings will perform calculations to "muffle" a sound that is behind blocks from the perspective of the player. This processing will require additional horsepower so it is disabled by default.
* :underlined:`reverbRays` - As part of the calculation process of the enhanced sound engine, logic will cast a number of "rays" away from the player to get a sense of the space the player is located within. Increasing this value will improve fidelity at the expense of processing power. Recommendation is to leave at the default.
* :underlined:`reverbBounces` - When casting out a ray, if the ray intesects with the block surface it will be reflected at an angle, or bounced. This setting controls the number of bounces that are permitted before a given ray path trace is terminated. Increasing this value will improve fidelity at the expense of processing power. Recommendation is to leave at the default.
* :underlined:`reverbRayTraceDistance` - The maximum number of blocks a ray will be traced before termination. Note that this is not actual distance from the player, its the total distance travelled which includes bounces. Recommendation is to leave at the default.

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

* :underlined:`ambientVolumeScaling` - Scaling factor to apply to all ambient sounds that are played. This factor is on top of the sound slider scaling of Minecraft. This value can be 0 - 400.
* :underlined:`replaceThunderSound` - Flag indicating whether to replace Minecraft's thunder sounds with the ones from Dynamic Surroundings.
* :underlined:`allowScarySounds` - Flag indicating whether scary sounds should be enabled within the mod. Some of the sounds I have added to the mod are considered scary to younger audiences. This will allow a parent to control which sounds can be played.
* :underlined:`playBiomeMusicWhileCreative` - Normally when a player is in creative mode the music that is played is for the creative session. Enabling this feature will allow the regular biome music to play as if the player was not in creative mode.
* :underlined:`displayToastMessagesForMusic` - Controls whether a toast popout will be displayed when playing music that required atribution. Currently not used by Dynamic Surroundings.

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

* :underlined:`blockEffectRange` - The range for which block effects will be determined. This range is a square around the player. This value can be 16 - 64 blocks. Increasing the distance will increase the load within the client tick. It is recommended that this value be left at the default.
* :underlined:`steamColumnEnabled` - Enables the steam effect for when water is close to a hot block (ie, something like lava or magma).
* :underlined:`flameJetEnabled` - Enables the flame jet effect from lava sources as well as lava cauldrons and max age netherwart.
* :underlined:`bubbleColumnEnabled` - Enables the bubble effect when under water.
* :underlined:`firefliesEnabled` - Enables the firefly effect around flowers at night.
* :underlined:`waterfallsEnabled` - Enables the waterfall effect feature. Sounds and particles can be individually controlled by the following settings.
* :underlined:`enableWaterfallSounds` - Enables generation of sounds for a water fall.
* :underlined:`enableWaterfallParticles` - Enables generation of waterfall splash particles.
* :underlined:`waterRippleStyle` - The style of water ripple for when rain hits a liquid surface. Currently ``PIXELATED_CIRCLE`` is the only option.

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

* :underlined:`entityEffectRange` - The maximum distance from the player that entity effects will be applied. This value can be 16 - 64. Recomendation is to leave at the default setting.
* :underlined:`enableBowPull` - Enables the sound effects related to pulling back on a bow.
* :underlined:`enableBreathEffect` - Enables frost breath particle generation when in a cold biome.
* :underlined:`enablePlayerToolbarEffect` - Enables sound play when selecting between different items on the hotbar.
* :underlined:`enableSwingEffect` - Enables sound effects when swinging an item, such as swords and axes.
* :underlined:`enableBrushStepEffect` - Enables sound effect when moving through blocks that are considered brush, such as tall flowers and grass.

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

* :underlined:`enableAccents` - Enables the footstep aound effects when moving.
* :underlined:`enableArmorAccents` - Enables armor sounds when moving. The sounds that are played are based on what the player is wearing.
* :underlined:`enableWetSurfaceAccents` - Enables water splash sounds when walking on blocks such as lily pads. Also, a splash sound will play when walking out in the open during a rain storm.
* :underlined:`enableFloorSqueaks` - Enables playing floor squeeks when walking on wooden floors.
* :underlined:`enableLeafAccents` - Enables playing sound effects when walking on leaf blocks.

particleTweaks
++++++++++++++

.. code-block:: JSON

    {
        "particleTweaks": {
            "suppressProjectileParticleTrails": false
        }
    }

* :underlined:`suppressProjectileParticleTrails` - Enables suppression of the particle trail generated by shooting an arrow.

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

* :underlined:`enableClock` - Enables the display of World Time and season information when holding a clock. Additionally, if an item frame is placed with clock as the framed item, looking at the framed clock will also display time and season information.
* :underlined:`enableCompass` - Enables the display of a compass HUD when holding a compass.
* :underlined:`compassStyle` - The style of compass to display. Possible selections are ``OPAQUE``, ``TRANSPARENT``, ``OPAQUE_WITH_INDICATOR``, and ``TRANSPARENT_WITH_INDICATOR``.
* :underlined:`scale` - The scaling factor to apply when rendering the compass HUD.

otherOptions
++++++++++++

.. code-block:: JSON

    {
        "otherOptions": {
            "playRandomSoundOnStartup": true
        }
    }

* :underlined:`playRandomSoundOnStartup` - Enables the play of a random sound when the Minecraft client starts.