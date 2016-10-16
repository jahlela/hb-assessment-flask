from flask import Flask, render_template, request, redirect
from flask_debugtoolbar import DebugToolbarExtension


app = Flask(__name__)


# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABC"


@app.route("/")
def index_page():
    """Show an index page."""

    return render_template("index.html")


@app.route('/application-form')
def form():
    """ Show the form page """

    return render_template("application-form.html")


@app.route('/application', methods=["POST"])
def render_response():
    """ Process form from POST request and render application-response.html 
        using the names, salary and job inputs """

    first_name = request.form.get("first_name")
    last_name = request.form.get("last_name")
    salary = request.form.get("salary")
    job = request.form.get("job")

    # Create more human-readable strings for possible jobs
    if job == "software_engineer":
        job = "Software Engineer"
    elif job == "qa_engineer":
        job = "QA Engineer"
    elif job == "product_manager":
        job == "Product Manager"
    
    return render_template("application-response.html",
                           first_name=first_name,
                           last_name=last_name,
                           salary=salary,
                           job=job)


@app.route('/application-response')
def response_redirect():
    """ Show application response """

    return redirect("/application")


if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    app.debug = True

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run(host="0.0.0.0")









