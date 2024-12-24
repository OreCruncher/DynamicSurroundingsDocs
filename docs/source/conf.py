# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'Dynamic Surroundings'
copyright = '2024, 2025 OreCruncher'
author = 'OreCruncher'

release = '0.4.0'
version = '0.0.1'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinxcontrib.youtube'
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'agogo'

html_theme_options = {
    'bodyfont' : 'Verdana',
    'headerfont': 'Verdana',
    'rightsidebar': 'false'
}

# -- Options for EPUB output
epub_show_urls = 'footnote'
