
from flask import (Flask, render_template, request, redirect, session)
import numpy as np
import pandas as pd

from sklearn.preprocessing import StandardScaler
from src.pipeline.predict_pipeline import CustomData, PredictPipeline

application = Flask(__name__)
app = application
app.secret_key = 'ItShouldBeAnythingButSecret'
# Route for a home page

user = {"username": "admin", "password": "admin"}

@app.route('/login', methods = ['POST', 'GET'])
def login():
    if(request.method == 'POST'):
        username = request.form.get('username')
        password = request.form.get('password')     
        if username == user['username'] and password == user['password']:
            
            session['user'] = username
            return redirect('/predictdata')

        return "<h1>Wrong username or password</h1>"    #if the username or password does not matches 

    return render_template("login.html")

@app.route('/')
def index():
    return render_template('login.html')


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


@app.route('/logout')
def logout():
    session.pop('user')
    return redirect('/login')

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 9090)
    # app.run(debug=True)



