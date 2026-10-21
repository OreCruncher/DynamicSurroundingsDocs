Features
========

Dynamic Surroundings adds sound and visual effects to Minecraft while staying close to the Vanilla feel of the game. It is 100% client side: it can be added to any
mod pack, and works when playing on a Vanilla server. Almost every feature can be turned off or adjusted; the settings for each are linked below.
See :doc:`config/modconfiguration` for all the settings, and :doc:`videos` to see many of these features in action.

Sound
-----

Biome Sounds
~~~~~~~~~~~~

Each biome has its own atmosphere: wind over mountains and deserts, birds and insects in forests, crickets at night, and the rumble of caves underground.
Sounds from the biomes around the player are blended by how much of the area each covers, so moving between biomes changes the sound gradually. Windy biome
sounds rise and fall with the simulated wind. Minecraft biomes and many modded biomes are supported.

* :confval:`soundOptions.ambientVolumeScaling` adjusts the volume of these sounds.
* :confval:`soundOptions.allowScarySounds` turns off sounds that may frighten younger players, such as wolves and monster growls.

Resource pack authors can add or change biome sounds; see :doc:`schemas/biomes`.

Enhanced Sound Processing
~~~~~~~~~~~~~~~~~~~~~~~~~

Sounds playing in the world get reverb based on the space around them and the blocks it is made of, so a large stone cave echoes and a small wooden room
does not. Optionally, sounds behind blocks can be muffled.

* :confval:`enhancedSounds.enableEnhancedSounds` turns the feature on or off.
* :confval:`enhancedSounds.enableOcclusionProcessing` turns on muffling of sounds behind blocks. It is off by default as it takes more processing.

*Voice chat added 1.21.1-0.4.7, experimental*: with `Simple Voice Chat <https://modrinth.com/plugin/simple-voice-chat>`_ installed, the voices of nearby players are processed
the same way, so a player talking in a cave echoes and, with occlusion on, a player behind a wall sounds muffled. Group chat, which is not positional, plays as it is.

* :confval:`enhancedSounds.enableVoiceChatProcessing` turns this on or off.
* :confval:`logging.voiceChatHearSelf` plays your own voice back to you, for hearing the effect without a second player.

Enhanced sound processing is turned off when Sound Physics Remastered is installed, as it provides its own, for voices too.

Footsteps and Movement
~~~~~~~~~~~~~~~~~~~~~~

Step sounds are replaced with more varied ones based on the block being walked on, for the player as well as other players and humanoid mobs. On top of the
step sound, extra sounds are added: armor rattling, splashes when walking in the rain or on lily pads, squeaking wooden floors, and rustling when walking
through tall grass, flowers, and crops.

* :confval:`soundOptions.remapSounds` controls the replacement step sounds.
* :confval:`footstepAccents.enableAccents` controls the extra sounds, with a setting for each kind.
* :confval:`entityEffects.enableBrushStepEffect` controls the rustling through plants.

For more detailed footstep sounds, Dynamic Surroundings works alongside the Presence Footsteps mod. With it installed, the wet surface accents and the rustling
through plants are turned off, as its own footstep sounds take their place.

Item Sounds
~~~~~~~~~~~

Swinging a sword or axe, drawing a bow, and switching items on the hotbar each make a sound fitting the item.

* :confval:`entityEffects.enableSwingEffect`, :confval:`entityEffects.enableBowPull`, and :confval:`entityEffects.enablePlayerToolbarEffect` control these.

Thunder
~~~~~~~

Minecraft's thunder is replaced with Dynamic Surroundings' own. See :confval:`soundOptions.replaceThunderSounds`.

Individual Sound Control
~~~~~~~~~~~~~~~~~~~~~~~~

Any sound in the game can be blocked, culled (so many copies playing at once become one, useful around animal farms), or made louder or quieter. See
:doc:`config/individual_sound_config`.

Music
~~~~~

Biomes can have several pieces of music to choose from, with conditions such as the time of day or season, and the wait between tracks can be shortened.
See :doc:`misc/music`.

Weather and Atmosphere
----------------------

Storms
~~~~~~

*Added 1.21.1-0.4.7*

