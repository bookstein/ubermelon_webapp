from flask import Flask, render_template, redirect
import model

app = Flask(__name__)

CONN = None
DB = None

@app.route("/")
def home():
	return render_template("index.html")

@app.route("/melons")
def show_all_melons():
	pass
	return render_template("all_melons.html", melons)



if __name__ == "__main__":
	app.run(debug=True)