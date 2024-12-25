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

.. js:function:: Boolean season.isWarm()

    Evaluates whether the current season is considered warm.

    :return: Returns ``true`` if the current season is Spring or Summer, ``false`` otherwise.
    :rtype: Boolean

.. js:function:: Boolean season.isCool()

    Evaluates whether the current season is considered cool.

    :return: Returns ``true`` if the current season is Autumn or Winter, ``false`` otherwise.
    :rtype: Boolean