Flight Recordings
=================

Some problems don't leave anything in the log: stutter, lag spikes, a low frame rate, or a strange interaction with another mod. For these, a Java Flight
Recorder (JFR) recording is the most useful thing to include in a report. It records what every part of the game was doing, including other mods, so it shows
where the time went and who was responsible.

Dynamic Surroundings can make the recording itself with the ``/dsprofile`` command. It needs nothing installed or added to the launcher, it leaves personal
information out of the recording (see :ref:`jfr-privacy`), and it saves the recording zipped, ready to attach to an issue. (*Added 1.21.1-0.4.7*)

Recording with /dsprofile
-------------------------

1. Join a world, go to where the problem shows, and run ``/dsprofile``.
2. A note at the top of the screen counts down to the start, then shows the time left while it records. Keep playing, and make the problem happen while it
   records. Recording adds little overhead, so the game plays normally.
3. When it is done, chat says where the recording was saved, with the frame rate and how long Dynamic Surroundings' effects took to draw. Click the file's name
   to open it.
4. Attach the ``.zip`` file to the issue, with ``logs/latest.log`` from the same session. See :ref:`jfr-sharing`.

By default it records two minutes of the game as it is. To record for another length, name a scene and give the number of seconds, from 10 to 600:

.. code-block:: text
    :class: copybutton

    /dsprofile general 300

Scenes
~~~~~~

A scene sets up one of Dynamic Surroundings' effects at its heaviest before recording, so it can be measured on its own. Use one when asked to, or when that
effect seems to be what is slow. Unless a scene is named, ``general`` is recorded.

.. list-table::
    :widths: auto
    :align: center
    :header-rows: 1

    *   - Scene
        - What it shows
        - While it records
    *   - ``general``
        - The game as it is. Nothing is changed.
        - Play as usual, or show what seems slow.
    *   - ``ground_fog``
        - Ground fog at its thickest, everywhere. In single player it also clears the weather.
        - Look across open ground and keep still.
    *   - ``weather``
        - A thunderstorm at full strength. In single player it also starts the thunderstorm.
        - Look around, out in the open, and keep still.
    *   - ``frost``
        - The most frost on every window.
        - Stand where windows fill the view and keep still.

A scene holds its effect the way ``/dsweather`` does (see :doc:`../commands/commands`), and puts it back as it was when the recording is done. Recording starts
a few seconds after the command, so the effect can fade in first.

The ``ground_fog`` and ``weather`` scenes also need the right weather. In single player they set it with ``/weather`` and stop the weather from changing with
``/gamerule doWeatherCycle false``; chat lists what was sent. These are world settings, so they are not put back afterwards: run
``/gamerule doWeatherCycle true`` to let the weather change again. They need cheats to be allowed in the world. On a server nothing is sent, and chat says
what the scene would have needed; the ground fog scene still works, and the weather scene shows its storm once it rains.

Where Recordings Are Saved
~~~~~~~~~~~~~~~~~~~~~~~~~~

Recordings are saved in the game directory, in ``config/dsurround/profiles``, named for the scene and the time they were made, such as
``dsurround-general-20261017-114439.zip``. Each ``.zip`` file holds one recording (``.jfr``). Only the 10 newest are kept; older ones are deleted when the game
starts. See :doc:`logs` for how to open the game directory.

If ``/dsprofile`` says profiling isn't available, the game's Java does not include Flight Recorder. Most do; see :ref:`jfr-other-ways` for another way.

.. _jfr-sharing:

Sharing the Recording
---------------------

Attach the ``.zip`` file to the issue as it is; GitHub accepts ``.zip`` files but not ``.jfr`` files. Include ``logs/latest.log`` from the same session, the
scene used, and what happened while it recorded.

.. _jfr-privacy:

Privacy
-------

