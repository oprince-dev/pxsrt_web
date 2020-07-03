import os

class Config:
    #secret key added to env (looking into if it's best practice)
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
    UPLOADED_IMAGES_DEST = 'pxsrt/static/img/uploads/'
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024
