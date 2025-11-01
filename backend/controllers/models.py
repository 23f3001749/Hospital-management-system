from database import db
from flask_security import UserMixin,RoleMixin

class User(db.Model,UserMixin):
    id=db.Column(db.String(255),unique=True,nullable=False,primary_key=True)
    email=db.Column(db.String(255),unique=True,nullable=False)
    password=db.Column(db.String(255),nullable=False)
    active=db.Column(db.Boolean(),default=True)

    fs_uniquifier=db.Column(db.String(255),unique=True,nullable=False)
    fs_token_uniquifier=db.Column(db.String(255),unique=True,nullable=True)
    roles=db.relationship('Role',secondary='user_roles')

class Role(db.Model,RoleMixin):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(80),unique=True,nullable=False)
    desc=db.Column(db.String(255))