from flask import Flask, render_template, redirect

app = Flask(__name__)

@app.route("/")
def home():
	return render_template("index.html")

@app.route("/melons")
def show_all_melons():
	pass
	query = """
	"""

	return render_template("all_melons.html", )



if __name__ == "__main__":
	app.run(debug=True)