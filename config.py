import os

basedir = os.path.abspath(os.path.dirname(__file__))

import pyrebase
import firebase_admin
from firebase_admin import credentials

class Config:
	
	SECRET_KEY = os.environ.get('SECRET_KEY') 

	SQLALCHEMY_COMMITON_TEARDOWN = True
	SQLALCHEMY_TRACK_MODIFICATIONS = True
	FLASK_MAIL_SUBJECT_PREFIX = '[Flasky]'
	FLASK_MAIL_SENDER = 'Flask Admin {}'.format(os.environ.get('MAIL_USERNAME'))
	FLASK_ADMIN = os.environ.get('FLASK_ADMIN')
	FLASKY_POSTS_PER_PAGE = 5
	FLASKY_FOLLOWERS_PER_PAGE = 10
	FIREBASE_CONFIG = dict(

		apiKey="AIzaSyDjODHfV_kxeoXgalnfaCyiyd38_EuBBds",
	    authDomain= "house-of-memes.firebaseapp.com",
	    projectId="house-of-memes",
	    storageBucket="house-of-memes.appspot.com",
	    databaseURL="https://house-of-memes-default-rtdb.firebaseio.com/",
	    messagingSenderId="737530410440",
	    appId= "1:737530410440:web:21441705198ae5fd46bcfd",
	    measurementId="G-0SXPFWWD1G",
		)

	FIREBASE_USER_APP_INSTANCE = pyrebase.initialize_app(FIREBASE_CONFIG)
	MAX_CONTENT_LENGTH = 1024 * 1024 * 5
	UPLOAD_PATH = os.path.join(basedir, "uploads")

	@staticmethod
	def init_app(app):

		pass

		#cred = credentials.Certificate(os.path.join(basedir, 'firebase_admin_config.json'))
		#firebase_admin.initialize_app(cred)

class DevelopmentConfig(Config):
	
	DEBUG = True

	MAIL_SERVER = 'smtp.googlemail.com'
	MAIL_PORT = 587
	MAIL_USE_TLS = True
	MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
	MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')

	SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
	'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')

class TestingConfig(Config):

	TESTING = True

	SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
	'sqlite:///' + os.path.join(basedir, 'data-test.sqlite')

class ProductionConfig(Config):

	SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
	'sqlite:///' + os.path.join(basedir, 'data.sqlte')



config = dict(developent = DevelopmentConfig, 
	testing = TestingConfig, 
	production = ProductionConfig, 
	default = DevelopmentConfig)