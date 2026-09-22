*season* Namespace
==================

This namespace provides information about the current season, if any. If Serene Seasons is installed, this information will reflect the current season defined by Serene Seasons.
If Serene Seasons is not installed, the season will always be Spring.

.. note::
    These functions are not available for biome condition scripts.

.. js:function:: Boolean season.isSpring()

    Evaluates whether the current season is Spring

    :return: ``true`` if it is Spring, ``false`` otherwise.
    :rtype: Boolean

.. js:function:: Boolean season.isSummer()

    Evaluates whether the current season is Summer

    :return: ``true`` if it is Summer, ``false`` otherwise.
    :rtype: Boolean

.. js:function:: Boolean season.isAutumn()

    Evaluates whether the current season is Autumn

    :return: ``true`` if it is Autumn, ``false`` otherwise.
    :rtype: Boolean

.. js:function:: Boolean season.isWinter()

    Evaluates whether the current season is Winter

    :return: ``true`` if it is Winter, ``false`` otherwise.
    :rtype: Boolean

.. js:function:: String season.isEarly()

    Evaluates whether the current period within a season is early. If a season mod is not installed it will always return ``true``. (*Added 1.21.1-0.4.4*)

    :return: ``true`` if it is early in the season, ``false`` otherwise.
    :rtype: Boolean

.. js:function:: String season.isMiddle()

    Evaluates whether the current period within a season is the middle. If a season mod is not installed it will always return ``true``. (*Added 1.21.1-0.4.4*)

    :return: ``true`` if it is middle of the season, ``false`` otherwise.
    :rtype: Boolean

.. js:function:: String season.isLate()

    Evaluates whether the current period within a season is late. If a season mod is not installed it will always return ``true``. (*Added 1.21.1-0.4.4*)

    :return: ``true`` if it is late in the season, ``false`` otherwise.
    :rtype: Boolean