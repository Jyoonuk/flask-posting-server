class Config :
    JWT_SECRET_KEY = 'yhacademy1029##heelo'
    JWT_ACCESS_TOKEN_EXPIRES = False
    PROPAGATE_EXCEPTIONS = True

    # AWS uk
    ACCESS_KEY = 'AKIA2EOOWFSV5PYW6OAH'
    SECRET_ACCESS = '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'  

    # S3 버킷이름과, 기본 URL 주소 셋팅
    S3_BUCKET = 'uk-image-test'
    S3_LOCATION = 'https://uk-image-test.s3.amazonaws.com/'
