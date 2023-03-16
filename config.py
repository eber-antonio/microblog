import os

class Config(object):
    """ Clase para guardar variables de ocnfiguracion """
    #en caso de subirse a produccion se debe de cambiar el key a uno más seguro
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'