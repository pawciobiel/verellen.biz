USE_S3 = True
AWS_ACCESS_KEY_ID = 'x'
AWS_SECRET_ACCESS_KEY = 'x'
AWS_STORAGE_BUCKET_NAME = 'x'
AWS_QUERYSTRING_AUTH = False
S3_URL = 'https://s3-eu-west-1.amazonaws.com/%s' % AWS_STORAGE_BUCKET_NAME

if USE_S3:
    DEFAULT_FILE_STORAGE = 'verellen.utils.s3utils.MediaRootS3BotoStorage'
    THUMBNAIL_DEFAULT_STORAGE = 'verellen.utils.s3utils.MediaRootS3BotoStorage'
    MEDIA_URL = S3_URL + '/media/'

MEDIA_ROOT = 'x'
