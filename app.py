from flask import Flask
from controller.api import bp
from mysql_script.db_connect import db
from config import SQLALCHEMY_DATABASE_URI


app = Flask(__name__)
app.register_blueprint(bp)

app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
app.secret_key = 'asodfajsdofijac'

db.init_app(app)
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
