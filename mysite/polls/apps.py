from __future__ import unicode_literals

from django.apps import AppConfig
INSTALLED_APPS = (
    'feedparser',
    'urllib2',
    'BeautifulSoup',
    'string',
    
)


class PollsConfig(AppConfig):
    name = 'polls'
