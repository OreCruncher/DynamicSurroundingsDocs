Troubleshooting
===============

When something goes wrong, the fastest way to a fix is a report with enough information to see what happened without a lot of back and forth. Problems are
reported on the `Dynamic Surroundings issue tracker <https://github.com/OreCruncher/DynamicSurroundingsFabric/issues>`_.

What to Include in a Report
---------------------------

* **The Dynamic Surroundings version and mod loader.** The jar name has both, such as ``dynamicsurroundings-fabric-1.21.1-0.4.7``. ``/dsversion`` checks
  whether a newer version is available; the problem may already be fixed.
* **The modpack, or a list of mods.** Many problems only happen alongside another mod. A link to the modpack is enough.
* **What happened, and how to make it happen again.** Where the player was, what they were doing, and whether it happens every time.
* **The log from the session where the problem happened.** Always include this, even when the problem doesn't seem related to anything logged. See :doc:`logs`.
* **The crash report**, if the game crashed. See :doc:`logs`.
* **A flight recording**, for poor performance (stutter, lag spikes, low frame rate), the game freezing, or a strange interaction with another mod.
  ``/dsprofile`` makes one in the game, ready to attach. See :doc:`jfr`.

Before Reporting
----------------

* Check the list of mods that replace a Dynamic Surroundings feature in :doc:`../installation`. When one is installed, Dynamic Surroundings turns its own version
  off on purpose. ``/dsconflicts`` lists what has been turned off in the current session, and which mod it was turned off for.
* If the problem might be caused by another mod, check whether it still happens with that mod removed. Say so in the report either way.

Particles Drawn as Squares
--------------------------

Smoke from campfires, waterfall foam, and other particles that show as white or colored squares are usually drawn with the wrong texture because of
another mod's particle: Minecraft draws all particles of a kind together, and a particle that changes the texture or blending while they are being added
spoils the rest. *Since 1.21.1-0.4.8* Dynamic Surroundings puts the state back before they are drawn and draws the particle responsible on its own, and the log
says which particle it was, once, in a line starting ``Particle <class> changes the``. The start of the class name tells which mod it is from; that mod is
where the fix belongs. One known case is the Rainbows mod, whose rainbow binds its own texture this way. The repair is :confval:`diagnostics.guards.repairParticleBatches`, under *Guards* in *Diagnostic Options*, if it ever needs turning off.

The Diagnostic Overlay
----------------------

Dynamic Surroundings has an overlay that shows what it is doing, including how long its work takes each tick. A screenshot of it while the problem is happening
can help. Its key is not bound by default: bind *Diagnostic Overlay* under *Dynamic Surroundings* in the *Key Binds* options. Each press shows the next view, in
the order debug information, biome information, and the effects being tracked in the world, then turns the overlay off.

.. toctree::
    :titlesonly:

    logs
    jfr
