from flask import Flask, render_template, request
import os
import StockModel as SM

app = Flask(__name__)

# preparing checkbox
# determin which checkbox has checked

# get table data
# tableData, imageName = SM.getStockData(app)
tableData = None
imageName = None


@app.route('/', methods=['GET', 'POST'])
def html_table():
    print(request.method)

    if request.method == 'POST':
        print('button pressed')
        checked = request.form.get('test', default=False, type=bool)
        print('checked', checked)
        if request.form.get('proceed') == 'proceed':
            print('Button ID: ', request.form.get('proceed'))
            tableData, imageName = SM.getStockData(app)
            full_filename = os.path.join(
                app.config['UPLOAD_FOLDER'], imageName)

            return render_template('stockData.html',
                                   tables=[tableData.to_html(classes='Data')],
                                   titles=tableData.columns.values,
                                   user_image=full_filename)
        else:
            return render_template('stockData.html')
    elif request.method == 'GET':
        print('No POST back call!')

    return render_template('stockData.html')


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080)