Each storm has its own strength, from a light drizzle to a downpour, that rises and falls as the storm goes on. Rain and snow are drawn as individual drops that
slant and drift with the wind, with sleet where rain and snow meet. In deserts and badlands, a storm blows dust along the ground instead of rain. Rain sounds
follow the storm's strength, from a soft patter to a roar. Every player in a world sees the same storm on the same day.

Where rain soaks into soft ground it leaves dark damp spots that dry. On windows facing the wind, drops cling to the glass, then run down it in short
rushes, leaving a wet trail. Snowflakes lie where they land, or stick where the wind blows them against a wall or trunk, for a moment before melting away.
For a while after the rain stops, water keeps dripping from the lowest leaves of trees and from overhanging edges such as eaves, less and less as things dry.
In the cold, frost grows on the outside of clear glass windows, in from their edges, thickest before sunrise; the sun melts it from east facing windows in the
morning and west facing ones in the evening.

* :confval:`weatherOptions.enableStormSimulation` turns storm strength on or off.
* :confval:`weatherOptions.enableParticlePrecipitation`, :confval:`weatherOptions.enableDustStorms`, and :confval:`weatherOptions.enableStormSounds` control the drops, dust, and sound.
* :confval:`weatherOptions.enableAfterRainDrips` controls the drips after rain, :confval:`weatherOptions.enableSnowOnSides` whether snow sticks to walls
  and trunks, :confval:`weatherOptions.enableWindowStreaks` the rain on windows, and :confval:`weatherOptions.enableWindowFrost` the frost on them.
* :confval:`weatherOptions.precipitationDensity`, :confval:`weatherOptions.precipitationRange`, :confval:`weatherOptions.rainDropScale`,
  :confval:`weatherOptions.snowflakeScale`, and :confval:`weatherOptions.rainTint` change how much rain and snow there is, how far it reaches, and how it
  looks, including how blue the rain is.

The particle rain and snow are not used while a shader pack is in use, or when the Particle Rain or Simple Weather mod is installed. The ``/dsweather`` command can
be used to see how storms of a given strength look; see :doc:`commands/commands`.

Wind
~~~~

*Added 1.21.1-0.4.7*

A wind blows that changes speed and direction over time, and gusts. It drifts the rain, snow, and dust, as well as mist, steam, smoke, and flames, and makes
windy biome sounds louder or quieter. Out in the open it also carries some particles from Minecraft and other mods, such as campfire smoke, ash, falling cherry
leaves, and spores; which ones is set by a tag (see :doc:`packs/tagging`). Dimensions without a sky, such as the Nether, have no wind.

Ground Fog
~~~~~~~~~~

*Added 1.21.1-0.4.7, experimental*

Mist lies low over the ground in swamps and eerie biomes such as the Dark Forest, drifting with the wind. It is thickest between midnight and morning, and heavy
rain thins it out. See :confval:`weatherOptions.groundFogQuality` to change its quality or turn it off.

Fog
~~~

The sky fog changes with the time of day, the biome, and the weather: morning fog that burns off as the day goes on, thicker fog in foggy biomes, and fog
during rain and snow. See :confval:`fogOptions.enableFogEffects`.

Auroras
~~~~~~~

*Added 1.21.1-0.4.6*

On some nights, curtains of light shimmer in the northern sky over cold biomes. See :confval:`auroraOptions.enableAuroras`. Auroras are not shown while a shader
pack is in use.

Block Effects
-------------

Waterfalls
~~~~~~~~~~

Water falling from a height splashes and roars where it lands, throwing up mist. Foam forms on the water and is carried along by the current, and water stepping
down a single block makes a gentle sound. Taller waterfalls are louder and splash more. See :confval:`waterfallOptions.enableWaterfalls`.

Steam and Flame Jets
~~~~~~~~~~~~~~~~~~~~

Water next to a hot block such as lava or magma gives off steam, and lava and fully grown nether wart send up jets of flame that light up the area around
them. See :confval:`blockEffects.steamColumnEnabled` and :confval:`flameJetOptions.enableFlameJets`.

Fireflies
~~~~~~~~~

Fireflies blink around flowers at night, with a soft glow that lights up the plants around them. See :confval:`fireflyOptions.enableFireflies`.

Water Ripples and Bubbles
~~~~~~~~~~~~~~~~~~~~~~~~~

