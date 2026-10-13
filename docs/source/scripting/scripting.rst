Scripting
=========

Dynamic Surroundings uses scripting as part of its configuration. Small snippets of script code are used when determining when
a biome rule applies to a given biome, whether a special effect is eligible for activation, or calculating the chance something
may occur. The scripts are compiled by an engine specific to Dynamic Surroundings.

.. note::
    The Nashorn JavaScript engine was replaced with a simplified scripting engine starting with Dynamic Surroundings 0.4.3. The script
    syntax is very similar to JavaScript and should not require any changes to existing scripts.


As an example, here is the biome configuration rule for lush desert biomes. Don't worry too much about the details; they will be
explained in specific sections that detail the implementation.

.. code-block:: JSON

    {
        "biomeSelector": "DESERT && LUSH",
        "_comment": "Lush deserts",
        "acoustics": [
            {
                "factory": "biome.wind.desert",
                "conditions": "weather.isRaining()"
            },
            {
                "factory": "biome.crickets",
                "conditions": "weather.isNotRaining() && !weather.canWaterFreeze() && diurnal.isNight()"
            }
        ]
    }

The ``biomeSelector`` value is a small script. Dynamic Surroundings will update the script execution environment with boolean values named for the various traits a biome can have
(see :doc:`biometraits`).
In this particular case, this piece of script will evaluate to ``true`` or ``false`` based on the values of ``DESERT`` and ``LUSH``.

This rule also has two :term:`acoustics <Acoustic>`, each with their own separate conditions. The ``biome.wind.desert`` will be active if it is raining. The ``biome.crickets`` acoustic will play if it is not
raining, water cannot freeze, and it is nighttime.

Common functions that a script may use are grouped into namespaces. For example, the ``isRaining()`` function is in the ``weather`` namespace. Every namespace and its functions are described in
:doc:`functions`. Namespace, function, and trait names are not case sensitive, so ``lib.oneOf`` and ``lib.oneof`` are the same function.

Only the ``biome``, ``lib``, ``math``, and ``platform`` namespaces are available to :term:`biome selector <Biome Selector>` scripts, since those scripts run during configuration rather than in game.

The ``/dsscript`` command can be used to test a script in game. See :doc:`../commands/commands`.

Script Syntax
-------------

A script is a single expression that produces a value. Biome selectors and acoustic conditions must produce a boolean, and chance scripts must produce a number. There are no statements,
assignments, or user defined variables.

Values
~~~~~~

.. list-table::
    :widths: auto
    :align: center
    :header-rows: 1

    *   - Type
        - Examples
        - Notes
    *   - Number
        - ``42``, ``0.004``, ``-1.5``
        - All numbers are double precision floating point. A number must start with a digit (use ``0.5``, not ``.5``), and exponent notation such as ``1e5`` is not supported.
    *   - String
        - ``'minecraft:plains'``, ``"dsurround"``
        - Enclosed in single or double quotes. There are no escape sequences. Since scripts are stored in Json strings, single quotes are the easiest to use.
    *   - Boolean
        - ``true``, ``false``
        - Not case sensitive.
    *   - Variable
        - ``DESERT``, ``math.pi``
        - A name without parentheses. :term:`Biome traits <Biome Trait>` (see :doc:`biometraits`) and constants are variables.
    *   - Function call
        - :js:func:`weather.isRaining`, ``lib.oneOf(biome.getId(), 'a', 'b')``
        - A name followed by parentheses, with arguments separated by commas. The parentheses are required even when there are no arguments.

Names can contain letters, digits, and underscores, and must not start with a digit. A dot separates a namespace from the name within it. Names are not case sensitive.

Operators
~~~~~~~~~

Operators are listed from highest precedence (evaluated first) to lowest. Operators on the same row are evaluated left to right. Parentheses can be used to change the order of evaluation.

.. list-table::
    :widths: auto
    :align: center
    :header-rows: 1

    *   - Operators
        - Description
    *   - ``!`` ``-``
        - Logical not, and negation. These come before their operand (ex, ``!weather.isRaining()``, ``-player.getY()``). A leading ``+`` is allowed and ignored.
    *   - ``*`` ``/``
        - Multiplication and division. Dividing by zero produces infinity rather than an error.
    *   - ``+`` ``-``
        - Addition and subtraction. If either operand of ``+`` is a string, the operands are joined as strings instead (ex, ``'Level ' + 3`` produces ``Level 3``).
    *   - ``<`` ``<=`` ``>`` ``>=``
        - Numeric comparison.
    *   - ``==`` ``!=``
        - Equality. Numbers compare by value. Strings are compared exactly, so the comparison is case sensitive.
    *   - ``&&``
        - Logical and. The right operand is only evaluated if the left operand is ``true``.
    *   - ``||``
        - Logical or. The right operand is only evaluated if the left operand is ``false``.

For example, ``a || b && c`` is evaluated as ``a || (b && c)``, and ``1 + 2 * 3`` is ``7``.

The following are **not** supported: the remainder operator ``%``, the conditional operator ``?:`` (use ``lib.iif`` instead), assignment, and the bitwise operators. A single ``=``, ``&``, or ``|``
is reported as an error.

Conversions
~~~~~~~~~~~

When an operator needs a value of a particular type, the value is converted if possible:

* **To a number**: a string that holds a number is converted (ex, ``'5' * 2`` is ``10``). Other values cause an error.
* **To a boolean**: a number is ``true`` if it is not zero, a string is ``true`` only if it is ``true`` (ignoring case), and a missing value is ``false``. Other values cause an error.

Comments and Whitespace
~~~~~~~~~~~~~~~~~~~~~~~

``//`` starts a comment that runs to the end of the line. Spaces, tabs, and line breaks between tokens are ignored.

Errors
~~~~~~

Mistakes such as an unknown function or variable name, a missing parenthesis, or the wrong number of function arguments are reported when the script is compiled, along with where in the
script the problem was found. Errors are written to the log. A biome selector or condition script that fails is treated as ``false``. The ``/dsscript`` command displays the error message,
which makes it a convenient way to check a script before adding it to a configuration file.

Examples
--------

See :doc:`examples` for scripts taken from the Dynamic Surroundings configuration, with an explanation of each.

.. toctree::
    :hidden:

    functions
    biometraits
    examples
