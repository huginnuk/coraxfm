#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Tom Lee-Gough'
SITENAME = 'Corax FM'
SITEURL = 'https://coraxfm.uk'

PATH = 'content'

TIMEZONE = 'Europe/London'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'feed.rss'
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ('info@coraxfm.uk', 'mailto:info@coraxfm.uk'),
    ('CIMA', 'https://www.cimaglobal.com/About-us/Find-a-CIMA-Accountant/Corax-FM-13911/'),
    ('LinkedIn', 'https://www.linkedin.com/company/coraxfm/'),
    ('Hermes', 'https://hermes.huginn.uk'),
    ('Cosearch', 'https://cosearch.huginn.uk'),
    ('Storyset', 'https://storyset.com/'),
    ('TOP', '#')
)

# Social widget
# SOCIAL = (
#     ('Linkedin', 'https://linkedin.com/in/tom-lee-gough-9b9b3433'),
#     ('Twitter', 'https://twitter.com/gidorahTLG')
# )

DEFAULT_PAGINATION = False

CSS_FILE = [
    'fontawesome/css/all.min.css',
	'spectre.min.css',
	'style.css'
]
THEME = 'tlg-theme'

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True