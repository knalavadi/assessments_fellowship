from flask import Flask, render_template, session
from flask_debugtoolbar import DebugToolbarExtension


app = Flask(__name__)


# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABC"

@app.route("/")
def index_page():
    """Show an index page."""

    

    return render_template("application-form.html")

@app.route("/application-form", methods=["POST"])
def form_submission():

    flash("Message flash from index")

    firstname= request.form.get("firstname")
    lastname= request.form.get("lastname")
    salary= request.form.get("salary")
    job = request.form.get("job")

    render_template("application-response.html", 
                       firstname=firstname, lastname=lastname, salary=salary, job=job)

#i used form.get for this but the result after submit isnt working - im 
#a bit confused about template inheritence 


if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    app.debug = True

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run(host="0.0.0.0")

