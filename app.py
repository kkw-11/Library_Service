from flask import Flask
from api import bp
from db_connect import db

app = Flask(__name__)
app.register_blueprint(bp)

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:1234@localhost:3306/eliceproject"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
app.secret_key = 'asodfajsdofijac'

db.init_app(app)
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
