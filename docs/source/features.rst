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
* :confval:`scaryContent.allowScaryContent` turns off sounds that may frighten younger players, such as wolves and monster growls and the heartbeat at low health, as well as the lightning.

Resource pack authors can add or change biome sounds; see :doc:`schemas/biomes`.

Block Sounds
~~~~~~~~~~~~

Some blocks make a sound now and then when the player is near: ice cracks, in the Nether soul sand laughs and nether bricks breathe, and powered redstone crackles.
Frogs croak from lily pads, with the odd bullfrog call, twice as often at night as by day, but not while the player is inside or when it is cold enough for water to
freeze (*back from older versions in 1.21.1-0.4.8*). Lily pads from Biomes O' Plenty, Twilight Forest, Oh The Biomes We've Gone, and Regions Unexplored croak too;
the ``dsurround:effects/frog_croaks`` tag sets which blocks do (see :doc:`packs/tagging`). Resource pack authors can add or change block sounds; see
:doc:`schemas/blocks` and the lily pad example in :doc:`scripting/examples`.

Player Sounds
~~~~~~~~~~~~~

A hungry player's stomach grumbles now and then, when their food level is at 4 or less or they have the Hunger effect. When their health is at 30% or less
(outside creative mode), their heart pounds until they heal (*back from older versions in 1.21.1-0.4.8*); as it can be unsettling, it is a scary sound,
turned off with :confval:`scaryContent.allowScaryContent`. Both have subtitles. With :confval:`entityEffects.enableJumpSound` on, the player takes a
breath when they jump, heard by them only (*back from older versions in 1.21.1-0.4.8*; off by default). Resource pack authors can change
them in the ``@player`` biome rule (see :doc:`schemas/biomes`); see the examples in :doc:`scripting/examples`.

Enhanced Sound Processing
~~~~~~~~~~~~~~~~~~~~~~~~~

Sounds playing in the world get reverb based on the space around them and the blocks it is made of, so a large stone cave echoes and a small wooden room
does not. Optionally, sounds behind blocks can be muffled.

* :confval:`enhancedSounds.enableEnhancedSounds` turns the feature on or off.
* :confval:`enhancedSounds.enableOcclusionProcessing` turns on muffling of sounds behind blocks. It is off by default as it takes more processing.

*Voice chat added 1.21.1-0.4.7, experimental*: with `Simple Voice Chat <https://modrinth.com/plugin/simple-voice-chat>`_ installed, the voices of nearby players are processed
the same way, so a player talking in a cave echoes and, with occlusion on, a player behind a wall sounds muffled. Group chat, which is not positional, plays as it is.

* :confval:`enhancedSounds.enableVoiceChatProcessing` turns this on or off.
* :confval:`diagnostics.voiceChatHearSelf` plays your own voice back to you, for hearing the effect without a second player.

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

Arrows fired from a bow, by players and skeletons, are heard with the bowstring's release in place of Minecraft's sound (*back from older versions in
1.21.1-0.4.8*); :confval:`soundOptions.remapSounds` turns it off along with the other remapped sounds.

Thunder
~~~~~~~

Minecraft's thunder is replaced with Dynamic Surroundings' own. See :confval:`soundOptions.replaceThunderSounds`. Lightning in the sky has thunder of its own;
see `Lightning`_.

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
Rain, snow, and dust blown in under an overhang drift a little way in, out of the wind, and fade, rather than stopping at the roof's edge; snowflakes that reach
the ground beneath lie there, and rain splashes on a porch floor (*added 1.21.1-0.4.8*). Rain and snow also stop on top of blocks from other mods that
Minecraft's own rain falls through, such as Mekanism's energy cube (*1.21.1-0.4.8*).
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

Lightning
~~~~~~~~~

*Added 1.21.1-0.4.8*

Lightning branches and forks, more the stronger the thunderstorm: a weak storm's bolts have a few branches, the strongest's many, forking again and again.
Each flash starts with a faint leader feeling its way down, then strokes that light the whole channel at once and flicker as they die away; later strokes light
the main channel again but barely touch the branches, as real lightning does. Minecraft's lightning bolts are drawn this way, each shaped from the bolt itself,
so every player sees the same one.

Through a thunderstorm the sky has lightning of its own, mostly from upwind, where the storm is coming from: bolts to the ground, spider lightning crawling
under the cloud base, and flashes hidden in the cloud that light it up in patches, the light moving about inside it from one stroke to the next. Each is
followed by its thunder, later the farther away it is (about a second for every 343 blocks), and quieter and lower when far off. One close by lights up the
sky, as Minecraft's own bolts do. With the `Clouds`_ on, a flash lights the clouds themselves from inside: their undersides where a bolt leaves them, the
towers it hides in, and not the gaps between. Far strikes are dimmer than near ones, the more so the thicker the weather between: rain hides a distant
storm's flashes a good deal more than clear air does.

* :confval:`scaryContent.enableLightning` turns the lightning off, as does :confval:`scaryContent.allowScaryContent`; Minecraft's own bolts are drawn then.
* With Minecraft's *Hide Lightning Flashes* accessibility option on, there is no lightning in the sky, and bolts strike once without flickering.

The lightning is not drawn while a shader pack is in use. ``/dsweather lightning`` strikes ahead of the player, to see how it looks; see
:doc:`commands/commands`.

Clouds
~~~~~~

*Added 1.21.1-0.4.8, experimental*

Blocky clouds that change with the weather take the place of Minecraft's. On fair days, scattered clouds build up into stepped towers through the afternoon
and flatten out at night, with thin streaks high above; some days are cloudier than others. They are cloudier over wet biomes than dry ones, so they build
over jungles and swamps and thin out over deserts as they drift. A storm closes them into a low deck that lowers and thickens with its strength, darker
underneath the thicker it is, and a thunderstorm's towers rise far above it. Lightning lights them from inside (see `Lightning`_).

