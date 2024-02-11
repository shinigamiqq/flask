from flask import Blueprint, render_template

view_blueprint = Blueprint("view", __name__, static_folder="static", template_folder="templates")

@view_blueprint.route("/view")
def view():
    return render_template("view.html", values = users.query.all())