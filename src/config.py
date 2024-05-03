class Config:
    SECRET_KEY = '+h^2p_i98q+-_-=wd9j!'

class DevelopmentConfig(Config):
    DEBUG = True
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = 'lUKYFeaf*)6_gp3]'
    MYSQL_DB = "cs50_project"

config = {
    'development': DevelopmentConfig
}
