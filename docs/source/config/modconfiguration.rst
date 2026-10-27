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
            "action": "cull"
        },
        {
            "soundEventId": "namespace:path2",
            "volumeScale": 50
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
        - The :term:`resource location <Resource Location>` of the sound in question. For example, the sheep bleating sound effect has the ID of ``minecraft:entity.sheep.ambient``. This is a *required* field.
    *   - volumeScale
        - Scaling factor to apply when playing a sound instance with that resource ID. Default is ``100``, and is not required. The value can be 0 - 400 where 0 mutes the sound entirely.
    *   - action
        - What happens when the sound plays: ``default`` (it plays normally), ``cull`` or ``block``. Culling limits the number of sound plays for a given resource ID over a short
          period of time. For example, if you have a farm with a lot of animals, culling sounds will reduce the overall sound load on the Minecraft sound engine as well as your ears.
          Blocking stops the sound from playing at all; usually this is applied to sounds and effects that are considered annoying. Default is ``default``, which is left out of the
          file, and is not required. (*Added 1.21.1-0.4.8*)

Before 1.21.1-0.4.8 the file had separate ``block`` and ``cull`` flags, and a ``startup`` flag for the random sound played when the game finished loading. An older file is still
read: ``"cull": true`` becomes ``cull``, ``"block": true`` becomes ``block`` (a sound with both is culled), and ``startup`` is ignored. The file is written in the new form the next
time it is saved.

dsurround.json
--------------

This Json file is comprised of multiple sections, with related options grouped within. These settings can be changed in the mod configuration menu, assuming the appropriate mod support is available.

In each section below the value of a setting is the default. The examples show the section as Dynamic Surroundings writes it: above each setting is a comment describing it, followed
by its range or possible values, its default, and, for a setting that only takes effect after restarting Minecraft or rejoining the world, a note saying so (*added 1.21.1-0.4.7*). The comments are rewritten each time the file is saved, so any comments added by hand will not be kept. Comments are allowed when
editing the file by hand. (*Comments added 1.21.1-0.4.6*)

Some settings have moved to a different section, or been renamed, between releases. When an older ``dsurround.json`` is loaded, the values of moved settings are carried over to their new
location automatically.

Settings for experimental features are colored orchid in the configuration menu. Experimental features are subject to change and may be removed in a future release. (*Added 1.21.1-0.4.7*)

generalOptions
++++++++++++++

*General Options* in the configuration menu. (*Added 1.21.1-0.4.8*)

.. code-block:: JSON

    {
      // General configuration options for the mod
      "generalOptions": {
        // Enable/disable chat window notification of newer updates available
        // Default: true
        "enableModUpdateChatMessage": true,
        // Enable/disable registration of client side commands
        // Default: true
        // Changes take effect after restarting Minecraft
        "registerCommands": true
      }
    }

.. confval:: generalOptions.enableModUpdateChatMessage
    :type: ``boolean``
    :default: ``true``
    :no-contents-entry:

    Enables display of version check results in the chat window when the player joins a world. (*Moved from* ``logging.enableModUpdateChatMessage``
    *in 1.21.1-0.4.8*)

.. confval:: generalOptions.registerCommands
    :type: ``boolean``
    :default: ``true``
    :no-contents-entry:

    Enables/disables registration of client side commands. Requires a restart. (*Moved from* ``logging.registerCommands`` *in 1.21.1-0.4.8*)

soundSystem
+++++++++++

.. code-block:: JSON

    {
      // Configuration options for modifying Minecraft's Sound System behavior
      "soundSystem": {
        // The number of sound channels to reserve for streaming sounds (music, biome sounds, records, etc.)
        // Range: 8 - 16, default: 12
        // Changes take effect after restarting Minecraft
        "streamingChannels": 12,
        // Ticks between culled sound events (0 to disable culling)
        // Range: 0 - 200, default: 20
        "cullInterval": 20,
        // Enables/disables cancellation of sound that a player will not hear
        // Default: true
        "enableSoundPruning": true
      }
    }

.. confval:: soundSystem.streamingChannels
    :type: ``integer``
    :default: ``12``
    :no-contents-entry:

    The number of sound channels to reserve for streaming. Sounds that are typically streamed are music and background sound tracks for biomes. Streaming means that sound information is read from disk throughout the sound play, whereas non-streaming the sound information is read all at once before sending to the engine. This value can be 8 - 16. Requires a restart. Recommendation is not touch this setting unless there is a real need.

.. confval:: soundSystem.cullInterval
    :type: ``integer``
    :default: ``20``
    :no-contents-entry:

    The number of ticks over which sounds are culled. The default of ``20`` means that a sound will be culled over a 1 second interval. This value can be 0 - 200. Setting to 0 disables sound culling.

.. confval:: soundSystem.enableSoundPruning
    :type: ``boolean``
    :default: ``true``
    :no-contents-entry:

    Determines if Dynamic Surroundings will automatically prevent sounds from playing that are too far away for the player to hear. Intent is to reduce needless load in the Minecraft sound engine. Does not apply to global, non-attenuated, or weather sounds.

enhancedSounds
++++++++++++++

.. code-block:: JSON

    {
      // Configuration options for enhanced sound processing
      "enhancedSounds": {
        // Enable/disable enhanced sound processing (reverb, occlusion, etc)
        // Default: true
        // Changes take effect after restarting Minecraft
        "enableEnhancedSounds": true,
        // Number of background threads to use for enhanced sound processing (0 means use internal default)
        // Range: 0 - 8, default: 0
        // Changes take effect after restarting Minecraft
        "backgroundThreadWorkers": 0,
        // Enable/disable sound occlusion processing (sound muffling behind blocks)
        // Default: false
        "enableOcclusionProcessing": false,
        // Apply enhanced sound processing to players' voices from Simple Voice Chat
        // Default: true
        "enableVoiceChatProcessing": true,
        // Check whether reflections reach the player only from each reverb ray's last reflection, instead of from every reflection. Cheaper; may sound different
        // Default: false
        "simplifiedSharedAirspace": false,
        // The number of rays to project around a sound location to calculate reverb effect
        // Range: 16 - 64, default: 32
        // Changes take effect after restarting Minecraft
        "reverbRays": 32,
        // The number of reflections the ray calculation will perform before ending a ray calculation
        // Range: 2 - 8, default: 4
        // Changes take effect after restarting Minecraft
        "reverbBounces": 4,
        // Total distance a reverb ray will traverse before ending calculation
        // Range: 64 - 256, default: 128
        // Changes take effect after restarting Minecraft
        "reverbRayTraceDistance": 128
      }
    }

.. confval:: enhancedSounds.enableEnhancedSounds
    :type: ``boolean``
    :default: ``true``
    :no-contents-entry:

    Enables/disables enhanced sound processing by Dynamic Surroundings. Enhanced sound processing is what provides reverb in caves. Requires a restart.

.. confval:: enhancedSounds.backgroundThreadWorkers
    :type: ``integer``
    :default: ``0``
    :no-contents-entry:

    This is the number of compute threads that run in the background to perform calculations for enhanced sounds. This value can be 0 - 8, where 0 means use the internal default. Requires a restart. Recommendation is to not change this setting.

.. confval:: enhancedSounds.enableOcclusionProcessing
    :type: ``boolean``
    :default: ``false``
    :no-contents-entry:

    Occlusion processing is an advanced feature of the sound processing system. If enabled, Dynamic Surroundings will perform calculations to "muffle" a sound that is behind blocks from the perspective of the player. This processing will require additional horsepower so it is disabled by default.

.. confval:: enhancedSounds.enableVoiceChatProcessing
    :type: ``boolean``
    :default: ``true``
    :no-contents-entry:

    *Experimental*. With `Simple Voice Chat <https://modrinth.com/plugin/simple-voice-chat>`_ installed, the voices of nearby players get the same reverb, occlusion, and air absorption as other sounds, so a player talking in a cave echoes. Group chat, which is not positional, plays as it is. Has no effect unless :confval:`enhancedSounds.enableEnhancedSounds` is on. Takes effect immediately. (*Added 1.21.1-0.4.7*)

.. confval:: enhancedSounds.simplifiedSharedAirspace
    :type: ``boolean``
    :default: ``false``
    :no-contents-entry:

    Reverb is brighter when reflections can reach the player directly (the player shares the space with the sound). Normally this is checked from every reflection of every reverb ray; simplified checks only each ray's last reflection, which casts up to a quarter as many rays. Cheaper, but may sound different. Takes effect immediately. (*Added 1.21.1-0.4.6*)

.. confval:: enhancedSounds.reverbRays
    :type: ``integer``
    :default: ``32``
    :no-contents-entry:

    As part of the calculation process of the enhanced sound engine, logic will cast a number of "rays" away from the player to get a sense of the space the player is located within. Increasing this value will improve fidelity at the expense of processing power. This value can be 16 - 64. Requires a restart. Recommendation is to leave at the default.

.. confval:: enhancedSounds.reverbBounces
    :type: ``integer``
    :default: ``4``
    :no-contents-entry:

    When casting out a ray, if the ray intersects with the block surface it will be reflected at an angle, or bounced. This setting controls the number of bounces that are permitted before a given ray path trace is terminated. Increasing this value will improve fidelity at the expense of processing power. This value can be 2 - 8. Requires a restart. Recommendation is to leave at the default.

.. confval:: enhancedSounds.reverbRayTraceDistance
    :type: ``integer``
    :default: ``128``
    :no-contents-entry:

    The maximum number of blocks a ray will be traced before termination. Note that this is not actual distance from the player, its the total distance traveled which includes bounces. This value can be 64 - 256. Requires a restart. Recommendation is to leave at the default. (*Default changed from 256 to 128 in 1.21.1-0.4.6*)

soundOptions
++++++++++++

.. code-block:: JSON

    {
      // Configuration options for sounds in general
      "soundOptions": {
        // Discard sounds that are played from a non-client thread
        // Default: true
        "discardNonClientSoundPlays": true,
        // Emit stack trace when discarding sounds
        // Default: false
        "logStacktraceWhenDiscarding": false,
        // Ambient sounds played by the mod will be multiplied by this factor
        // Range: 0 - 400, default: 100
        "ambientVolumeScaling": 100,
        // Enables replacement of thunder sounds with Dynamic Surroundings' version
        // Default: true
        "replaceThunderSounds": true,
        // Enables playing biome background music while in creative
        // Default: false
        "playBiomeMusicWhileCreative": false,
        // Enables display of toast messages for credited music
        // Default: true
        "displayToastMessagesForMusic": true,
        // Enables sound remapping when sounds are played
        // Default: true
        "remapSounds": true
      }
    }

.. confval:: soundOptions.discardNonClientSoundPlays
    :type: ``boolean``
    :default: ``true``
    :no-contents-entry:

    Flag indicating whether to discard sound plays by non-client threads. Sounds played by non-client threads run the risk of triggering comodiciation exceptions which will crash the client. Ignored when Raise Sound Limit Simplified is installed. (*Added 1.21.1-0.4.4*)

.. confval:: soundOptions.logStacktraceWhenDiscarding
    :type: ``boolean``
    :default: ``false``
    :no-contents-entry:

    Flag indicating whether to log a stack trace when discarding a sound play. This is useful for debugging issues with other mods that are not playing sounds correctly. (*Added 1.21.1-0.4.4*)

.. confval:: soundOptions.ambientVolumeScaling
    :type: ``integer``
    :default: ``100``
    :no-contents-entry:

    Scaling factor to apply to all ambient sounds that are played. This factor is on top of the sound slider scaling of Minecraft. This value can be 0 - 400.

.. confval:: soundOptions.replaceThunderSounds
    :type: ``boolean``
    :default: ``true``
    :no-contents-entry:

    Flag indicating whether to replace Minecraft's thunder sounds with the ones from Dynamic Surroundings.

.. confval:: soundOptions.playBiomeMusicWhileCreative
    :type: ``boolean``
    :default: ``false``
    :no-contents-entry:

    Normally when a player is in creative mode the music that is played is for the creative session. Enabling this feature will allow the regular biome music to play as if the player was not in creative mode.

.. confval:: soundOptions.displayToastMessagesForMusic
    :type: ``boolean``
    :default: ``true``
    :no-contents-entry:

    Controls whether a toast popout will be displayed when playing music that required atribution.

.. confval:: soundOptions.remapSounds
    :type: ``boolean``
    :default: ``true``
    :no-contents-entry:

    Enables sound remapping when sounds are played. Enabling tells Dynamic Surroundings to replace various step sounds with replacement versions, and a bow's
    shot, by a player or a skeleton, with the bowstring's release. (*Added 1.21.1-0.4.2; bow shots added 1.21.1-0.4.8*)

scaryContent
++++++++++++

*Added 1.21.1-0.4.8*

Options for content some players find frightening. A parent can use these to control what younger players see and hear.

.. code-block:: JSON

    {
      // Configuration options for content some players find frightening
      "scaryContent": {
        // Enables content that is considered scary: sounds marked as scary, and lightning
        // Default: true
        "allowScaryContent": true,
        // Enable/disable lightning: branching bolts in place of vanilla's, flashes in the sky during thunderstorms, and their thunder. Off while scary content is off
        // Default: true
        "enableLightning": true
      }
    }

.. confval:: scaryContent.allowScaryContent
    :type: ``boolean``
    :default: ``true``
    :no-contents-entry:

    Flag indicating whether scary content is enabled within the mod: sounds that are considered scary, such as wolves and monster growls at night and the
    heartbeat at low health, and the mod's lightning. Turning it off also turns off the lightning, whatever :confval:`scaryContent.enableLightning` is set to. Scripts read it with
    ``global.allowScary()``; which sounds are scary is up to the configuration (see :doc:`../concepts/acoustic`). (*Moved from*
    ``soundOptions.allowScarySounds`` *in 1.21.1-0.4.8*)

.. confval:: scaryContent.enableLightning
    :type: ``boolean``
    :default: ``true``
    :no-contents-entry:

    Flag indicating whether the mod's lightning is shown: lightning that branches and forks in place of Minecraft's bolts, and through a thunderstorm
    lightning in the sky with its thunder (see :doc:`../features`). Off while :confval:`scaryContent.allowScaryContent` is off, and not drawn while a shader
    pack is in use; Minecraft's own bolts are drawn then. With Minecraft's *Hide Lightning Flashes* accessibility option on, there is no lightning in the sky,
    and bolts strike once without flickering. Scripts read whether lightning is shown with ``global.allowLightning()``. (*Added 1.21.1-0.4.8*)

blockEffects
++++++++++++

.. code-block:: JSON

    {
      // Configuration options for block effects
      "blockEffects": {
        // Radius around the player, in blocks, where block effects (waterfalls, steam, random block effects) are found and shown. Past 32, effects show farther than vanilla particles, at more cost.
        // Range: 16 - 64, default: 40
        "blockEffectRange": 40,
        // Enable/disable steam column effect when liquids are adjacent to hot sources, like lava and magma
        // Default: true
        "steamColumnEnabled": true,
        // Enable/disable little flames burning in the eyes of skeleton skulls placed in the world (blue soul fire for wither skeleton skulls)
        // Default: true
        "skullFlamesEnabled": true,
        // Enable/disable bubble columns generated underwater
        // Default: true
        "bubbleColumnEnabled": true,
        // The style of water ripple to render when a drop hits a fluid
        // Values: NONE, PIXELATED_CIRCLE, default: "PIXELATED_CIRCLE"
        "waterRippleStyle": "PIXELATED_CIRCLE"
      }
    }

.. confval:: blockEffects.blockEffectRange
    :type: ``integer``
    :default: ``40``
    :no-contents-entry:

    The radius around the player, in blocks, within which block effects such as waterfalls, steam, and flame jets are found and shown. This value can be 16 - 64 blocks. Past 32, effects show farther away than Minecraft shows particles; increasing the distance increases the load within the client tick. Changing it resets the effects and rescans the area. (*A sphere since 1.21.1-0.4.8, with the default raised from 32 to 40, which scans about as many blocks as the old 32 block cube*)

.. confval:: blockEffects.steamColumnEnabled
    :type: ``boolean``
    :default: ``true``
    :no-contents-entry:

    Enables the steam effect for when water is close to a hot block (ie, something like lava or magma).

.. confval:: blockEffects.skullFlamesEnabled
    :type: ``boolean``
    :default: ``true``
    :no-contents-entry:

    Enables little flickering flames in the eyes of skeleton skulls placed in the world, with blue soul fire in wither
    skeleton skulls. The flames light the floor and wall around the skull (see :confval:`flameJetOptions.enableLight`).
    (*Added 1.21.1-0.4.8*)

.. confval:: blockEffects.bubbleColumnEnabled
    :type: ``boolean``
    :default: ``true``
    :no-contents-entry:

    Enables the bubble effect when under water.

.. confval:: blockEffects.waterRippleStyle
    :type: ``string``
    :default: ``"PIXELATED_CIRCLE"``
    :no-contents-entry:

    The style of water ripple for when rain hits a liquid surface. Currently ``PIXELATED_CIRCLE`` is the only option.

waterfallOptions
++++++++++++++++

*Added 1.21.1-0.4.6*

.. code-block:: JSON

    {
      // Configuration options for waterfalls
      "waterfallOptions": {
        // Enable/disable waterfall effects where flowing water lands
        // Default: true
        "enableWaterfalls": true,
        // Enable/disable sounds from waterfalls, and from water stepping down a block
        // Default: true
        "enableSounds": true,
        // Enable/disable particles from waterfalls: their splashes, and the mist and foam where they land
        // Default: true
        "enableParticles": true,
        // Enable/disable waterfall mist: many small puffs of mist thrown up where a waterfall lands
        // Default: true
        "enableMist": true,
        // Enable/disable water froth: foam where flowing water drops one block (with a gentle sound) and around where waterfalls land
        // Default: true
        "enableFroth": true
      }
    }

.. confval:: waterfallOptions.enableWaterfalls
    :type: ``boolean``
    :default: ``true``
    :no-contents-entry:

    Enables waterfall effects, their sounds and particles, where flowing water lands. Turning this off disables waterfalls entirely. (*Formerly* ``blockEffects.waterfallsEnabled``)

.. confval:: waterfallOptions.enableSounds
    :type: ``boolean``
    :default: ``true``
    :no-contents-entry:

    Enables waterfall sounds, and the gentle sound of water stepping down a block. Particles still show if enabled. (*Formerly* ``blockEffects.enableWaterfallSounds``)

.. confval:: waterfallOptions.enableParticles
    :type: ``boolean``
    :default: ``true``
    :no-contents-entry:

    Enables particles from waterfalls: their splashes, and the mist and foam where they land. Sounds still play if enabled. (*Formerly* ``blockEffects.enableWaterfallParticles``)

.. confval:: waterfallOptions.enableMist
    :type: ``boolean``
    :default: ``true``
    :no-contents-entry:

    Enables waterfall mist: many small puffs of mist thrown up and drifting out from where a waterfall lands.

.. confval:: waterfallOptions.enableFroth
    :type: ``boolean``
    :default: ``true``
    :no-contents-entry:

    Enables water froth: foam on the water, carried along by the current. Forms where flowing water drops one block (on every step down a slope, with a gentle sound) and around where waterfalls land.

flameJetOptions
+++++++++++++++

*Added 1.21.1-0.4.7*

.. code-block:: JSON

    {
      // Configuration options for flame jets
      "flameJetOptions": {
        // Enable/disable flame jets over lava and nether wart
        // Default: true
        "enableFlameJets": true,
        // Enable/disable the flicker of flame jets' and burning mobs' light on their surroundings
        // Default: true
        "enableLight": true
      }
    }

.. confval:: flameJetOptions.enableFlameJets
    :type: ``boolean``
    :default: ``true``
    :no-contents-entry:

    Enables flame jets produced over lava sources as well as lava cauldrons and max age nether wart. (*Formerly* ``blockEffects.flameJetEnabled``)

.. confval:: flameJetOptions.enableLight
    :type: ``boolean``
    :default: ``true``
    :no-contents-entry:

    Enables the flickering light flame jets, burning mobs and skull flames cast on the ground and walls around them. Not shown while a shader pack is in use.

fireflyOptions
++++++++++++++

*Added 1.21.1-0.4.6*

.. code-block:: JSON

    {
      // Configuration options for fireflies
      "fireflyOptions": {
        // Enable/disable fireflies
        // Default: true
        "enableFireflies": true,
        // Enable/disable a soft glow around fireflies
        // Default: true
        "enableGlow": true,
        // Enable/disable fireflies lighting the grass, leaves and ground close to them. Not shown while a shader pack is in use
        // Default: true
        "enableLight": true
      }
    }

.. confval:: fireflyOptions.enableFireflies
    :type: ``boolean``
    :default: ``true``
    :no-contents-entry:

    Enables the firefly effect around flowers at night. (*Formerly* ``blockEffects.firefliesEnabled``)

.. confval:: fireflyOptions.enableGlow
    :type: ``boolean``
    :default: ``true``
    :no-contents-entry:

    Enables a soft glow around fireflies.

.. confval:: fireflyOptions.enableLight
    :type: ``boolean``
    :default: ``true``
    :no-contents-entry:

    Enables fireflies lighting the grass, leaves and ground close to them. Not shown while a shader pack is in use.

entityEffects
+++++++++++++

.. code-block:: JSON

    {
      // Configuration options for entity effects
      "entityEffects": {
        // The maximum range at which entity special effects are applied
        // Range: 16 - 64, default: 32
        "entityEffectRange": 32,
        // Enable/disable bow pull sound effect
        // Default: true
        "enableBowPull": true,
        // Enable/disable breath effect in cold biomes and underwater
        // Default: true
        "enableBreathEffect": true,
        // Enable/disable breath from animals (cows, sheep, horses, wolves...) near you, along with the breath effect
        // Default: true
        "enableAnimalBreath": true,
        // Enable/disable player toolbar sound effects
        // Default: true
        "enablePlayerToolbarEffect": true,
        // Enable/disable item swing sound effects from players and mobs
        // Default: true
        "enableSwingEffect": true,
        // Enable/disable a breath when you jump, heard by you only
        // Default: false
        "enableJumpSound": false,
        // Enable/disable sound effect when walking through dense brush
        // Default: true
        "enableBrushStepEffect": true,
        // Enable/disable flames like a flame jet's on burning mobs, in place of vanilla's flat fire. Vanilla's fire stays past the entity effect range, with Particles on Minimal and while a shader pack is in use
        // Default: true
        "enableBurningEffect": true,
        // Enable/disable dark mist where a mob's body vanishes when it dies, in place of vanilla's white puffs
        // Default: true
        "enableDeathPuffs": true,
        // Enable/disable numbers popping off mobs and players when their health changes: red for damage, green for healing
        // Default: true
        "enableDamagePopoffs": true,
        // Enable/disable a comic book word over a heavy blow's number
        // Default: true
        "showCritWords": true,
        // Enable/disable footprints left by players and mobs walking on soft ground: dirt, sand, gravel, snow, mud
        // Default: true
        "enableFootprints": true,
        // The look of players' footprints
        // Values: SHOE, SQUARE, HORSESHOE, BIRD, PAW, SQUARE_SOLID, LOWRES_SQUARE, default: "SQUARE"
        "footprintStyle": "SQUARE"
      }
    }

.. confval:: entityEffects.entityEffectRange
    :type: ``integer``
    :default: ``32``
    :no-contents-entry:

    The maximum distance from the player that entity effects will be applied. This value can be 16 - 64. Recommendation is to leave at the default setting. (*Default raised from 24 to 32 in 1.21.1-0.4.8*)

.. confval:: entityEffects.enableBowPull
    :type: ``boolean``
    :default: ``true``
    :no-contents-entry:

    Enables the sound effects related to pulling back on a bow.

.. confval:: entityEffects.enableBreathEffect
    :type: ``boolean``
    :default: ``true``
    :no-contents-entry:

    Enables frost breath particle generation when in a cold biome, and bubbles when underwater.

.. confval:: entityEffects.enableAnimalBreath
    :type: ``boolean``
    :default: ``true``
    :no-contents-entry:

    Animals within 16 blocks breathe too, from their mouths: cows, sheep, goats, horses, wolves, and others (see
    ``dsurround:effects/animal_breath`` in :doc:`../packs/tagging`). Needs :confval:`entityEffects.enableBreathEffect`.
    (*Added 1.21.1-0.4.8*)

.. confval:: entityEffects.enablePlayerToolbarEffect
    :type: ``boolean``
    :default: ``true``
    :no-contents-entry:

    Enables sound play when selecting between different items on the hotbar.

.. confval:: entityEffects.enableSwingEffect
    :type: ``boolean``
    :default: ``true``
    :no-contents-entry:

    Enables sound effects when players and mobs swing an item, such as swords and axes.

.. confval:: entityEffects.enableJumpSound
    :type: ``boolean``
    :default: ``false``
    :no-contents-entry:

    Plays a breath when you jump, heard by you only. Stepping up a stair or walking off an edge isn't a jump, and there is
    none while sneaking, in water, riding, or flying. (*Back from older versions in 1.21.1-0.4.8*)

.. confval:: entityEffects.enableBrushStepEffect
    :type: ``boolean``
    :default: ``true``
    :no-contents-entry:

    Enables sound effect when moving through blocks that are considered brush, such as tall flowers and grass.

.. confval:: entityEffects.enableBurningEffect
    :type: ``boolean``
    :default: ``true``
    :no-contents-entry:

    Enables flames like a flame jet's on burning mobs, in place of Minecraft's flat fire. Minecraft's fire stays beyond :confval:`entityEffects.entityEffectRange`, with Particles on Minimal, while a shader pack is in use, and for the player's own body in first person. (*Added 1.21.1-0.4.8*)

.. confval:: entityEffects.enableDeathPuffs
    :type: ``boolean``
    :default: ``true``
    :no-contents-entry:

    Enables dark mist where a mob's body vanishes when it dies, in place of Minecraft's white puffs. Minecraft's puffs stay with Particles on Minimal. (*Added 1.21.1-0.4.8*)

.. confval:: entityEffects.enableDamagePopoffs
    :type: ``boolean``
    :default: ``true``
    :no-contents-entry:

    Enables numbers popping off mobs and players when their health changes: red for damage, green for healing. (*Added 1.21.1-0.4.8*)

.. confval:: entityEffects.showCritWords
    :type: ``boolean``
    :default: ``true``
    :no-contents-entry:

    Enables a comic book word, such as KAPOW!, over the number of a heavy blow: 40% or more of the mob's health. (*Added 1.21.1-0.4.8*)

.. confval:: entityEffects.enableFootprints
    :type: ``boolean``
    :default: ``true``
    :no-contents-entry:

    Enables footprints left by players and mobs walking on soft ground: dirt, grass, sand, gravel, snow, and mud. Prints fade after a while, last longer in snow, and wash away faster in the rain. None while sneaking, with Particles on Minimal, or while a shader pack is in use. (*Added 1.21.1-0.4.8*)

.. confval:: entityEffects.footprintStyle
    :type: ``string``
    :default: ``SQUARE``
    :no-contents-entry:

    The look of players' footprints: ``SHOE``, ``SQUARE``, ``HORSESHOE``, ``BIRD``, ``PAW``, ``SQUARE_SOLID``, or ``LOWRES_SQUARE``. Mobs' prints depend on their feet, set by tags (see :doc:`../packs/tagging`). (*Added 1.21.1-0.4.8*)

footstepAccents
+++++++++++++++

.. code-block:: JSON

    {
      // Configuration options for footstep accent effects
      "footstepAccents": {
        // Enable/disable foot step accents globally
        // Default: true
        "enableAccents": true,
        // Enable/disable accents for armor that is worn
        // Default: true
        "enableArmorAccents": true,
        // Enable/disable accents when it is raining or blocks are waterlogged
        // Default: true
        "enableWetSurfaceAccents": true,
        // Enable/disable accents when the player is walking on squeaky blocks
        // Default: true
        "enableFloorSqueaks": true
      }
    }

.. confval:: footstepAccents.enableAccents
    :type: ``boolean``
    :default: ``true``
    :no-contents-entry:

    Enables the footstep sound effects when moving.

.. confval:: footstepAccents.enableArmorAccents
    :type: ``boolean``
    :default: ``true``
    :no-contents-entry:

    Enables armor sounds when moving. The sounds that are played are based on what the player is wearing.

.. confval:: footstepAccents.enableWetSurfaceAccents
    :type: ``boolean``
    :default: ``true``
    :no-contents-entry:

    Enables water splash sounds when walking on blocks such as lily pads. Also, a splash sound will play when walking out in the open during a rain storm.

.. confval:: footstepAccents.enableFloorSqueaks
    :type: ``boolean``
    :default: ``true``
    :no-contents-entry:

    Enables playing floor squeaks when walking on wooden floors.

particleTweaks
++++++++++++++

.. code-block:: JSON

    {
      // Configuration options for tweaking particle behavior
      "particleTweaks": {
        // Enable/disable showing of projectile particle trails
        // Default: false
        "suppressProjectileParticleTrails": false,
        // Smoke, ash, leaves and spores, from the game and other mods, drift with the wind out in the open
        // Default: true
        "windBlowsParticles": true
      }
    }

.. confval:: particleTweaks.suppressProjectileParticleTrails
    :type: ``boolean``
    :default: ``false``
    :no-contents-entry:

    Enables suppression of the particle trail generated by shooting an arrow.

.. confval:: particleTweaks.windBlowsParticles
    :type: ``boolean``
    :default: ``true``
    :no-contents-entry:

    *Added 1.21.1-0.4.7*. Particles from Minecraft and other mods, such as smoke, ash, falling leaves, and spores, drift with the simulated wind when they are
    made out in the open. Particles made indoors or in a cave are left as they are. Which particles drift is set by the ``dsurround:effects/wind_blown``
    particle type tag; see :doc:`../packs/tagging`.

compassAndClockOptions
++++++++++++++++++++++

.. code-block:: JSON

    {
      // Configuration options for the compass and clock overlay
      "compassAndClockOptions": {
        // Style of compass rendering, or NONE for no compass display
        // Values: NONE, OPAQUE, TRANSPARENT, OPAQUE_WITH_INDICATOR, TRANSPARENT_WITH_INDICATOR, ROSE_1, ROSE_2, ROSE_3, default: "TRANSPARENT_WITH_INDICATOR"
        "compassStyle": "TRANSPARENT_WITH_INDICATOR",
        // Style of clock rendering, or NONE for no clock display
        // Values: NONE, TEXT, POCKET_WATCH, POCKET_WATCH_WITH_TEXT, default: "POCKET_WATCH"
        "clockStyle": "POCKET_WATCH",
        // Shows the compass and pocket watch in a side or corner of the screen while one is in the hot bar or off hand, rather than above the crosshair while held
        // Default: false
        "showInMargin": false,
        // The side or corner of the screen for the compass and pocket watch when shown there
        // Values: TOP_LEFT, TOP, TOP_RIGHT, LEFT, RIGHT, BOTTOM_LEFT, BOTTOM, BOTTOM_RIGHT, default: "LEFT"
        "marginPosition": "LEFT",
        // Scales the display by the specified amount
        // Range: 0.5 - 4, step: 0.1, default: 1.0
        "scale": 1.0
      }
    }

.. confval:: compassAndClockOptions.compassStyle
    :type: ``string``
    :default: ``"TRANSPARENT_WITH_INDICATOR"``
    :no-contents-entry:

    The style of compass to display when holding a compass. ``OPAQUE``, ``TRANSPARENT``, ``OPAQUE_WITH_INDICATOR``, and ``TRANSPARENT_WITH_INDICATOR`` show a band
    above the crosshair that slides with the player's heading. ``ROSE_1``, ``ROSE_2``, and ``ROSE_3`` (*added 1.21.1-0.4.7*) show a compass rose laid flat in front of
    the player that turns with the heading. ``NONE`` (*added 1.21.1-0.4.7*) turns the compass display off; it replaces the earlier ``enableCompass`` setting, and a
    configuration with ``enableCompass`` off is changed to ``NONE`` when loaded.

.. confval:: compassAndClockOptions.clockStyle
    :type: ``string``
    :default: ``"POCKET_WATCH"``
    :no-contents-entry:

    *Added 1.21.1-0.4.7*. The style of clock to display when holding a clock, or looking at a clock in an item frame:

    * ``NONE`` turns the clock display off. It replaces the earlier ``enableClock`` setting, and a configuration with ``enableClock`` off is changed to ``NONE``
      when loaded.
    * ``TEXT`` shows the day, the time and the season as text above the hot bar.
    * ``POCKET_WATCH`` shows a pocket watch above the crosshair. Its hands tick from minute to minute; a window under XII shows day or night, as Minecraft's
      clock does, to tell noon from midnight; and a window above VI shows the season when Serene Seasons is installed, or the moon's phase without it. When the
      compass is shown as well, the watch sits beside it, on the side of the hand holding the clock.
    * ``POCKET_WATCH_WITH_TEXT`` shows both.

    The pocket watch's textures can be replaced by a resource pack; see :doc:`../packs/overlay_textures`.

.. confval:: compassAndClockOptions.showInMargin
    :type: ``boolean``
    :default: ``false``
    :no-contents-entry:

    *Added 1.21.1-0.4.7*. Shows the compass and the pocket watch in a side or corner of the screen, picked by :confval:`compassAndClockOptions.marginPosition`,
    while a compass or clock is anywhere in the hot bar or in the off hand, rather than above the crosshair only while one is held. There they are drawn smaller:
    the compass rose and the pocket watch are 64 GUI pixels across, and the compass band is half its usual size. The compass rose stands upright rather than lying
    flat, and turns with the player's heading. The clock's text, from the ``TEXT`` and ``POCKET_WATCH_WITH_TEXT`` styles, is still shown above the hot bar, and only
    while a clock is held.

.. confval:: compassAndClockOptions.marginPosition
    :type: ``string``
    :default: ``"LEFT"``
    :no-contents-entry:

    *Added 1.21.1-0.4.7*. The side or corner of the screen for the compass and pocket watch when :confval:`compassAndClockOptions.showInMargin` is on: ``TOP_LEFT``,
    ``TOP``, ``TOP_RIGHT``, ``LEFT``, ``RIGHT``, ``BOTTOM_LEFT``, ``BOTTOM``, or ``BOTTOM_RIGHT``. When both are shown, they sit one above the other, compass first,
    on the sides and in the corners, and side by side, compass on the left, at ``TOP`` and ``BOTTOM``. ``BOTTOM`` places them above the hot bar and the health,
    armor, and food bars.

.. confval:: compassAndClockOptions.scale
    :type: ``number``
    :default: ``1.0``
    :no-contents-entry:

    The scaling factor to apply when rendering the compass and the pocket watch, including when they are shown in the screen margin. This value can be 0.5 - 4.0.

lightLevelOptions
+++++++++++++++++

*Added 1.21.1-0.4.7*

Options for the light level overlay, which is turned on and off with the *Light Level Overlay* key (under *Dynamic Surroundings* in the controls; it starts unbound).
See :doc:`../features` for what the colors mean.

.. code-block:: JSON

    {
      // Configuration options for the light level overlay
      "lightLevelOptions": {
        // The light shown on each block: BLOCK (torches and other lights), SKY (as it is now), or BLOCK_SKY (the brighter of the two)
        // Values: BLOCK, SKY, BLOCK_SKY, default: "BLOCK"
        "mode": "BLOCK",
        // The colors for the numbers: BRIGHT or DARK
        // Values: BRIGHT, DARK, default: "BRIGHT"
        "colors": "BRIGHT",
        // How many blocks out from the player light levels are shown
        // Range: 8 - 32, default: 16
        "range": 16,
        // Shows numbers only where monsters can spawn
        // Default: false
        "hideSafe": false,
        // Shows what the colors mean in the bottom right corner of the screen while light levels are shown
        // Default: true
        "showLegend": true
      }
    }

.. confval:: lightLevelOptions.mode
    :type: ``string``
    :default: ``"BLOCK"``
    :no-contents-entry:

    The light shown as the number on each block: ``BLOCK`` for light from torches, lava, and other light giving blocks; ``SKY`` for light from the sky as it is now,
    darker at night and in storms; ``BLOCK_SKY`` for the brighter of the two, the light a mob sees. Whichever is shown, the color always tells whether monsters can
    spawn there.

.. confval:: lightLevelOptions.colors
    :type: ``string``
    :default: ``"BRIGHT"``
    :no-contents-entry:

    The colors for the numbers. ``BRIGHT`` uses red where monsters can spawn now, yellow where they can once the sky darkens, green where it is too bright, and aqua
    where they can never spawn. ``DARK`` uses darker shades of the same: dark red, gold, dark green, and dark aqua.

.. confval:: lightLevelOptions.range
    :type: ``integer``
    :default: ``16``
    :no-contents-entry:

    How many blocks out from the player, east to west and north to south, light levels are shown, from 8 to 32. Below the player they are shown as far down as this,
    and above only a few blocks up.

.. confval:: lightLevelOptions.hideSafe
    :type: ``boolean``
    :default: ``false``
    :no-contents-entry:

    Shows numbers only where monsters can spawn, now or once the sky darkens: the red and yellow ones. The legend then lists only those two.

.. confval:: lightLevelOptions.showLegend
    :type: ``boolean``
    :default: ``true``
    :no-contents-entry:

    Shows what the colors mean, in the bottom right corner of the screen, while light levels are shown. It is hidden while Minecraft's F3 screen is open.

weatherOptions
++++++++++++++

*Added 1.21.1-0.4.7*

Dynamic Surroundings simulates storms on the client. When it starts to rain, each storm is given its own strength, from a drizzle to a downpour, rather than always building to full strength. Storms are
seeded by the Minecraft day so every player in a world sees the same storm on the same day. Storm simulation only works in dimensions where other mods do not hook weather rendering, and the particle
weather effects turn themselves off if the Particle Rain or Simple Weather mod is installed. The ``/dsweather`` command can be used to see how storms of a given strength look.

.. code-block:: JSON

    {
      // Configuration options for weather
      "weatherOptions": {
        // Enable/disable simulated storms, each storm has its own strength, from a drizzle to a downpour
        // Default: true
        "enableStormSimulation": true,
        // The weakest a storm can be, as a percent of full strength
        // Range: 1 - 100, default: 10
        "minStormIntensity": 10,
        // The strongest a storm can be, as a percent of full strength
        // Range: 1 - 100, default: 100
        "maxStormIntensity": 100,
        // How far a storm eases off between its surges, as a percent of its peak
        // Range: 0 - 100, default: 40
        "stormVariation": 40,
        // Draw rain and snow as individual drops instead of vanilla's sheets
        // Default: true
        "enableParticlePrecipitation": true,
        // How many drops of particle rain and snow there are, as a percent of the most
        // Range: 25 - 100, default: 100
        "precipitationDensity": 100,
        // How far from the player, in blocks, particle rain, snow and dust are drawn
        // Range: 8 - 32, default: 14
        "precipitationRange": 14,
        // How big particle rain drops are drawn, as a percent of their usual size
        // Range: 50 - 250, default: 100
        "rainDropScale": 100,
        // How blue particle rain is: 0 is a nearly colorless pale gray, 100 a deep blue
        // Range: 0 - 100, default: 15
        "rainTint": 15,
        // How big particle snowflakes are drawn, as a percent of their usual size
        // Range: 50 - 200, default: 100
        "snowflakeScale": 100,
        // With particle rain and snow on, storms in deserts and badlands blow dust and thicken the fog
        // Default: true
        "enableDustStorms": true,
        // Rain sounds that follow the storm's strength, from a patter to a roar, and the sound of blowing dust
        // Default: true
        "enableStormSounds": true,
        // Water drips from leaves and overhanging edges for a while after the rain stops
        // Default: true
        "enableAfterRainDrips": true,
        // With particle snow on, snowflakes blown by the wind against a wall or tree trunk stick to it for a moment
        // Default: true
        "enableSnowOnSides": true,
        // With particle rain on, rain drops run down the outside of windows in stick-and-slide streaks
        // Default: true
        "enableWindowStreaks": true,
        // Frost forms on the outside of clear glass windows when it is cold
        // Default: true
        "enableWindowFrost": true,
        // Mist lying low over the ground in swamps and eerie biomes: off, or how finely it is drawn. Fast costs least; Fabulous costs several times Fancy
        // Values: NONE, FAST, FANCY, FABULOUS, default: "FANCY"
        "groundFogQuality": "FANCY",
        // Clouds that change with the weather: scattered puffs that build up through fair afternoons, a low dark deck in a storm, towering in a thunderstorm. Drawn in place of vanilla's clouds
        // Default: true
        "enableDynamicClouds": true,
        // How far dynamic clouds reach, in chunks, whatever the render distance
        // Range: 8 - 32, default: 24
        "cloudDistance": 24
      }
    }

.. confval:: weatherOptions.enableStormSimulation
    :type: ``boolean``
    :default: ``true``
    :no-contents-entry:

    Enables simulated storms. Each storm has its own strength, from a drizzle to a downpour, rather than always building to full strength.

.. confval:: weatherOptions.minStormIntensity
    :type: ``integer``
    :default: ``10``
    :no-contents-entry:

    The weakest a storm can be, as a percent of full strength. This value can be 1 - 100.

.. confval:: weatherOptions.maxStormIntensity
    :type: ``integer``
    :default: ``100``
    :no-contents-entry:

    The strongest a storm can be, as a percent of full strength. This value can be 1 - 100.

.. confval:: weatherOptions.stormVariation
    :type: ``integer``
    :default: ``40``
    :no-contents-entry:

    How far a storm eases off between its surges, as a percent of its peak. A storm's strength rises and falls every half minute or so; at 0 it holds steady. This value can be 0 - 100.

.. confval:: weatherOptions.enableParticlePrecipitation
    :type: ``boolean``
    :default: ``true``
    :no-contents-entry:

    Draws rain and snow as individual drops near the player, as many as the storm's strength calls for, in place of vanilla's sheets of falling rain. Rain and snow drift with the wind. Not used while a shader pack is in use.

.. confval:: weatherOptions.precipitationDensity
    :type: ``integer``
    :default: ``100``
    :no-contents-entry:

    How many drops of particle rain and snow there are, and puffs of dust, as a percent of the most. Lower it if heavy rain or snow slows the game. The Particles video setting lowers it further: Decreased halves it, Minimal quarters it. This value can be 25 - 100.

.. confval:: weatherOptions.precipitationRange
    :type: ``integer``
    :default: ``14``
    :no-contents-entry:

    How far from the player, in blocks, particle rain, snow and dust are drawn. The drops are as dense at any range, so twice as far is four times as many drops to draw. Beyond the range the weather's fog stands in. The area is a circle around the player. This value can be 8 - 32. (*Default raised from 12 to 14, and the area made round rather than square, in 1.21.1-0.4.8*)

.. confval:: weatherOptions.rainDropScale
    :type: ``integer``
    :default: ``100``
    :no-contents-entry:

    How big particle rain drops are drawn, as a percent of their usual size. It changes only how the rain looks: drops fall and splash as before. This value can be 50 - 250.

.. confval:: weatherOptions.rainTint
    :type: ``integer``
    :default: ``15``
    :no-contents-entry:

    How blue particle rain is, falling and running down windows: 0 is a nearly colorless pale gray, 100 a deep blue. The rain is lit as the world is, so it
    is darker at night and in shade whatever its tint. This value can be 0 - 100. (*Added 1.21.1-0.4.7*)

.. confval:: weatherOptions.snowflakeScale
    :type: ``integer``
    :default: ``100``
    :no-contents-entry:

    How big particle snowflakes are drawn, as a percent of their usual size. Larger flakes cost more to draw: twice the size is about four times the work. This value can be 50 - 200.

.. confval:: weatherOptions.enableDustStorms
    :type: ``boolean``
    :default: ``true``
    :no-contents-entry:

    With particle rain and snow on, a storm in a desert or badlands blows dust along the ground and thickens the fog, in place of the rain other biomes get.

.. confval:: weatherOptions.enableStormSounds
    :type: ``boolean``
    :default: ``true``
    :no-contents-entry:

    Rain that sounds as strong as the storm: a soft patter in a drizzle, building to a roar in a downpour. Dust storms make the sound of blowing dust.

.. confval:: weatherOptions.enableAfterRainDrips
    :type: ``boolean``
    :default: ``true``
    :no-contents-entry:

    Water drips from the lowest leaves of trees, and from overhanging edges such as eaves, for a while after the rain stops, fewer and fewer as things dry.
    Edges drip while it rains too. Works whether or not particle rain is on. (*Added 1.21.1-0.4.7*)

.. confval:: weatherOptions.enableSnowOnSides
    :type: ``boolean``
    :default: ``true``
    :no-contents-entry:

    With particle snow on, snowflakes blown by the wind against the side of a wall, leaves or a tree trunk stick there for a moment before melting, as they
    do on the ground. Off, they only settle on top of things. (*Added 1.21.1-0.4.7*)

.. confval:: weatherOptions.enableWindowStreaks
    :type: ``boolean``
    :default: ``true``
    :no-contents-entry:

    With particle rain on, rain drops on the outside of glass blocks and panes cling, then run down in short rushes, leaving a wet trail, as real drops do.
    Where the glass ends over open air they drip off the edge; onto a sill or the wall below, they run off.
    Windows facing the wind and open to the sky get the most; windows indoors or under eaves stay dry. Which blocks count as windows is the
    ``dsurround:effects/windows`` block tag (glass blocks and panes), which a resource pack can add to. (*Added 1.21.1-0.4.7*)

.. confval:: weatherOptions.enableWindowFrost
    :type: ``boolean``
    :default: ``true``
    :no-contents-entry:

    When it is cold, frost grows on the outside of clear glass blocks and panes, in from the edges of the window and thickest along its bottom. It follows the
    temperature where the window is, Serene Seasons' included, and the time of day: it is thickest just before sunrise, and in a cool biome gone by the afternoon,
    while in the bitter cold some of it lasts all day. The sun melts it from the windows it shines on, east facing ones in the morning and west facing ones in the
    evening; north and south facing windows keep theirs. Glass under cover frosts less, and windows indoors stay clear. Frost creeps in over a couple of minutes,
    and melts a little faster. Works whether or not particle rain is on, and is not drawn while a shader pack is in use. Which blocks frost is the
    ``dsurround:effects/frosted_windows`` block tag, which a resource pack can add to; ``/dsweather frost`` sets the frost for testing (see
    :doc:`../commands/commands`). (*Added 1.21.1-0.4.7*)

.. confval:: weatherOptions.groundFogQuality
    :type: ``string``
    :default: ``"FANCY"``
    :no-contents-entry:

    *Experimental*. Mist lying low over the ground in swamps and eerie biomes, drifting with the wind. Possible selections are ``NONE``, ``FAST``, ``FANCY``, and ``FABULOUS``. ``NONE`` turns ground fog off; ``FAST`` draws it more coarsely and costs the least; ``FABULOUS`` draws it most finely and costs several times as much as ``FANCY``. Not used while a shader pack is in use.

.. confval:: weatherOptions.enableDynamicClouds
    :type: ``boolean``
    :default: ``true``
    :no-contents-entry:

    *Experimental*. Blocky clouds that change with the weather, in place of Minecraft's. On fair days scattered clouds build up through the afternoon and
    flatten out at night, with thin streaks high above; some days are cloudier than others, and wet biomes cloudier than dry ones. A storm closes them into a
    low deck, darker underneath the thicker it is, that towers in a thunderstorm; lightning lights them from inside. Every player in a world sees the same
    clouds. Not used while a shader pack is in use, when clouds are turned off in Minecraft's Video Settings, or in dimensions that draw their own clouds (see
    ``dynamicClouds`` in :doc:`../schemas/dimensions`); Minecraft's clouds are drawn then. See :doc:`../features`. (*Added 1.21.1-0.4.8*)

