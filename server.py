from flask import Flask, render_template, request
from flask.globals import session
from werkzeug.utils import redirect

app= Flask(__name__)
app.secret_key="secret"



@app.route("/", methods=["POST"])
def displayHome():
   
    return render_template("index.html")

@app.route("/result", methods=["POST"])
  
def displayResult():
    name=request.form['Name']
    location=request.form['Location']
    language=request.form['Language']
    
    return render_template("result.html")


if __name__ == "__main__":
    app.run(debug=True)
