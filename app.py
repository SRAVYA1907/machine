from flask import Flask, render_template, request, jsonify
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from datetime import datetime, timedelta
from flask_cors import CORS
import warnings
warnings.filterwarnings("ignore")
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)


app = Flask(__name__)
CORS(app)

@app.route('/cncprediction')
def index():
    return render_template('index/index.html')
@app.route('/cncprediction-homepage')
def Home():
    return render_template('Home/Home.html')
@app.route('/cncprediction-zones')
def Zones():
    return render_template('Zones/zones.html')
@app.route('/cncprediction-faq')
def FAQ():
    return render_template('FAQ/faq.html')
@app.route('/cncprediction-download')
def Download():
    return render_template('Download/Download.html')
@app.route('/cncprediction-modig')
def modig():
    return render_template('Status/Status1.html')
@app.route('/cncprediction-jyoti')
def jyoti():
    return render_template('Status/Status2.html')
@app.route('/cncprediction-dmg')
def dmg():
    return render_template('Status/Status3.html')
@app.route('/cncprediction-mazak')
def mazak():
    return render_template('Status/Status4.html')
@app.route('/pre')
def pre():
    return render_template('pre/pre.html')

# def load_model():

#     return RandomForestRegressor(n_estimators=100)

# def predict_data(data):

#     return "Placeholder prediction"

# @app.route('/predict', methods=['POST'])
# def predict():
#     data = request.json
#     machine = data['machine']
#     start_date = data['startDate']
#     end_date = data['endDate']
#     data = load_data(machine, start_date, end_date)

#     prediction = predict_data(data)

#     return jsonify({'prediction': prediction})

# def load_data(machine, start_date, end_date):
#     file_path = f"C:\\Users\\tsravya\\OneDrive - RealPage\\Desktop\\Project\\templates\\pre\\mo.csv"
#     data = pd.read_csv(file_path, infer_datetime_format=True)
#     data['Date'] = pd.to_datetime(data['Date'])
#     data.set_index('Date', inplace=True)
#     start_date = datetime.strptime(start_date, "%Y-%m-%dT%H:%M:%S.%fZ")
#     end_date = datetime.strptime(end_date, "%Y-%m-%dT%H:%M:%S.%fZ")
#     data = data.loc[start_date:end_date]
#     return data

if __name__ == "__main__":
    app.run(debug=True)