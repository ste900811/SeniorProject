from flask import Flask, render_template, request
import pickle
import pandas as pd
import json

app = Flask(__name__)

with open("model_pickle.pkl", "rb") as f:
  clf = pickle.load(f)
columns=['Sex', 'Age', 'Race', 'Diastolic', 'Systolic', 'Pulse', 'BMI', 'HDL', 'Trig', 'LDL', 'TCHOL', 'kidneys_eGFR', 'Diabetes', 'CurrentSmoker', 'isActive']
startingValue = [2,50,1,66.66666667,104,82,42.6,31,204,113,185,117.0147731,2,2,2]
startingData = dict(zip(columns, startingValue))

testlist = [1,2,3]

@app.route('/', methods=['GET', 'POST'])
def home():
  if request.method == 'POST':
    data = dict(request.form)
    input = [[int(data['Sex']), int(data['Age']), int(data['Race']), float(data['Diastolic']), 
              float(data['Systolic']), float(data['Pulse']), float(data['BMI']), int(data['HDL']), 
              int(data['Trig']), int(data['LDL']), int(data['TCHOL']), float(data['kidneys_eGFR']), 
              float(data['Diabetes']), int(data['CurrentSmoker']), float(data['isActive'])]]
    test = pd.DataFrame(input, columns=columns)
    result = clf.predict_proba(test)
    print(data)
    print(data['Sex'])
    return render_template('home.html', result=result[0][0], data=data, li = testlist)
  print(startingData)
  print(startingData['Sex'])
  return render_template('home.html', result="", data=startingData, li = testlist)

if __name__ == '__main__':
  app.run(debug=True)
