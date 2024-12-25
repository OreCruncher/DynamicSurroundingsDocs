*state* Namespace
=================

.. note::
    These functions are not available for biome condition scripts.

.. js:function:: Boolean state.isInVillage()

    Evalulates whether the player is within 64 blocks of a bell and villagers are present.

    :return: Returns ``true`` if the player is within 64 blocks of a bell and villagers are present, ``false`` otherwise.
    :rtype: Boolean

.. js:function:: Boolean state.isInside()

    Evaluates whether the player is under cover. Note that some blocks do not count as cover, such as leaf blocks and fences.

    :return: Returns ``true`` if the area scanner determines the player is under cover, ``false`` otherwise.
    :rtype: Boolean

.. js:function:: Boolean state.isUnderWater()

    Evaluates whether the player's head is inside a liquid block.

    :return: Returns ``true`` if the player's head is in water, ``false`` otherwise.
    :rtype: Boolean
