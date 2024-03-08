from flask import Flask, render_template, redirect, url_for, request
import pickle
import pandas as pd
import random

app = Flask(__name__)

with open("model_pickle.pkl", "rb") as f:
  clf = pickle.load(f)
columns=['Sex', 'Age', 'Race', 'Diastolic', 'Systolic', 'Pulse', 'BMI', 'HDL', 'Trig', 'LDL', 'TCHOL', 'kidneys_eGFR', 'Diabetes', 'CurrentSmoker', 'isActive']

# Sample for input and test
# data = [[2,50,1,66.66666667,104,82,42.6,31,204,113,185,117.0147731,2,2,2]]
# test = pd.DataFrame(data, columns=columns)

@app.route('/', methods=['GET', 'POST'])
def home():
  if request.method == 'POST':
    i = random.randint(0, 100)
    data = dict(request.form)
    print(data)
    input = [[int(data['Sex']), int(data['Age']), int(data['Race']), float(data['Diastolic']), 
              float(data['Systolic']), float(data['Pulse']), float(data['BMI']), int(data['HDL']), 
              int(data['Trig']), int(data['LDL']), int(data['TCHOL']), float(data['kidneys_eGFR']), 
              float(data['Diabetes']), int(data['CurrentSmoker']), float(data['isActive'])]]
    test = pd.DataFrame(input, columns=columns)
    result = clf.predict_proba(test)
    print(result)
    return render_template('home.html', result=result[0][0], message=i)
  return render_template('home.html', result="")

if __name__ == '__main__':
  app.run(debug=True)
