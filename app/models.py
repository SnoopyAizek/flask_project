from . import db

ROLE_USER = 0
ROLE_ADMIN = 1


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), unique=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    role = db.Column(db.SmallInteger, default=ROLE_USER)

    def to_dict(self):
        data = {
            'id': self.id,
            'username': self.username,
            'email': self.email
        }
        return data

    def __str__(self):
        return f'User: {self.username}'
