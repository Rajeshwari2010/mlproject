from flask import Flask, jsonify, request,render_template
import numpy as np
import pandas as pd

from sklearn.preprocessing import StandardScaler
import pickle
from src.pipeline.predict_pipeline import CustomData,PredictPipeline



app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predictdata', methods=['GET', 'POST'])
def predict_datapoint():
    if request.method == 'POST':
        data=CustomData(
            gender=request.form.get('gender'),
            race_ethnicity=request.form.get('ethnicity'),
            lunch=request.form.get('lunch'),
            parental_level_of_education=request.form.get('parental_level_of_education'),
            test_preparation_course=request.form.get('test_preparation_course'),
            writing_score=int(request.form.get('writing_score')),
            reading_score=int(request.form.get('reading_score'))
        )

        pred_df=data.get_data_as_dataframe()
        print(pred_df)
        prediction_pipeline=PredictPipeline()
        prediction=prediction_pipeline.predict(pred_df)

        return render_template('home.html',results=prediction[0])

    if request.method == 'GET':
        return render_template('home.html')
    


if __name__=="__main__":
    app.run(host="0.0.0.0",port=8080,debug=True)