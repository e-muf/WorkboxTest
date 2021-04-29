from flask import Flask, jsonify, request, render_template
from config import config
from models import db, User

def create_app(environment):
  app = Flask(__name__)
  app.config.from_object(environment)

  with app.app_context():
    db.init_app(app)
    db.create_all()

  return app

environment = config['development']
app = create_app(environment)

@app.route('/')
def home():
  return render_template('index.html')

@app.route('/users')
def get_users():
  users = db.session.query(User).all()
  return jsonify(users=[user.to_dict() for user in users])

@app.route('/users/<int:user_id>')
def get_user(user_id):
  user = db.session.query(User).get(user_id)
  if user is None:
    return jsonify(error={"Not Found": "User doesn't exist in database"}), 404
  
  return jsonify({'user': user.to_dict()})

@app.route('/users', methods=['POST'])
def create_user():
  new_user = User(
    name = request.form.get('name'),
    lastName = request.form.get('lastName'),
    address = request.form.get('address')
  )

  db.session.add(new_user)
  db.session.commit()

  return jsonify(response={'success': {'user_id': new_user.user_id}})

if __name__ == '__main__':
  app.run(debug=True)