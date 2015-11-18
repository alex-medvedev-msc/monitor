from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"


@app.route("/tree/16s")
def tree_16s():
	return render_template("tree_render.html")


if __name__ == "__main__":
    app.run(host='0.0.0.0')