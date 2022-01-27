from flask import render_template, Blueprint

phome = Blueprint("phome", __name__, template_folder = "templates", url_prefix="")
@phome.route("/home")
@phome.route("/")
def landing():
	return render_template('home.html')