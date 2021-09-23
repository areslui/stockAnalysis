from flask import Flask, render_template
import os

IMAGE_FOLDER = os.path.join('static', 'images')

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = IMAGE_FOLDER

@app.route('/')
def show_index():
    full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'airPlane.jpg')
    return render_template("showImage.html", user_image = full_filename)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)