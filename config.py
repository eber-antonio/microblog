import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    """ Clase para guardar variables de ocnfiguracion """
    #en caso de subirse a produccion se debe de cambiar el key a uno más seguro
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'

    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

