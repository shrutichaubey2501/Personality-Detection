from flask import Flask, blueprints, session


from prediction.home import phome
from prediction.page import page



app = Flask(__name__)
app.secret_key = 'hello'


app.register_blueprint(phome, url_prefix= "/")
app.register_blueprint(page, url_prefix="/test_page")

if __name__ == '__main__':
	app.run(port = 80, debug = 'true')