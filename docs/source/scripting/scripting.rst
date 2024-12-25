Scripting
=========

Dynamic Surroundings uses JavaScript as part of its configuration. Small snippits of JavaScript are used when determining when
a biome rule applies to a given biome, whether a special effect is eligbile for activation, or calculating the chance something
may occur. The Nashorn JavaScript engine is used to execute these small scripts.

As an example, here is the biome configuration rule for lush desert biomes. Don't worry too much about the details; they will be
explained in specific sections that detail the implementation.

.. code-block:: JSON

    {
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
    }

The ``biomeSelector`` value is a small JavaScript. Dynamic Surroundings will update the JavaScript execution environment with boolean values named for the various traits a biome can have.
In this particular case, this piece of script will evaluate to ``true`` or ``false`` based on the values of ``DESERT`` and ``LUSH``.

This rule also has two acoustics, each with their own seperate conditions. The ``biome.wind.desert`` will be active if it is raining. The ``biome.crickets`` acoustic will play if it is not
raining, water cannot freeze, and it is nighttime.

Common functions that a script may use are grouped into namespaces. For example, the ``isRaining()`` function is in the ``weather`` namespace. Documentation for the available namespaces
are listed below:

.. toctree::
    :titlesonly:

    biome<namespace_biome>
    dim<namespace_dim>
    diurnal<namespace_diurnal>
    global<namespace_global>
    lib<namespace_lib>
    player<namespace_player>
    state<namespace_state>
    season<namespace_season>
    weather<namespace_weather>
    biometraits

|
