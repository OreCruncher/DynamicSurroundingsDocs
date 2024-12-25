*player* Namespace
==================

Functions in this namespace are related to the state of the current player.

.. note::
    These functions are not available for biome condition scripts.

.. code-block:: javascript

    Boolean isCreative()
    Boolean isBurning()
    Boolean isSuffocating()
    Boolean isFlying()
    Boolean isSprinting()
    Boolean isInLava()
    Boolean isInvisible()
    Boolean isInWater()
    Boolean isMoving()
    Boolean isWet()
    Boolean isRiding()
    Boolean isOnGround()
    Boolean canRainOn()
    Boolean canSeeSky()

Returns ``true`` if the player is in the given state, ``false`` otherwise.

.. code-block:: javascript

    Float getHealth()
    Float getMaxHealth()

Returns information about the players current health parameters.

.. code-block:: javascript

    Float getFoodLevel()
    Float getFoodSaturationLevel()

Provides information about the players food levels.

.. code-block:: javascript

    Double getX()
    Double getY()
    Double getZ()

Provides the player's current block location.

.. code-block:: javascript

    Boolean hasEffect(String effect)

Returns ``true`` if the player has the given effect, ``false`` otherwise.
