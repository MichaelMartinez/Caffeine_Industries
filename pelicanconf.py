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
    'extra/favicon.ico',
    'extra/favicon-16x16.png',
    'extra/favicon-32x32.png',
    'extra/favicon-96x96.png',
    'extra/favicon-160x160.png',
    'extra/favicon-196x196.png',
]

# Extra metadata dictionaries keyed by relative path
EXTRA_PATH_METADATA = {
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
#RELATIVE_URLS = True

# Plugins & Settings ----------------------------------------------------------
# Mac Path: PLUGIN_PATHS = ["plugins", "/Users/michaelmartinez/Dropbox/pelican/pelican-plugins"]
PLUGIN_PATHS = ["plugins", "/Users/mm/Dropbox/pelican/pelican-plugins"]
# Use these plugins for development
#PLUGINS = ["post_stats"]

# Only use image_process when publishing...
PLUGINS = ["image_process", "post_stats"]

# Image process settings use ![Picture][/pic.jpg]{: class=image-process-large-photo }
IMAGE_PROCESS = {
    'crisp': {'type': 'responsive-image',
              'srcset': [('1x', ["scale_in 800 600 True"]),
                         ('2x', ["scale_in 1600 1200 True"]),
                         ('4x', ["scale_in 3200 2400 True"]),
                         ],
              'default': '1x',
              },
    'large-photo': {'type': 'responsive-image',
                    'sizes': '(min-width: 1200px) 800px, (min-width: 992px) 650px, \
                              (min-width: 768px) 718px, 100vw',
                    'srcset': [('600w', ["scale_in 600 450 True"]),
                               ('800w', ["scale_in 800 600 True"]),
                               ('1600w', ["scale_in 1600 1200 True"]),
                               ],
                    'default': '800w',
                    },
}

# Theme settings --------------------------------------------------------------

THEME = '/Users/mm/Dropbox/caffeine_pelican/caff_boot'
#THEME = './caff_boot'
# Define a custom header CAF style. Need to include Navigation stuff.
SKIP_DEFAULT_NAVIGATION = True
# add custome site header_nav
CUSTOM_SITE_HEADERS = ('caf_header_nav.html',)
CUSTOM_FOOTER = ('footer.html')
PROFILE_IMAGE = '/images/CI_web.png'
EXTRA_FAVICON = True
# Define Pages in Content folder that can be displayed here.
DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = False
# BOOTSTRAP_STYLESHEET = ('simplex-bootstrap.css')
# Extra stylesheets, for bootstrap overrides or additional styling.
STYLESHEET_FILES = ('pygment.css', 'caf.css',)
STYLESHEET_URLS = (
'https://fonts.googleapis.com/css?family=Open+Sans:400,300,300italic,400italic,600,700italic,800,800italic,700,600italic',
'https://fonts.googleapis.com/css?family=Merriweather')
JAVASCRIPT_FILES = ('smoothScroll.js', 'main.js')

SHOW_ARTICLE_AUTHOR = True
# SITE_SUBTEXT = 'Caffeine Industries is the home of Micahel Martinez'
META_DESCRIPTION = '''Caffeine Industries is and LLC owned by Michael Martinez and his Wife Nathalia. I feel most at
home in Python, but I can use a variety of technology stacks. I make stuff for the web, Android, and lots of other
tech stacks with love.'''

PROJECTITEMS = (
    ('Engineer Toolkit', 'engineer-toolkit.html'),
    ('Abecedario Infantil', 'abecedario-infantil-spanish-alphabet-for-children.html'),
)

# LICENSE_URL = ''
# LICENSE_NAME = ''

# MENUITEMS = (
#     ('Stuff', 'Link'),
#     ('Mailing List', 'Link'),
# )

# GITHUB_ADDRESS = 'https://github.com/michaelmartinez'
# TWITTER_ADDRESS = 'https://twitter.com/monkmartinez'

# DISQUS_SITENAME = 'caffeineindustries'
GOOGLE_ANALYTICS = 'UA-1946861-1'
