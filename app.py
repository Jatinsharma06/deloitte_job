from flask import Flask

app=Flask(__name__)

@app.route("/info")

def jatin():
    return"welcome to the jatin's application"

app.run(host='0.0.0.0')