.. confval:: weatherOptions.cloudDistance
    :type: ``integer``
    :default: ``24``
    :no-contents-entry:

    How far the dynamic clouds reach, in chunks, from 8 to 32, whatever the render distance: farther shows more of the sky covered toward the horizon, and
    costs a little more. The fog of rain and dust storms still closes in on them, as it does on the land. (*Added 1.21.1-0.4.8*)

fogOptions
++++++++++

*Added 1.21.1-0.4.1*

.. code-block:: JSON

    {
      // Configuration options for fog effects
      "fogOptions": {
        // Enable/disable fog effects
        // Default: true
        "enableFogEffects": true,
        // Enable/disable morning fog effect
        // Default: true
        "enableMorningFog": true,
        // Enable/disable biome fog effect
        // Default: true
        "enableBiomeFog": true,
        // Enable/disable weather fog effect
        // Default: true
        "enableWeatherFog": true
      }
    }

.. confval:: fogOptions.enableFogEffects
    :type: ``boolean``
    :default: ``true``
    :no-contents-entry:

    Enable/disable fog effect processing

.. confval:: fogOptions.enableMorningFog
    :type: ``boolean``
    :default: ``true``
    :no-contents-entry:

    Enable/disable morning fog effect. Fog will start rolling in early in the AM, and eventually burn off later in the morning.