They change a little at a time, a cloud fading in or out rather than appearing or vanishing. Every player in a world sees the same clouds, carried by the
wind up high, which follows the day's wind. Far off they fade out into the fog: in rain the deck overhead stays dark while the distance turns to haze, and a
dust storm hides all but what is right overhead.

* :confval:`weatherOptions.enableDynamicClouds` turns them on or off; Minecraft's own clouds are drawn when they are off.
* :confval:`weatherOptions.cloudDistance` sets how far they reach, whatever the render distance.

They are not drawn while a shader pack is in use, when clouds are turned off in Minecraft's Video Settings, or in dimensions that draw their own clouds
(see ``dynamicClouds`` in :doc:`schemas/dimensions`). ``/dsweather clouds`` holds how much of the sky they cover, to see how they look; see
:doc:`commands/commands`.

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

Block effects such as waterfalls, steam, and flame jets are found within :confval:`blockEffects.blockEffectRange` of the player. *Since 1.21.1-0.4.8* that range
is a sphere, and the nearest blocks are found first, so the effects close by appear first after arriving somewhere new. Past 32 blocks, effects show farther away than
Minecraft shows particles, at more cost.

Random block effects, such as fireflies, flame jets, bubbles, and the sounds some blocks make, come from blocks picked at random around the player each tick, as
Minecraft picks blocks for its own particles: more often close by, less often farther away, mostly within 32 blocks. Sounds keep that spread. *Since
1.21.1-0.4.8*, with the range set past 32 blocks, effects (not sounds) also come from past 32 blocks, thinning out evenly toward the edge of the range.

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

Animals breathe too (*added 1.21.1-0.4.8*): cows, mooshrooms, sheep, goats, pigs, horses, donkeys, mules, llamas, camels, wolves, foxes, cats, ocelots,
polar bears, pandas, sniffers, armadillos, hoglins, and ravagers. The breath comes from the mouth, out in front of the body, and follows the head as it turns
and nods; bigger animals breathe bigger puffs. An animal with its head down or out of the way (a sheep eating grass, a goat about to ram, a rearing horse, a
sleeping fox) holds its breath until it's done. Only animals within 16 blocks of the player breathe. See :confval:`entityEffects.enableAnimalBreath`.

Burning Mobs
~~~~~~~~~~~~

*Added 1.21.1-0.4.8*

A burning mob is wreathed in flames like a flame jet's, with sparks and smoke, in place of Minecraft's two flat sheets of fire. The fire fits the mob: more flames
for a bigger body and larger ones for a broader body. The flames keep up with a running mob, burn on through its death until the body is gone, and in lava only
rise from the part above the surface. Each casts one flickering light on the area around it (:confval:`flameJetOptions.enableLight`), unless LambDynamicLights or RyoamicLights is
installed, as it already lights burning mobs. Mobs farther away get fewer flames, and a crowd of burning mobs shares a budget, so undead burning at dawn thin out evenly.

Minecraft's own fire is kept beyond :confval:`entityEffects.entityEffectRange`, with Particles set to Minimal, while a shader pack is in use, and for the player's own
body in first person. See :confval:`entityEffects.enableBurningEffect`. Mobs tagged ``dsurround:effects/vanilla_fire`` keep Minecraft's fire; see :doc:`packs/tagging`.

Death Mist
~~~~~~~~~~

*Added 1.21.1-0.4.8*

When a mob's body vanishes at the end of its death, it leaves a cloud of dark mist that drifts out and fades, in place of Minecraft's white puffs. Minecraft's puffs
are kept with Particles set to Minimal. See :confval:`entityEffects.enableDeathPuffs`.

Damage Pop-offs
~~~~~~~~~~~~~~~

*Added 1.21.1-0.4.8, from older versions*

When a mob's or player's health changes, a number pops off above it: red for damage, green for healing. A heavy blow, 40% or more of the mob's health, also gets a
comic book word in gold over the number, such as KAPOW! The killing blow shows too. Nothing pops off the player's own body in first person. See
:confval:`entityEffects.enableDamagePopoffs` and :confval:`entityEffects.showCritWords`. Mobs tagged ``dsurround:effects/no_health_popoffs`` (armor stands, by
default) get none.

Footprints
~~~~~~~~~~

*Added 1.21.1-0.4.8*

Players and mobs leave footprints in soft ground: dirt, grass, sand, gravel, snow, mud, soul sand, and blocks tagged ``dsurround:effects/footprints``. A print is left
for each foot as it comes down, and both on landing from a jump. Players' prints are square by default (:confval:`entityEffects.footprintStyle`); mobs' fit their feet,
set by tags: square for humanoids such as zombies and villagers, paws for wolves, cats, foxes and bears, hooves for horses, cows, sheep, pigs and goats, and bird tracks
for chickens and parrots. Smaller bodies leave smaller prints, closer together; bears' prints are larger and skeletons' smaller
than their size alone gives (the ``footprints/large`` and ``footprints/small`` tags).

Prints fade after about 10 seconds, or a minute in snow, and wash away faster where rain falls on them in the open. They go when the ground under them changes.
No prints are left while sneaking, swimming or riding, by invisible mobs, with Particles set to Minimal, or while a shader pack is in use. See
:confval:`entityEffects.enableFootprints`, and :doc:`packs/tagging` for the tags.

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
* **Guards** (*added 1.21.1-0.4.8*): fixes for problems other mods cause, each of which can be turned off. The first repairs particles drawn as squares when
  another mod's particle spoils Minecraft's particle drawing, and names that particle in the log; see :confval:`diagnostics.guards.repairParticleBatches` and
  :doc:`troubleshooting/troubleshooting`.
