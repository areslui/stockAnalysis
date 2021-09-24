from pandas_datareader import data
import matplotlib.pyplot as plt
import os


class StockModel:

    def __init__(self) -> None:
        pass


    def getStockData(self, flask):
        # get data
        stockData = data.DataReader("^TWII", "yahoo", "2021-08-31", "2021-09-23")
        # print(stockData)
        stockData60 = stockData.rolling(60, min_periods=1).mean()
        plt.plot(stockData.loc["2021"]["Close"])
        plt.plot(stockData60.loc["2021"]["Close"])
        self.processingWithImage(flask)
        return stockData, self.getImageName()


    def processingWithImage(self, app):
        app.config['UPLOAD_FOLDER'] = os.path.join('static', 'images')
        imagePath = os.path.dirname(os.path.abspath(__file__)) + '/static/images/'
        plt.savefig(os.path.join(imagePath, self.getImageName()))


    def getImageName(self):
        return 'stockFigure.png'
