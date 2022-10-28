from distutils.debug import DEBUG


class Developmentconfig():
    DEBUG=True
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = '1q2w3e4r'
    MYSQL_DB = 'prueba'

config = {
    'development': Developmentconfig
}