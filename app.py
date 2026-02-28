from flask import Flask, render_template, request, redirect, jsonify


app = Flask(__name__)

@app.route("/")
def sign_in():
    return render_template("sign_in.html")

@app.route("/submit", methods = ["POST"])
def submit():
    username = request.form.get("username")
    password = request.form.get("password")
    if username == "John" and password == "123456":
        return redirect("/dashboard")
    else:
        return "Credentials are incorrect", 401

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@app.route("/home")
def home():
    return render_template("home.html")

if __name__ == "__main__":
    app.run(debug= True, host = "0.0.0.0", port = 3030)