.. confval:: fogOptions.enableBiomeFog
    :type: ``boolean``
    :default: ``true``
    :no-contents-entry:

    Enable/disable biome fog effect. Some biomes will be configured as foggy, and when the player is in those biomes the density of fog will increase.

.. confval:: fogOptions.enableWeatherFog
    :type: ``boolean``
    :default: ``true``
    :no-contents-entry:

    Enable/disable generation of fog when raining/snowing.

auroraOptions
+++++++++++++

*Added 1.21.1-0.4.6*

.. code-block:: JSON

    {
      // Configuration options for auroras
      "auroraOptions": {
        // Enable/disable auroras: curtains of light in the night sky, on some nights, over cold biomes
        // Default: true
        "enableAuroras": true,
        // Percent of nights with an aurora
        // Range: 0 - 100, default: 33
        "chance": 33,
        // The most curtains of light an aurora can have
        // Range: 1 - 3, default: 3
        "maxBands": 3
      }
    }

.. confval:: auroraOptions.enableAuroras
    :type: ``boolean``
    :default: ``true``
    :no-contents-entry:

    Enables auroras: curtains of light in the night sky over cold biomes. Not every night has one, and they are not shown while a shader pack is in use.

.. confval:: auroraOptions.chance
    :type: ``integer``
    :default: ``33``
    :no-contents-entry:

    Percent of nights with an aurora. Every player in a world sees the same aurora on the same night. This value can be 0 - 100.

