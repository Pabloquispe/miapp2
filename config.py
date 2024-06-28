import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or os.urandom(24)
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    HORARIO_INICIO_MANANA = '09:00'
    HORARIO_FIN_MANANA = '12:00'
    HORARIO_INICIO_TARDE = '13:00'
    HORARIO_FIN_TARDE = '18:00'

class DevelopmentConfig(Config):
    DEBUG = True
SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 
    'mysql+pymysql://camaralurin22_pablo:Pablo123456%23@localhost/camaralurin22_proyecto26')


class TestingConfig(Config):
    TESTING = True
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'test.db')

class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')

config_by_name = {
    'dev': DevelopmentConfig,
    'test': TestingConfig,
    'prod': ProductionConfig,
    'default': DevelopmentConfig
}
