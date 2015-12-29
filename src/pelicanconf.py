#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Voidspace'
SITENAME = u'My life rants'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DISQUS_SITENAME = "ramaseshan"

# Blogroll
#LINKS = (('Home', '/'), ('Presentations', '/presentations'),('About', '/about'),)

# Social widget
TWITTER_USERNAME = 'voidspacexyz'
SOCIAL = (('Twitter', '@voidspacexyz'),('Email', 'null@voidspace.xyz'),)
GITHUB_NAME = "ramaseshan"

DEFAULT_PAGINATION = 6
THEME = 'theme'
ARTICLE_URL = '{category}/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = '{category}/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'
# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
