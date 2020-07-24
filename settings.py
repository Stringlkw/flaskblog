class Config:
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@127.0.0.1:3306/flaskblog'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    ENV = 'development'
    SQLALCHEMY_ECHO = True


class ProductionConfig(Config):
    ENV = 'production'
    DEBUG = False
