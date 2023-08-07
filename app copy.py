from flask import Flask, request, render_template
import numpy as np
import pandas as pd

from sklearn.preprocessing import StandardScaler
from src.pipeline.predict_pipeline import CustomData, PredictPipeline

application = Flask(__name__)

app = application

# Route for a home page


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/predictdata', methods=['GET', 'POST'])
def predict_datapoint():
    if request.method == 'GET':
        return render_template('home.html')
    else:
        data = CustomData(
                        SIM_COMPANY=request.form.get('SIM_COMPANY'),
                        VALIDITY=request.form.get('VALIDITY'),
                        DATA_PER_DAY=request.form.get('DATA_PER_DAY'),
                        ADDITIONAL_DATA = request.form.get('ADDITIONAL_DATA'),
                        SMS_PER_DAY = request.form.get('SMS_PER_DAY'),
                        ADDITIONAL_SMS = request.form.get('ADDITIONAL_SMS'),
                        DISNEY_HOTSTAR = request.form.get('DISNEY_HOTSTAR'),
                        COST_PER_DAY = request.form.get('COST_PER_DAY')
        
        )

        pred_df=data.get_data_as_data_frame()
        print(pred_df)
        print("Before Prediction")

        predict_pipeline=PredictPipeline()
        print("Mid Prediction")
        results=predict_pipeline.predict(pred_df)
        print("after Prediction")
        #return render_template('home.html', results = results[0])
        return render_template('predict.html', results = float(results[0]))


if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 9090)
    # app.run(debug=True)



