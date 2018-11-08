# -*- coding: utf-8 -*-
#
# PlaidCloud documentation build configuration file, created by
# sphinx-quickstart on Thu Mar 30 22:41:32 2017.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# Mike did some hacking on 4/24/17 to handle this: http://stackoverflow.com/questions/12772927/specifying-an-online-image-in-sphinx-restructuredtext-format
# search this code for monkeypatch to see where
import os
import sys
import sphinx.environment                  # monkeypatch from SO
from docutils.utils import get_source_line  # monkeypatch from SO
import recommonmark

sys.path.insert(0, os.path.abspath('.'))
sys.path.insert(0, os.path.abspath('/src/plaid/rpc_v1'))

def _warn_node(self, msg, node, **kwargs):                             # monkeypatch
    if not msg.startswith('nonlocal image URI found:'):                # monkeypatch
        self._warnfunc(msg, '%s:%s' % get_source_line(node), **kwargs)  # monkeypatch
        # monkeypatch
sphinx.environment.BuildEnvironment.warn_node = _warn_node             # monkeypatch

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'
html_show_sphinx = False
html_show_sourcelink = False


# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo',
    'sphinx.ext.mathjax',
    'sphinx.ext.ifconfig',
    'sphinxcontrib.fulltoc',
    'sphinx.ext.napoleon',
    'sphinx_sitemap'
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# This allows these modules to be mocked up without importing all dependencies, to add to this just add the root module name.
autodoc_mock_imports = ["plaid", "plaidtools"]

# Adding markdown so we can use lecacy stuff more-easily.
# http://www.sphinx-doc.org/en/stable/markdown.html
source_parsers = {
    '.md': 'recommonmark.parser.CommonMarkParser',
}

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
source_suffix = ['.rst', '.md']

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'PlaidCloud'
copyright = u'2008-2018, Tartan Solutions, Inc'
author = u'Paul Morel, Michael Rea'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = u''
# The full version, including alpha/beta/rc tags.
release = u''

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
# Mike added '**/*__*' on 20170607 to be able to turn off things we want to exclude.
exclude_patterns = ['**/*__*', '**/._*']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True


# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
#html_theme = 'alabaster'
html_theme = 'sphinx_rtd_theme'
#html_theme = 'classic'
#html_theme = 'pyramid'
html_logo = '_static/plaidcloud-white-239x63.png'

html_theme_path = ['.']

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
html_theme_options = {
    'navigation_depth': 2
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

def setup(app):
    app.add_stylesheet('css/custom.css')


# -- Options for HTMLHelp output ------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'PlaidClouddoc'


# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'PlaidCloud.tex', u'PlaidCloud Documentation',
     u'Paul Morel, Michael Rea', 'manual'),
]


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'plaidcloud', u'PlaidCloud Documentation',
     [author], 1)
]


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'PlaidCloud', u'PlaidCloud Documentation',
     author, 'PlaidCloud', 'One line description of project.',
     'Miscellaneous'),
]


# -- Options for Epub output ----------------------------------------------

# Bibliographic Dublin Core info.
epub_title = project
epub_author = author
epub_publisher = author
epub_copyright = copyright

# The unique identifier of the text. This can be a ISBN number
# or the project homepage.
#
# epub_identifier = ''

# A unique identification for the text.
#
# epub_uid = ''

# A list of files that should not be packed into the epub file.
epub_exclude_files = ['search.html']


# Example configuration for intersphinx: refer to the Python standard library.
intersphinx_mapping = {'https://docs.python.org/': None}

# PJM - This is to pretty up the API docstring publishing
add_module_names = True
autodoc_docstring_signature = True

# This is for the sitemap generation
site_url = 'https://plaidcloud.io/docs/'
