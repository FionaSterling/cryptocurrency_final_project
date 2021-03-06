import os

class Config(object):
    API_KEY = os.environ.get('API_KEY') or 'you-will-never-guess'
    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