.. confval:: auroraOptions.maxBands
    :type: ``integer``
    :default: ``3``
    :no-contents-entry:

    The most curtains of light, side by side, that an aurora can have. This value can be 1 - 3.

musicManagerOptions
+++++++++++++++++++

*Added 1.21.1-0.4.3*

.. code-block:: JSON

    {
      // Configuration options for modded Music Manager
      "musicManagerOptions": {
        // Replace Minecraft's music manager with modded version
        // Default: true
        // Changes take effect after restarting Minecraft
        "replaceMusicManager": true,
        // Reduce the wait time between music plays by a percentage
        // Range: 0 - 100, default: 0
        "reduceWaitTime": 0
      }
    }

.. confval:: musicManagerOptions.replaceMusicManager
    :type: ``boolean``
    :default: ``true``
    :no-contents-entry:

    Replace Minecraft's music manager with modded version. This will enable the use of music manager commands (/dsmm). Requires a restart.

.. confval:: musicManagerOptions.reduceWaitTime
    :type: ``integer``
    :default: ``0``
    :no-contents-entry:

    Reduces the amount of time to wait between music plays. This value is a percentage, and is independent of the modded music manager. By default play interval will not be reduced.

diagnostics
+++++++++++

*Diagnostic Options* in the configuration menu. Before 1.21.1-0.4.8 this section was ``logging``, and also held :confval:`generalOptions.enableModUpdateChatMessage`
and :confval:`generalOptions.registerCommands`; values set there are carried over.

