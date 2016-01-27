# -*- coding: utf-8 -*-
import os

#
# This is the configuration file of the application
#
# Please make sure you don't store here any secret information and use environment
# variables
#


SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
SQLALCHEMY_POOL_RECYCLE = 60
SENDGRID_USERNAME = os.environ.get('SENDGRID_USERNAME')
SENDGRID_PASSWORD = os.environ.get('SENDGRID_PASSWORD')


SECRET_KEY = 'aiosdjsaodjoidjioewnioewfnoeijfoisdjf'

# available languages
LANGUAGES = {
    'en': 'English',
    'he': 'עברית',
}