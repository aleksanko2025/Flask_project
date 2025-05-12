from flask import Flask, render_template
app = Flask(__name__)	


@app.route('/')
def portada():
    return render_template("portada.html")

@app.route('/inicio')
def inicio():
    return render_template("inicio.html") 


app.run("0.0.0.0",5000,debug=True)