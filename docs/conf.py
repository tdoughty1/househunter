"""Sphinx configuration."""
project = "Househunter"
author = "Todd Doughty"
copyright = "2023, Todd Doughty"
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx_click",
    "myst_parser",
]
autodoc_typehints = "description"
html_theme = "furo"
