# -*- coding: utf-8 -*-

import os
import sphinx_bootstrap_theme
import sys
from datetime import date
from pygments.lexers.web import PhpLexer
from sphinx.highlighting import lexers

extensions = ['sphinxcontrib.phpdomain']
templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'
project = u'Moar'
copyright = unicode(date.today().year) + u', Bryan Davis and contributors'
version = 'dev'
release = version
exclude_patterns = ['_build']
pygments_style = 'sphinx'

lexers['php'] = PhpLexer(startinline=True)
primary_domain = 'php'

on_rtd = os.environ.get('READTHEDOCS', None) == 'True'
if on_rtd:
  html_theme = 'default'
else:
  html_theme = 'bootstrap'
  html_theme_path = sphinx_bootstrap_theme.get_html_theme_path()
  html_theme_options = {
      'bootswatch_theme': 'cerulean'
      }
#end if

html_static_path = ['_static']
htmlhelp_basename = 'Moardoc'
