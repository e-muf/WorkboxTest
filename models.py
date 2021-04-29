from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class User(db.Model):
  __tablename__ = 'user'
  user_id   = db.Column(db.Integer, primary_key = True)
  name      = db.Column(db.String(40), nullable=False)
  lastName  = db.Column(db.String(100), nullable=False)
  address   = db.Column(db.String(250), nullable=False)

  def to_dict(self):
    return {column.name: getattr(self, column.name) for column in self.__table__.columns}
  