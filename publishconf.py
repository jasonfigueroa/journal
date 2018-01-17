#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

# not sure about the following
# DELETE_OUTPUT_DIRECTORY = True

# FEED_ALL_ATOM = 'feeds/all.atom.xml'
# CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'

AUTHOR = u'Jason Figueroa'
SITENAME = u'Jason Figueroa'

SITEURL = 'https://jasonfigueroa.github.io'
ABOUTURL = 'https://jasonfigueroa.github.io/pages/about-me.html'
ABOUTSITEURL = 'https://jasonfigueroa.github.io/pages/about-site.html'

# SITEURL = ''

THEME = 'pelican-blue'

PATH = 'content'

TIMEZONE = 'America/Chicago'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# added for pelican-blue theme
SIDEBAR_DIGEST = 'Passionate Learner'

FAVICON = 'https://jasonfigueroa.github.io/images/favicon.ico'

DISPLAY_PAGES_ON_MENU = True

# TWITTER_USERNAME = 'jasonfigueroa_'

MENUITEMS = (('Blog', SITEURL), ('About Me', ABOUTURL), ('About This Site', ABOUTSITEURL))

# Social widget
SOCIAL = (('twitter', 'https://twitter.com/jasonfigueroa_'),
          ('github', 'https://github.com/jasonfigueroa'),
          ('linkedin', 'https://www.linkedin.com/in/jason-figueroa-b59a3798/'),)

DEFAULT_PAGINATION = 10

DISQUS_SITENAME = "jasonfigueroa"


# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
RELATIVE_URLS = False

#GOOGLE_ANALYTICS = ""
