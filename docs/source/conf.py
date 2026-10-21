# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'Dynamic Surroundings'
copyright = '2024-2026 OreCruncher'
author = 'OreCruncher'

release = '0.4.7'
version = '0.4'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.extlinks',
    'sphinxcontrib.youtube',
    'sphinx_rtd_theme',
    'sphinx_copybutton'
]

# -- Copy buttons on code blocks

# Only blocks marked with ":class: copybutton" (such as commands for players to paste) get a copy button
copybutton_selector = 'div.copybutton > div.highlight > pre'

# -- Links to the mod's source on GitHub

# The branch or tag that source links point at
source_branch = 'main'
_source_repo = 'https://github.com/OreCruncher/DynamicSurroundingsFabric'

# :source:`path` links to a file, :source-dir:`path` to a folder, both relative to the repository root;
# :asset:`path` links to a file in the mod's assets folder. Use :source:`text <path>` for custom link text.
extlinks = {
    'source': (f'{_source_repo}/blob/{source_branch}/%s', '%s'),
    'source-dir': (f'{_source_repo}/tree/{source_branch}/%s', '%s'),
    'asset': (f'{_source_repo}/blob/{source_branch}/common/src/main/resources/assets/dsurround/%s', '%s'),
}

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

html_theme_options = {
    'logo_only': True,
    'style_external_links': True
}

# Style sheets
html_static_path = ['_static']
html_css_files = [
    'css/custom.css'
]

html_logo = 'images/icon.png'

# -- Options for link checking (make linkcheck)

# CurseForge rejects automated requests with 403, so its links can't be checked
linkcheck_ignore = [
    r'https://www\.curseforge\.com/.*'
]

# GitHub rate limits bursts of requests (429); retry rather than report the link as broken
linkcheck_retries = 3

# -- Options for EPUB output
epub_show_urls = 'footnote'
