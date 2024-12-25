*player* Namespace
==================

Functions in this namespace are related to the state of the current player.

.. note::
    These functions are not available for biome condition scripts.

.. js:function:: Boolean player.isCreative()

    Evaluates whether the player is in creative mode.

    :return: ``true`` if the player is in creative mode, ``false`` otherwise.
    :rtype: Boolean

.. js:function:: Boolean player.isBurning()

    Evaluates whether the player is isBurning

    :return: ``true`` if the player is burning, ``false`` otherwise.
    :rtype: Boolean

.. js:function:: Boolean player.isSuffocating()

    Evaluates whether the player is suffocating.

    :return: ``true`` if the player is suffocating, ``false`` otherwise.
    :rtype: Boolean

.. js:function:: Boolean player.isFlying()

    Evaluates whether the player is flying.

    :return: ``true`` if the player is flying, ``false`` otherwise.
    :rtype: Boolean

.. js:function:: Boolean player.isSprinting()

    Evaluates whether the player is sprinting.

    :return: ``true`` if the player is sprinting, ``false`` otherwise.
    :rtype: Boolean

.. js:function:: Boolean player.isInLava()

    Evaluates whether the player is located within lava.

    :return: ``true`` if the player is in lava, ``false`` otherwise.
    :rtype: Boolean

.. js:function:: Boolean player.isInvisible()

    Evaluates whether the player is invisible.

    :return: ``true`` if the player is invisible, ``false`` otherwise.
    :rtype: Boolean

.. js:function:: Boolean player.isInWater()

    Evaluates whether the player is in water.

    :return: ``true`` if the player is in water, ``false`` otherwise.
    :rtype: Boolean

.. js:function:: Boolean player.isMoving()

    Evaluates whether the player is moving, ``false`` otherwise.
    :rtype: Boolean

.. js:function:: Boolean player.isWet()

    Evaluates whether the player is wet.

    :return: ``true`` if the player is wet, ``false`` otherwise.
    :rtype: Boolean

.. js:function:: Boolean player.isRiding()

    Evaluates whether the player is riding an entity such as a horse or minecart.

    :return: ``true`` if the player is riding, ``false`` otherwise.
    :rtype: Boolean

.. js:function:: Boolean player.isOnGround()

    Evaluates whether the player is on the ground.

    :return: ``true`` if the player is on the ground, ``false`` otherwise.
    :rtype: Boolean

.. js:function:: Boolean player.canRainOn()

    Evaluates whether the player is in the open where rain can fall on them.

    :return: ``true`` if the player can be rained on, ``false`` otherwise.
    :rtype: Boolean

.. js:function:: Boolean player.canSeeSky()

    Evaluates whether the player is able to see the sky when looking up.

    :return: ``true`` if the player can see the sky, ``false`` otherwise.
    :rtype: Boolean

.. js:function:: Float player.getHealth()

    Gets the current health of the player.

    :return: Player's current health
    :rtype: Float

.. js:function:: Float player.getMaxHealth()

    Gets the players maximum possible health value.

    :return: Player's maximum health
    :rtype: Float

.. js:function:: Float player.getFoodLevel()

    Gets the players current food level.

    :return: Player's current food level
    :rtype: Float

.. js:function:: Float player.getFoodSaturationLevel()

    Gets the player's current food saturation level.

    :return: Player's current food saturation level.
    :rtype: Float

.. js:function:: Double player.getX()

    Gets the X value of the player's current block position.

    :return: X value of the block position of the player
    :rtype: Double

.. js:function:: Double player.getY()

    Gets the Y value of the player's current block position.

    :return: Y value of the block position of the player
    :rtype: Double

.. js:function:: Double player.getZ()

    Gets the Z value of the player's current block position.

    :return: Z value of the block position of the player
    :rtype: Double

.. js:function:: Boolean player.hasEffect(String effect)

    Evaluates whether the player has the specified effect. The effect is expressed as a resource location ID.

    :param effect: The effect to check for
    :type effect: String
    :return: Returns ``true`` if the player has the given effect, ``false`` otherwise.
    :rtype: Boolean
