# -*- coding: utf-8 -*-

import sys, os
from datetime import date

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

from sphinx.highlighting import lexers
from pygments.lexers.web import PhpLexer
lexers['php'] = PhpLexer(startinline=True)
primary_domain = 'php'

on_rtd = os.environ.get('READTHEDOCS', None) == 'True'
if on_rtd:
  html_theme = 'default'
else:
  html_theme = 'nature'

html_static_path = ['_static']
htmlhelp_basename = 'Moardoc'
