*season* Namespace
==================

This namespace provides information about the current season, if any. If Serene Seasons is installed, this information will reflect the current season defined by Serene Seasons.
If Serene Seasons is not installed, the season will always be Spring.

.. note::
    These functions are not available for biome condition scripts.

.. code-block:: javascript

    Boolean isSpring()
    Boolean isSummer()
    Boolean isAutumn()
    Boolean isWinter()

These functions will return ``true`` or ``false`` depending on the current season.

.. code-block:: javascript

    Boolean isWarm()

Returns ``true`` if the current season is Spring or Summer, ``false`` otherwise.

.. code-block:: javascript

    Boolean isCool()

Returns ``true`` if the current season is Autumn or Winter, ``false`` otherwise.