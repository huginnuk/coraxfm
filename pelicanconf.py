#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Tom Lee-Gough'
SITENAME = 'tlg-accounting.co.uk'
SITEURL = 'https://tlg-accounting.co.uk'

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
    ('Email', 'mailto:info@tlg-accouting.co.uk'),
    ('CIMA', 'https://www.cimaglobal.com/About-us/Find-a-CIMA-Accountant/Tom-Lee-Gough-Accounting-13911/'),
    ('LinkedIn', 'https://www.linkedin.com/company/tlg-accounting/'),
    ('Hermes', 'https://hermes.dev.huginn.co.uk'),
    ('Xero', 'https://xero.com'),
    ('TOP', '#')
)

# Social widget
# SOCIAL = (
#     ('Linkedin', 'https://linkedin.com/in/tom-lee-gough-9b9b3433'),
#     ('Twitter', 'https://twitter.com/gidorahTLG')
# )

DEFAULT_PAGINATION = False

CSS_FILE = [
	# 'spectre.min.css',
	'style.css'
]
THEME = 'tlg-theme'

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True