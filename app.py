from flask import Flask, render_template, redirect, url_for
import pickle
import pandas as pd

app = Flask(__name__)

with open("model_pickle.pkl", "rb") as f:
  clf = pickle.load(f)
data = [[2,50,1,66.66666667,104,82,42.6,31,204,113,185,117.0147731,2,2,2]]
test = pd.DataFrame(data, columns=['Sex', 'Age', 'Race', 'Diastolic', 'Systolic', 'Pulse', 'BMI', 'HDL', 'Trig', 'LDL', 'TCHOL', 'kidneys_eGFR', 'Diabetes', 'CurrentSmoker', 'isActive'])
result = clf.predict_proba(test)

@app.route('/')
def home():
  return render_template('home.html', result=result)

@app.route('/<name>')
def user(name):
  return f"Hello {name}! {result}"

@app.route('/admin')
def admin():
  return redirect(url_for('home'))

if __name__ == '__main__':
  app.run(debug=True)