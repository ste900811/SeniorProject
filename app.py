from flask import Flask, render_template, redirect, url_for, request
import pickle
import pandas as pd
import random

app = Flask(__name__)

with open("model_pickle.pkl", "rb") as f:
  clf = pickle.load(f)
data = [[2,50,1,66.66666667,104,82,42.6,31,204,113,185,117.0147731,2,2,2]]
test = pd.DataFrame(data, columns=['Sex', 'Age', 'Race', 'Diastolic', 'Systolic', 'Pulse', 'BMI', 'HDL', 'Trig', 'LDL', 'TCHOL', 'kidneys_eGFR', 'Diabetes', 'CurrentSmoker', 'isActive'])
result = clf.predict_proba(test)

@app.route('/', methods=['GET', 'POST'])
def home():
  if request.method == 'POST':
    i = random.randint(0, 100)
    return render_template('home.html', result=result, message=i)
  return render_template('home.html', result=result)

@app.route('/display_message')
def display_message():
  return redirect(url_for('home'), message="Hello, display success!")

@app.route('/<name>')
def user(name):
  return f"Hello {name}! {result}"

@app.route('/admin')
def admin():
  return redirect(url_for('home'))

if __name__ == '__main__':
  app.run(debug=True)