.. code-block:: JSON

    {
      // Configuration options for modifying diagnostic behavior
      "diagnostics": {
        // Enables/disables debug logging of the mod
        // Default: false
        "enableDebugLogging": false,
        // Bitmask for toggling various debug traces
        // Default: 0
        "traceMask": 0,
        // Enable/disable filtering display of tags in the diagnostics overlay
        // Default: true
        "filteredTagView": true,
        // Play your own Simple Voice Chat voice back to you, with enhanced sound processing, for testing
        // Default: false
        "voiceChatHearSelf": false,
        // Fixes for problems other mods cause, each of which can be turned off should it cause a problem of its own
        "guards": {
          // Put back the drawing state another mod's particle changes while Minecraft's particles are drawn, which draws them as squares, and draw that particle on its own. Turn off if it causes a problem
          // Default: true
          "repairParticleBatches": true
        }
      }
    }

.. confval:: diagnostics.enableDebugLogging
    :type: ``boolean``
    :default: ``false``
    :no-contents-entry:

    Turns on detailed diagnostic trace from the mod.

.. confval:: diagnostics.traceMask
    :type: ``integer``
    :default: ``0``
    :no-contents-entry:

    Set of bits that control which detail is desired. Only takes effect while :confval:`diagnostics.enableDebugLogging` is on. See :doc:`../troubleshooting/logs`
    for the values.

