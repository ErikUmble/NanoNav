# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import os
import sys

# Add the project root to the path to allow autofunction for nanonav.py
sys.path.insert(0, os.path.abspath('./'))

project = 'NanoNav'
copyright = '2024, Erik Umble, Joel McCandless, & Chris Kurbiel'
author = 'Erik Umble, Joel McCandless, & Chris Kurbiel'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx_rtd_theme',
    'sphinx.ext.autodoc',
    'sphinx_copybutton',
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# mock imports for micropython modules
autodoc_mock_imports = ["bluetooth", "micropython", "ble_advertising", "rp2", "machine"]


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

# below is used for css roles (to set a phrase with in color, for instance)
rst_prolog = """
.. include:: <s5defs.txt>

"""

def setup(app):
    app.add_css_file('css/s4defs-roles.css')
