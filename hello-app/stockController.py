from showImage import IMAGE_FOLDER
from flask import Flask, render_template
from pandas_datareader import data
import matplotlib.pyplot as plt
import os
# import pandas as pd
# import numpy as np

IMAGE_FOLDER = os.path.join('static', 'images')
# print('image folder' + IMAGE_FOLDER)
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = IMAGE_FOLDER

# get data from source
stockData = data.DataReader("^TWII", "yahoo", "2021-08-31","2021-09-23")
# print(stockData)
stockData60 = stockData.rolling(60, min_periods=1).mean()
plt.plot(stockData["2021"]["Close"])
plt.plot(stockData60["2021"]["Close"])

my_path = os.path.dirname(os.path.abspath(__file__)) + '/static/images/'
my_file = 'stockFigure.png'
plt.savefig(os.path.join(my_path, my_file))
print(my_path)
# plt.show()
# print(plt.get_backend())

@app.route("/")
def html_table():
    full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'stockFigure.png')
    return render_template("stockData.html", 
    tables = [stockData.to_html(classes="Data")], 
    titles = stockData.columns.values, 
    user_image = full_filename)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080)