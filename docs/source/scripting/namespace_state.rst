*state* Namespace
=================

.. note::
    These functions are not available for biome condition scripts.

.. code-block:: javascript

    Boolean isInVillage()

Returns ``true`` if the player is within 64 blocks of a bell and villagers are present, ``false`` otherwise.

.. code-block:: javascript

    Boolean isInside()

Returns ``true`` if the area scanner determines the player is under cover, ``false`` otherwise. Note that some blocks do not count as cover, such as leaf blocks and fences.

.. code-block:: javascript

    Boolean isUnderWater()

Returns ``true`` if the player's head is in water, ``false`` otherwise.
