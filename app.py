from flask import Flask, render_template, redirect, url_for
import joblib
import pandas as pd

app = Flask(__name__)

with open("model_joblib.pkl", "rb") as f:
  clf_joblib = joblib.load(f)
data = [[1004,1.41,2,50,1,1,66.66666667,104,82,42.6,31,204,113,185,117.0147731,2,2,2,2]]
test = pd.DataFrame(data, columns=['ParticipantID', 'Income', 'Sex', 'Age', 'Race', 'Edu', 'Diastolic', 'Systolic', 'Pulse', 'BMI', 'HDL', 'Trig', 'LDL', 'TCHOL', 'kidneys_eGFR', 'Diabetes', 'CurrentSmoker', 'isActive', 'isInsured'])
finalTest = test.drop(columns=["ParticipantID", "Income", "Edu", "isInsured"])

@app.route('/')
def home():
  return render_template('home.html')

@app.route('/<name>')
def user(name):
  return f"Hello {name}!"

@app.route('/admin')
def admin():
  return redirect(url_for('home'))

if __name__ == '__main__':
  app.run(debug=True)