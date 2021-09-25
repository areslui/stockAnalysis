from flask import Flask, render_template
import os
import StockModel as SM

app = Flask(__name__)

# preparing checkbox
# determin which checkbox has checked

# get table data
tableData, imageName = SM.getStockData(app)


@app.route("/")
def html_table():
    full_filename = os.path.join(app.config['UPLOAD_FOLDER'], imageName)
    return render_template("stockData.html",
                           tables=[tableData.to_html(classes="Data")],
                           titles=tableData.columns.values,
                           user_image=full_filename)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080)
