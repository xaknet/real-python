import os

basedir = os.path.abspath(os.path.dirname(__file__))

DATABASE = 'flasktaskr.db'
USERNAME = 'admin'
PASSWORD = 'admin'
WTF_CSRF_ENABLED = True
SECRET_KEY = 'x4lTFbxSwhwCdvm1B1Ar'


DATABASE_PATH = os.path.join(basedir, DATABASE)