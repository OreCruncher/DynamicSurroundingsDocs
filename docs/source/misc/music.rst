Music
=====

In Vanilla, Minecraft makes it's music selection based on biome. A mod or resource pack author would configure a property for background music. A player notices this
this mostly in the Nether dimension where each biome has a different theme.

Dynamic Surroundings modifies the biome property, enabling the ability of choosing from mutlple different selections. Further, these selections can have criteria that
evaluates whether a given piece of music can play. For example, a music selection can be configured to be eligible for play at specific times of day, certain biomes,
or any other criteria that can be made.

If there happens to be background music configured for a biome *natively*, that music is also added to the possible list of candidates.

Any music that is eligible for play are gathered into a weight table. A random selection is made from this table, and the result is what is provided to the music
manager for play.

A command that can be useful during pack development is ``/dsmm reset``. This command will force a reset of the music manager. This will cause the music manager to
stop playing the current piece of music, and to set the internal timers so that another music selection will be made in the very near future. The command could also
be used during game play to change the current music.

For more information on adding music in a resource pack, see :doc:`../schemas/acoustic`.