.. note::

    Recordings made with ``/dsprofile`` are meant to be shared, so personal information is left out of them. They do not include:

    * The command line the game was started with, which holds the Minecraft account's name, its ID, and its access token.
    * Environment variables, Java's system and security properties, and the computer's other running processes.
    * Network addresses and traffic, including the server's address, and certificates.
    * Which files were read or written, the folders that libraries and Java agents were loaded from, and the text of errors, which often holds folder paths.
    * The operating system's full description, which on some systems holds the computer's name.

    The path of the home folder is redacted wherever it appears, so a folder such as ``C:\Users\Alex`` reads as ``C:\Users\****``.

    What a recording does have:

    * The processor, memory, graphics card and its driver version, operating system and its version, and Java version.
    * The Dynamic Surroundings version, the mod loader, how many mods are installed, the graphics setting, render distance, and whether a shader pack is in use.
    * What each part of the game, and each mod, was doing and how long it took. The names of the mods' code show which mods are installed.
    * The folder paths of the game and its mods, with the home folder redacted. A game installed outside the home folder, such as in ``D:\Games``, keeps
      that path.

.. _jfr-other-ways:

Other Ways to Record
--------------------

``/dsprofile`` needs a world to be loaded, and can't be started once the game has frozen. For problems while the game loads, or for a freeze, start a recording
from the launcher instead. Java does not leave personal information out of these recordings by itself: the settings in the argument below leave out the most
important, but the home folder is not redacted. **Do not share a recording made without those settings.** This includes recordings made with Minecraft's own
``--jfrProfile`` option.

1. Add the JVM argument below to the launcher. It must be all one line with no spaces, separated by a space from any arguments already there.
2. Start the game and make the problem happen.
3. Quit the game normally, from the menu, within a few minutes of the problem. The recording keeps the last 10 minutes, and is written to ``dsurround.jfr``
   in the game directory when the game quits. It is replaced each time the game starts, so copy it somewhere else before playing again.
4. Remove the argument from the launcher again, and put ``dsurround.jfr`` in a ``.zip`` file to attach it.

.. code-block:: text
    :class: copybutton

    -XX:StartFlightRecording=name=dsurround,settings=profile,maxage=10m,dumponexit=true,filename=dsurround.jfr,jdk.JVMInformation#enabled=false,jdk.InitialEnvironmentVariable#enabled=false,jdk.InitialSystemProperty#enabled=false

If the game does not start after adding the argument, check it for a typo or a space.

.. list-table:: Where to Add the Argument
    :widths: auto
    :align: center
    :header-rows: 1

    *   - Launcher
        - Location
    *   - Minecraft Launcher
        - *Installations*, edit the installation, *More Options*, *JVM Arguments*.
    *   - CurseForge
        - *Settings*, *Minecraft*, *Java Settings*, *Additional Arguments*. This applies to every modpack in CurseForge.
    *   - Prism Launcher
        - Edit the instance, *Settings*, *Java*, check *Java arguments*.
    *   - Modrinth App
        - The instance's settings, *Java and memory*, *Java arguments*.

If the Game Freezes
~~~~~~~~~~~~~~~~~~~

A recording is only written when the game quits normally, so a game that has frozen and has to be closed with the task manager will not write one. If the game
was started with the argument above and a Java Development Kit (JDK) is installed, the recording can be saved while the game is still frozen, using the
``jcmd`` command in a terminal. The launcher's Java usually does not include ``jcmd``; use a JDK of the same major version as the game's Java, such as 21 for
Minecraft 1.21.

.. code-block:: text
    :class: copybutton

    jcmd

    jcmd <process id> JFR.dump name=dsurround filename=freeze.jfr
    jcmd <process id> Thread.print > threads.txt

``jcmd`` on its own lists the running Java programs, each line starting with its process ID. The game is the one whose name mentions Minecraft, Fabric, or
NeoForge; put its number in place of ``<process id>``. On Windows the process ID is also in the Task Manager, under *Details*, in the *PID* column for
``javaw.exe``.

``JFR.dump`` saves the recording so far to ``freeze.jfr`` in the game directory. ``Thread.print`` saves what every thread is doing at that moment to
``threads.txt``, which often shows on its own what the game is stuck on. Put both in a ``.zip`` file and include it.
