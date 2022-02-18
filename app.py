from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = "manbearpig"

@app.route("/hello")
def index():
    flash("What is your USERID?")
    return render_template("index.html")

@app.route("/greet", methods=["POST", "GET"])
def greet():
    request.form["name_input"]
    flash("Hello " + str(request.form["name_input"]) + ", great to see you again! ")
    return render_template('index.html')
app.run(debug=True)