import os
import sys
sys.path.insert(0, os.path.abspath('..'))

project = 'Bitdefender Login Account'
author = 'Your Name'
release = '1.0'

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
]

templates_path = ['_templates']
exclude_patterns = []

html_theme = 'alabaster'  # You can change to 'sphinx_rtd_theme' if you add it in requirements
html_static_path = ['_static']
master_doc = 'index'
