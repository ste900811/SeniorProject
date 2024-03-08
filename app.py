from flask import Flask, render_template, request
import pickle
import pandas as pd
import json

app = Flask(__name__)

with open("model_pickle.pkl", "rb") as f:
  clf = pickle.load(f)
columns=['Sex', 'Age', 'Race', 'Diastolic', 'Systolic', 'Pulse', 'BMI', 'HDL', 'Trig', 'LDL', 'TCHOL', 'kidneys_eGFR', 'Diabetes', 'CurrentSmoker', 'isActive']
startingValue = [2,50,1,66.67,104.0,82.0,42.6,31,204,113,185,117.01,2,2,2]
startingData = dict(zip(columns, startingValue))

@app.route('/', methods=['GET', 'POST'])
def home():
  if request.method == 'POST':
    data = dict(request.form)
    input = [int(data['Sex']), int(data['Age']), int(data['Race']), float(data['Diastolic']), 
              float(data['Systolic']), float(data['Pulse']), float(data['BMI']), int(data['HDL']), 
              int(data['Trig']), int(data['LDL']), int(data['TCHOL']), float(data['kidneys_eGFR']), 
              float(data['Diabetes']), int(data['CurrentSmoker']), float(data['isActive'])]
    test = pd.DataFrame([input], columns=columns)

    if clf.predict_proba(test)[0][0] >= 0.5:
      result = "High percentage has heart attack, check with doctor"
    else:
      result = "Low percentage has heart attack, keep healthy"
    
    dictData = dict(zip(columns, input))
    
    return render_template('home.html', result=result, data=dictData)
  return render_template('home.html', result="", data=startingData)

if __name__ == '__main__':
  app.run(debug=True)
