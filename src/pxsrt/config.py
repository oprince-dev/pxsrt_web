class Config:
    SECRET_KEY = '19876e6891d3a956529578b0e5d34a88'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    UPLOADED_IMAGES_DEST = 'pxsrt/static/img/uploads/'
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024
