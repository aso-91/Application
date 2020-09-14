from pathlib import PurePath

basedir = PurePath(__file__).parent
DATABASE = "flasktaskr.db"
USERNAME = 'admin'
PASSWORD = 'admin'
CSRF_ENABLED = True
SECRET_KEY = b'\xbd\xbb+\xaag\xa9I\x8a\x07\x11\xa2H>\xbaA\n\x00\\f\xf3\x96\xee\xbb\x97'

DEBUG = False

DATABASE_PATH = basedir.joinpath(DATABASE)

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + str(DATABASE_PATH)