Rain landing on water makes ripples, and bubble columns rise underwater. See :confval:`blockEffects.waterRippleStyle` and :confval:`blockEffects.bubbleColumnEnabled`.

Player and Entity Effects
-------------------------

Frost Breath
~~~~~~~~~~~~

Players, villagers, and raiders breathe visible puffs in cold biomes, and give off bubbles underwater. See :confval:`entityEffects.enableBreathEffect`.

Compass and Clock
~~~~~~~~~~~~~~~~~

Holding a compass shows a compass on screen, and holding a clock (or looking at one in an item frame) shows the time. The compass spins in dimensions where compasses do not work.
The compass is either a band above the crosshair that slides with the player's heading, or (*added 1.21.1-0.4.7*) a compass rose laid flat in front of the player that turns with it.

The clock is shown as text above the hot bar, giving the day, the time and the season, or (*added 1.21.1-0.4.7*) as a well loved pocket watch above the crosshair, styled after
Minecraft's clock. Its hands tick from minute to minute. A window under XII shows day or night, as Minecraft's clock does, so noon can be told from midnight, and a window above VI
shows the season when Serene Seasons is installed, or the moon's phase without it. Both windows show discs that turn clockwise: the sun crosses the day window from left to
right, rising at 6 AM and setting at 6 PM, while each season, or moon phase, enters the lower window from the right and leaves to the left. Holding a compass as well puts the
watch beside the compass, on the side of the hand holding the clock.

The compass and pocket watch can instead be shown in a side or corner of the screen whenever one is in the hot bar or off hand, without having to hold it
(*added 1.21.1-0.4.7*). See :confval:`compassAndClockOptions.showInMargin`.

See :confval:`compassAndClockOptions.compassStyle`, :confval:`compassAndClockOptions.clockStyle`, :confval:`compassAndClockOptions.showInMargin`,
:confval:`compassAndClockOptions.marginPosition` and :confval:`compassAndClockOptions.scale`. Resource packs can replace the
compass and pocket watch textures; see :doc:`packs/overlay_textures`.

Light Level Overlay
~~~~~~~~~~~~~~~~~~~

*Added 1.21.1-0.4.7*

Bind the *Light Level Overlay* key (under *Dynamic Surroundings* in the controls; it starts unbound) to show the light level on the blocks around the player that a
monster could stand on. Press it again to turn it off. Each number lies flat on its block, turned to read upright whichever way the player faces, and is colored by
whether monsters can spawn there:

* **Red**: dark enough for monsters to spawn now.
* **Yellow**: safe for now, but monsters can spawn once the sky darkens, at night or in a thunderstorm.
* **Green**: too bright for monsters.
* **Aqua**: monsters can never spawn there, however dark, such as on glass, slabs, or leaves.

Spawning follows the dimension's own rules, as Minecraft does: in the Overworld any block light at all keeps monsters away, and otherwise they spawn where the light
is 7 or less; in the Nether, block light of 7 or less lets them spawn. A legend in the bottom right corner of the screen says what the colors mean. It moves up out of the
way of the compass and pocket watch when those are shown in that corner, and above the hot bar on a narrow screen.

The numbers are drawn with the game's font, so a resource pack that changes the font changes them too. The overlay turns off when leaving a world.

See :confval:`lightLevelOptions.mode`, :confval:`lightLevelOptions.colors`, :confval:`lightLevelOptions.range`, :confval:`lightLevelOptions.hideSafe` and
:confval:`lightLevelOptions.showLegend`.

Other
-----

* **Seasons**: with Serene Seasons installed, the season changes temperature dependent effects such as frost breath and biome sounds, and is available to scripts.
* **Vanilla servers**: Dynamic Surroundings works when connected to a Vanilla server, as everything it does is on the client.
* **Sound credits**: the *Sound Credit* button in Minecraft's *Music & Sounds* options lists credit and license information for the mod's sounds.
* **Diagnostic overlay**: bind the *Diagnostic Overlay* key (under *Dynamic Surroundings* in the controls) to show information about the player's biome and the
  effects around them, without crowding Minecraft's F3 screen. With Simple Voice Chat installed, it also shows whether voices are processed and how many are
  playing.
* **Commands**: client side commands for reloading configuration, testing scripts, and dumping configuration. See :doc:`commands/commands`.
