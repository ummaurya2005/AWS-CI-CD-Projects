from flask import Flask,request,render_template
import numpy as np
import pandas as pd


from sklearn.preprocessing import StandardScaler
from src.pipeline.predict_pipeline import CustomData,PredictionPipeline

application=Flask(__name__)
app=application

## Route for the homepage
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predictdata',methods=['GET','POST'])
def predict_datapoint():
    if request.method=='GET':
        return render_template('home.html')
    else:
        data=CustomData(
            gender=request.form.get('gender'), # type: ignore
            race_ethnicity=request.form.get('race_ethnicity'), # type: ignore
            parental_level_of_education=request.form.get('parental_level_of_education'), # type: ignore
            lunch=request.form.get('lunch'), # type: ignore
            test_preparation_course=request.form.get('test_preparation_course'), # type: ignore
            reading_score=float(request.form.get('reading_score')),
            writing_score=float(request.form.get('writing_score')),
        )
        pred_df=data.get_data_as_data_frame()
        print(pred_df)

        predict_pipeline=PredictionPipeline()
        results=predict_pipeline.predict(pred_df)  # Fixed this line
        return render_template('home.html',results=results[0])

if __name__=="__main__":  # Fixed indentation - this should be at module level
    app.run(host="0.0.0.0",debug=True)
