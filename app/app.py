from flask import Flask
from inventoryAPI import inventory_api
import models
import os

app = Flask(__name__)

db_user = os.environ.get('DB_USER')
db_pass = os.environ.get('DB_PASS')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'ThisIsSecretKey'
app.config[
    'SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://' + db_user + ':' + db_pass + '@localhost/inventory_test_db?auth_plugin=mysql_native_password'

models.init_app(app)
models.create_tables(app)
app.register_blueprint(inventory_api)


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run(port=5004, debug=True)
