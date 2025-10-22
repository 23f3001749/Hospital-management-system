from app import app
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash
db=SQLAlchemy(app)

class User(db.Model):
    user_id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    username=db.Column(db.String(32),unique=True,nullable=False)
    passhash=db.Column(db.String(80))
    email=db.Column(db.String(120),unique=True,nullable=True)
    role=db.Column(db.Integer,nullable=False)


with app.app_context():
    db.create_all()
    admin_user=User.query.filter_by(username='admin').first()
    if not admin_user:
        admin_user=User(username='admin',
        passhash=generate_password_hash('admin123'),
        role=0
        )
        db.session.add(admin_user)
        db.session.commit()
     

