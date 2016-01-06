#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Michael Martinez'
SITENAME = 'Caffeine Industries'
SITEURL = 'http://caffeineindustries.com'

PATH = 'content'

TIMEZONE = 'US/Arizona'

DEFAULT_LANG = 'en'

# Delete the output directory, before generating new files
DELETE_OUTPUT_DIRECTORY = True

# The static paths you want to have accessible on the output path "static"
STATIC_PATHS = [
    'images',
    'extra/CNAME',
    'extra/favicon.ico',
    'extra/favicon-16x16.png',
    'extra/favicon-32x32.png',
    'extra/favicon-96x96.png',
    'extra/favicon-160x160.png',
    'extra/favicon-196x196.png',
    'extra/robots.txt',
]

# Extra metadata dictionaries keyed by relative path
EXTRA_PATH_METADATA = {
    'extra/CNAME': {'path': 'CNAME'},
    'extra/favicon.ico': {'path': 'favicon.ico'},
    'extra/favicon-16x16.png': {'path': 'favicon-16x16.png'},
    'extra/favicon-32x32.png': {'path': 'favicon-32x32.png'},
    'extra/favicon-96x96.png': {'path': 'favicon-96x96.png'},
    'extra/favicon-160x160.png': {'path': 'favicon-160x160.png'},
    'extra/favicon-196x196.png': {'path': 'favicon-196x196.png'},
}

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

DISPLAY_CATEGORIES_ON_MENU = False

# Theme settings --------------------------------------------------------------
THEME = '/Users/michaelmartinez/Dropbox/caffeine_pelican/caff_boot'
# Define a custom header CAF style. Need to include Navigation stuff.
SKIP_DEFAULT_NAVIGATION = True
# add custome site header_nav
CUSTOM_SITE_HEADERS = ('caf_header_nav.html',)
PROFILE_IMAGE = '/images/CI_web.png'
EXTRA_FAVICON = True
# Define Pages in Content folder that can be displayed here.
DISPLAY_PAGES_ON_MENU = True
#BOOTSTRAP_STYLESHEET = ('simplex-bootstrap.css')
# Extra stylesheets, for bootstrap overrides or additional styling.
STYLESHEET_FILES = ('pygment.css', 'caf.css',)

SHOW_ARTICLE_AUTHOR = True
#SITE_SUBTEXT = 'Caffeine Industries is the home of Micahel Martinez'
META_DESCRIPTION = '''Caffeine Industries is and LLC owned by Michael Martinez and his Wife Nathalia. I feel most at
home in Python, but I can use a variety of technology stacks. I make stuff for the web, Android, and lots of other
tech stacks with love.'''

# LICENSE_URL = ''
# LICENSE_NAME = ''
PROJECTITEMS = (
    ('Engineer Toolkit', 'engineer-toolkit.html'),
    ('Abecedario Infantil', 'abecedario-infantil-spanish-alphabet-for-children.html'),
)

# MENUITEMS = (
#     ('Stuff', 'Link'),
#     ('Mailing List', 'Link'),
# )

#GITHUB_ADDRESS = 'https://github.com/micahelmartinez'
#TWITTER_ADDRESS = 'https://twitter.com/monkmartinez'

#DISQUS_SITENAME = 'caffeineindustries'
#GOOGLE_ANALYTICS_ID = '<insert tracking number here>'


