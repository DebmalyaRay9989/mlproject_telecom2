
from flask import Flask,render_template,flash, redirect,url_for,session,logging,request
from flask_sqlalchemy import SQLAlchemy

import numpy as np  
import pandas as pd

from sklearn.preprocessing import StandardScaler
from src.pipeline.predict_pipeline import CustomData, PredictPipeline


application = Flask(__name__)
app = application

#configuring the database
app.config['SQLALCHEMY_DATABASE_URI']= 'postgres://mltelecom:ggtDwvWnajIQw4VDNTaJwBbY02LXUVIF@dpg-cj946sqvvtos739f05j0-a.oregon-postgres.render.com/mltelecom'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

db = SQLAlchemy(app)

class user(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    email = db.Column(db.String(120))
    password = db.Column(db.String(80))


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods = ['POST', 'GET'])
def login():
    if request.method == "POST":
        uname = request.form["uname"]
        passw = request.form["passw"]

        login = user.query.filter_by(username=uname, password=passw).first()
        if login is not None:
            return redirect('/predictdata')
    return render_template("login.html")


@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "POST":
        uname = request.form['uname']
        mail = request.form['mail']
        passw = request.form['passw']

        register = user(username = uname, email = mail, password = passw)
        db.session.add(register)
        db.session.commit()

        return redirect('/login')
    return render_template("register.html")


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
	session.pop('uname', None)
	return redirect('/')


if __name__ == "__main__":
    db.create_all()
    app.run(host = "0.0.0.0", port = 9090)
    # app.run(debug=True)