.. confval:: diagnostics.filteredTagView
    :type: ``boolean``
    :default: ``true``
    :no-contents-entry:

    Controls the amount of tag information to display within the mods diagnostics overlay.

.. confval:: diagnostics.voiceChatHearSelf
    :type: ``boolean``
    :default: ``false``
    :no-contents-entry:

    *Experimental*. For testing :confval:`enhancedSounds.enableVoiceChatProcessing` without a second player: plays the player's own Simple Voice Chat voice back to them, from their head, with reverb and the other effects. Only while the player is transmitting, and only while enhanced sound processing is on. Use headphones, or the speakers will feed back into the microphone. The playback is slightly delayed, which can sound like a short echo. Takes effect immediately. (*Added 1.21.1-0.4.7*)

Guards
~~~~~~

Fixes for problems other mods cause. Each can be turned off, should it ever cause a problem of its own. (*Added 1.21.1-0.4.8*)

.. confval:: diagnostics.guards.repairParticleBatches
    :type: ``boolean``
    :default: ``true``
    :no-contents-entry:

    *Added 1.21.1-0.4.8*. Minecraft draws all particles of a kind together, with the texture and blending set up for them. Some mods' particles change
    that texture or blending while they are added, so every particle drawn with them comes out wrong, often as squares (campfire smoke and waterfall foam
    are where it shows). With this on, Dynamic Surroundings puts the state back before the particles are drawn, names the particle responsible in the log
    once, and from then on draws that particle on its own so it looks right too. Turn it off if it ever causes a problem; the log line is still worth
    reporting to the mod named.

