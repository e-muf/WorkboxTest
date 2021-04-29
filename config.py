
class Config:
  pass

class DevelopmentConfig(Config):
  DEBUG = True
  SQLALCHEMY_DATABASE_URI = 'sqlite:///users.db'
  SQLALCHEMY_TRACK_MODIFICATIONS = False
  JSON_AS_ASCII = False

config = {
  'development': DevelopmentConfig,
}