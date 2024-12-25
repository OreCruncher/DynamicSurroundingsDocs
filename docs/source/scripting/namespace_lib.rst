*lib* Namespace
===============

The functions in this namespace provide support for common things that a script may do. This namespace is available for biome conditions, acoustic filtering, and chance percentages.

.. code-block:: javascript

    Object iif(boolean result, Object trueResult, Object falseResult)

This function will return the value of ``trueResult`` or ``falseResult`` depending on the value of ``result``.

.. code-block:: javascript

    Boolean match(String pattern, String input)

Applies the provided regular expression ``pattern`` to determine if ``input`` is a match.

.. code-block:: javascript

    Boolean oneof(Object input, Object... possibles)

Determines if ``input`` matches one of the ``possibles`` values.

.. code-block:: javascript

    Boolean isBetween(Double value, Double min, Double max)

Determines if ``value`` is between ``min`` and ``max`` inclusive.

.. code-block:: javascript

    Boolean isModLoaded(String modId)

Determines if the mod associated with ``modId`` is loaded.
