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
	melon_list = model.get_all_melons()
	return render_template("all_melons.html", melon_list = melon_list)



if __name__ == "__main__":
	app.run(debug=True)