Moved and Removed Settings
++++++++++++++++++++++++++

Settings from earlier versions that have moved or no longer exist. Values of moved settings are carried over automatically when an older
``dsurround.json`` is loaded.

.. list-table::
    :widths: auto
    :align: center
    :header-rows: 1

    *   - Setting
        - Status
    *   - ``logging``
        - Renamed ``diagnostics`` in 1.21.1-0.4.8; ``logging.enableDebugLogging`` is now :confval:`diagnostics.enableDebugLogging`, and so on
    *   - ``logging.enableModUpdateChatMessage``
        - Moved to :confval:`generalOptions.enableModUpdateChatMessage` in 1.21.1-0.4.8
    *   - ``logging.registerCommands``
        - Moved to :confval:`generalOptions.registerCommands` in 1.21.1-0.4.8
    *   - ``soundOptions.allowScarySounds``
        - Moved to :confval:`scaryContent.allowScaryContent` in 1.21.1-0.4.8, where it also covers the lightning
    *   - ``otherOptions.playRandomSoundOnStartup``
        - Removed in 1.21.1-0.4.8, with the random sound played when the game finishes loading
    *   - ``entityEffects.enableToolbarBlockSounds``
        - Removed in 1.21.1-0.4.8
    *   - ``enhancedSounds.enableMonoConversion``
        - Removed in 1.21.1-0.4.6
    *   - ``compassAndClockOptions.enableCompass``
        - Replaced by ``NONE`` in :confval:`compassAndClockOptions.compassStyle` in 1.21.1-0.4.7
    *   - ``compassAndClockOptions.enableClock``
        - Replaced by ``NONE`` in :confval:`compassAndClockOptions.clockStyle` in 1.21.1-0.4.7
    *   - ``blockEffects.flameJetEnabled``
        - Moved to :confval:`flameJetOptions.enableFlameJets` in 1.21.1-0.4.7
    *   - ``blockEffects.firefliesEnabled``
        - Moved to :confval:`fireflyOptions.enableFireflies` in 1.21.1-0.4.6
    *   - ``blockEffects.waterfallsEnabled``
        - Moved to :confval:`waterfallOptions.enableWaterfalls` in 1.21.1-0.4.6
    *   - ``blockEffects.enableWaterfallSounds``
        - Moved to :confval:`waterfallOptions.enableSounds` in 1.21.1-0.4.6
    *   - ``blockEffects.enableWaterfallParticles``
        - Moved to :confval:`waterfallOptions.enableParticles` in 1.21.1-0.4.6
    *   - ``footstepAccents.enableLeafAccents``
        - Removed in 1.21.1-0.4.2
