from flask import Flask, render_template, request, redirect, jsonify

server = Flask(__name__)

@server.route("/")
def sign_in():
    return render_template("sign_in.html")

@server.route("/home")
def home():
    return render_template("home.html")

@server.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@server.route("/chat_bot")
def chat_bot():
    return render_template("chat_bot.html")

@server.route("/submit", methods=["POST"])
def submit():
    # collecting username and password
    username = request.form.get("username")
    password = request.form.get("password")

    # simple authentication
    valid_username = ["John", "Jane", "Jack", "Jill"]
    pass_code = "12345UPER"
    if (username.title() in valid_username and password == pass_code):
        return redirect("/chat_bot", 302)
    else:
        return redirect("/")

# the code below is for the chatbot respose
@server.route("/response", methods=["POST"])
def get_bot_response():
    # Use request.json because we will send data from JS as JSON
    data = request.json
    user_message = data.get("message", "").lower()

    # Simple logic for bot responses
    if "hello" in user_message or "hi" in user_message:
        bot_answer = "Hello! How can I help you today?"
    elif "time" in user_message:
        from datetime import datetime
        bot_answer = f"The current time is {datetime.now().strftime('%H:%M:%S')}."
    else:
        bot_answer = f"You said: '{user_message}'. I'm still learning, but that sounds interesting!"

    # Return the response as JSON
    return jsonify({"reply": bot_answer})





if __name__ == "__main__":
    server.run(debug= True, host="0.0.0.0", port= 7070)