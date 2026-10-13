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

Footsteps and Movement
~~~~~~~~~~~~~~~~~~~~~~

Step sounds are replaced with more varied ones based on the block being walked on, for the player as well as other players and humanoid mobs. On top of the
step sound, extra sounds are added: armor rattling, splashes when walking in the rain or on lily pads, squeaking wooden floors, and rustling when walking
through tall grass, flowers, and crops.

* :confval:`soundOptions.remapSounds` controls the replacement step sounds.
* :confval:`footstepAccents.enableAccents` controls the extra sounds, with a setting for each kind.
* :confval:`entityEffects.enableBrushStepEffect` controls the rustling through plants.

For more detailed footstep sounds, Dynamic Surroundings works alongside the Presence Footsteps mod.

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

* :confval:`weatherOptions.enableStormSimulation` turns storm strength on or off.
* :confval:`weatherOptions.enableParticlePrecipitation`, :confval:`weatherOptions.enableDustStorms`, and :confval:`weatherOptions.enableStormSounds` control the drops, dust, and sound.

The particle rain and snow are not used while a shader pack is in use, or when the Particle Rain or Simple Weather mod is installed. The ``/dsweather`` command can
be used to see how storms of a given strength look; see :doc:`commands/commands`.

Wind
~~~~

*Added 1.21.1-0.4.7*

A wind blows that changes speed and direction over time, and gusts. It drifts the rain, snow, and dust, as well as mist, steam, smoke, and flames, and makes
windy biome sounds louder or quieter. Dimensions without a sky, such as the Nether, have no wind.

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

Holding a compass shows a compass on screen, and holding a clock shows the time of day and the season. The compass spins in dimensions where compasses do not work.
See :confval:`compassAndClockOptions.enableCompass` and :confval:`compassAndClockOptions.enableClock`.

Other
-----

* **Seasons**: with Serene Seasons installed, the season changes temperature dependent effects such as frost breath and biome sounds, and is available to scripts.
* **Vanilla servers**: Dynamic Surroundings works when connected to a Vanilla server, as everything it does is on the client.
* **Sound credits**: the *Sound Credit* button in Minecraft's *Music & Sounds* options lists credit and license information for the mod's sounds.
* **Diagnostic overlay**: bind the *Diagnostic Overlay* key (under *Dynamic Surroundings* in the controls) to show information about the player's biome and the
  effects around them, without crowding Minecraft's F3 screen.
* **Commands**: client side commands for reloading configuration, testing scripts, and dumping configuration. See :doc:`commands/commands`.
