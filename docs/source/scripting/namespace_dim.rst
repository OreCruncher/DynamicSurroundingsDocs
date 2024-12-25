*dim* Namespace
===============

Namespace containing functions related to the player's current dimension.

.. note::
    These functions are not available for biome condition scripts.

.. code-block:: javascript

    String getId()

The ID of the dimension as a string.

.. code-block:: javascript

    String getDimName()

The name of the dimension.

.. code-block:: javascript

    Boolean hasSky()

Returns ``true`` if the dimension has a sky, ``false`` otherwise.

.. code-block:: javascript

    Boolean isSuperFlat()

Returns ``true`` if the current dimension is super flat, ``false`` otherwise.