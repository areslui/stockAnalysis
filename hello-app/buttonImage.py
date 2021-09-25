from flask import Flask
from flask.templating import render_template

app = Flask(__name__)


@app.route("/")
def hello():
    return render_template("buttonImage.html")


@app.route("/images")
def get_img():
    return "airPlane.jpg"


app.add_url_rule("/", view_func=hello)
app.add_url_rule("/images", view_func=get_img)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
