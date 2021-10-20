class SystemConfig:
      DEBUG = True

  SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{user}:{password}@{host}/{db-name}?charset=utf8'.format(**{
      'user': '{User名}',
      'password': '{設定したPassword}',
      'host': 'localhost',
      'db_name': 'test_db'
  })

Config = SystemConfig
