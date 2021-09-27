from flask import Flask, render_template, request
from flask.globals import session
from werkzeug.utils import redirect

app= Flask(__name__)
app.secret_key="secret"



@app.route("/", methods=["GET"])
def displayHome():
   
    return render_template("index.html")

@app.route("/submit", methods=["POST"])
  
def displayResult():
    session['Name']=request.form['Name']
    session['Location']=request.form['Location']
    session['Language']=request.form['Language']
    session['Comments']=request.form['Comments']
    
    


    return render_template("result.html")


if __name__ == "__main__":
    app.run(debug=True)
