*dim* Namespace
===============

Namespace containing functions related to the player's current dimension.

.. note::
    These functions are not available for biome condition scripts.

.. js:function:: String dim.getId()

    Gets the ID of the dimension as a string.

    :return: The resource location ID of the dimension
    :rtype: String

.. js:function:: String dim.getDimName()

    Gets the name of the dimension.

    :return: The dimension name
    :rtype: String

.. js:function:: Boolean dim.hasSky()

    Returns whether the dimension has a sky.

    :returns: Returns ``true`` if the dimension has a sky, ``false`` otherwise.
    :rtype: Boolean

.. js:function:: Boolean dim.isSuperFlat()

    Returns whether the dimension is super flat.

    :return: Returns ``true`` if the current dimension is super flat, ``false`` otherwise.
    :rtype: Boolean