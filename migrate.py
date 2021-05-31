from app import app
from db import db

db.init_app(app)

if __name__ == '__main__':
    db.create_all(app=app)