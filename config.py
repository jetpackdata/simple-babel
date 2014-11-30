# -*- coding: UTF-8 -*-

import os
basedir=os.path.abspath(os.path.dirname(__file__))

class Config:
  SECRET_KEY='set a secret key here'
  DEBUG = True
  LANGUAGES = {
    'en': 'English',
    'fr': 'Français'
  }

  @staticmethod
  def init_app(app):
    pass

class TestingConfig(Config):
  TESTING = False

class ProductionConfig(Config):
  pass

config = {
  'testing' : TestingConfig,
  'production': ProductionConfig
}
