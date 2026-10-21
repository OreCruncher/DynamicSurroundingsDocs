Logs and Crash Reports
======================

Minecraft writes what it and every mod are doing to log files. Most of the time the log has enough information to find the source of a problem, so include it
with every report.

Finding the Game Directory
--------------------------

All the files on this page are in the game directory, the folder that also has the ``mods`` and ``config`` folders. Each launcher has a way to open it:

* **Minecraft Launcher**: on the *Installations* tab, the folder button next to the installation. With the default location, this is ``%APPDATA%\.minecraft`` on
  Windows, ``~/Library/Application Support/minecraft`` on macOS, and ``~/.minecraft`` on Linux.
* **CurseForge**: right click the modpack and choose *Open Folder*.
* **Prism Launcher**: select the instance and click *Folder*.
* **Modrinth App**: open the instance's menu and choose *Open folder*.

Files to Include
----------------

.. list-table::
    :widths: auto
    :align: center
    :header-rows: 1

    *   - File
        - What it is
    *   - ``logs/latest.log``
        - The log of the most recent session. **Always include this.** It is replaced each time the game starts, and the previous one is kept as a compressed
          file named by date, such as ``logs/2026-10-14-1.log.gz``. If the game has been started again since the problem, send the dated file from the
          session where it happened.
    *   - ``logs/debug.log``
        - NeoForge only. A more detailed log of the same session. Include it too.
    *   - ``crash-reports/crash-<date>-client.txt``
        - Written when the game crashes and shows a crash screen. Include the one with the time of the crash.
    *   - ``hs_err_pid<number>.log``
        - Written to the game directory itself when Java crashes outright, and the game closes with no crash screen or crash report. This usually happens in
          native code, such as a graphics or sound driver, and the file shows where.
    *   - ``config/dsurround/dsurround.json`` and ``config/dsurround/soundconfig.json``
        - Dynamic Surroundings' settings. Include them when settings have been changed from the defaults. See :doc:`../config/modconfiguration`.

If the game does not start at all, the launcher's own log may be the only one with the error. Most launchers can show it from a console or log window.

Getting a Useful Log
--------------------

1. Start the game and make the problem happen.
2. Quit the game normally, from the menu. This lets everything still waiting to be written reach the log.
3. Take ``logs/latest.log`` before starting the game again.

Debug Logging
-------------

Dynamic Surroundings can write more detail to the log. Only turn this on when asked, or when making a resource pack, since some of it adds a lot of lines.

* :confval:`logging.enableDebugLogging` turns on debug messages. They are written to ``latest.log`` with ``[DEBUG]`` at the start of the line.
* :confval:`logging.traceMask` turns on extra traces, each with a number. Add the numbers of the traces wanted, so ``5`` turns on the first and third.

.. list-table:: Trace Mask Values
    :widths: auto
    :align: center
    :header-rows: 1

    *   - Value
        - Trace
    *   - 1
        - Each sound Dynamic Surroundings plays or stops itself, such as biome and block sounds.
    *   - 2
        - Each sound played through Minecraft's sound engine, by any mod, and the sounds dropped for being too far away to hear. This adds many lines; leave it
          on only long enough to make the problem happen.
    *   - 4
        - The configuration and tag files found and loaded, from mods, resource packs, and the ``config`` folder. Useful when a resource pack's
          configuration does not seem to be applied. See :doc:`../packs/layout`.

Traces only take effect while :confval:`logging.enableDebugLogging` is on. Changes made in the configuration menu take effect immediately. Turn debug logging
off again when done.

Sharing Logs
------------

Logs can be attached to an issue on GitHub. Attachments are limited to 25MB and to the extensions ``.log``, ``.gz``, ``.txt``, and ``.zip``; anything else
can be put in a ``.zip`` file. A log can also be uploaded to a paste site such as `mclo.gs <https://mclo.gs>`_ and the link included in the report.

Logs and crash reports contain the player's name and folder paths, which may include the computer's user name. Neither is needed to diagnose a problem, so it
is fine to replace them before sharing.
