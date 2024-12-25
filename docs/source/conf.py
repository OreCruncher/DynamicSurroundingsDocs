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
    'sphinxcontrib.youtube',
    'sphinx_rtd_theme'
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

html_theme_options = {
    'logo_only' : 'true',
    'style_external_links': 'true'
}

# Style sheets
html_static_path = ['_static']
html_css_files = [
    'css/custom.css'
]

html_logo = 'images/icon.png'

# -- Options for EPUB output
epub_show_urls = 'footnote'
