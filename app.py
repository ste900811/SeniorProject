from flask import Flask, render_template, request
import pickle
import pandas as pd

app = Flask(__name__)

# Load the model
with open("model_pickle.pkl", "rb") as f:
  clf = pickle.load(f)

# Columns of the dataset needed for the model
columns=['Sex', 'Age', 'Race', 'Diastolic', 'Systolic', 'Pulse', 'BMI', 'HDL', 'Trig', 'LDL', 'TCHOL', 'kidneys_eGFR', 'Diabetes', 'CurrentSmoker', 'isActive']

# Starting values for the input form
startingValue = [2,50,1,66.67,104.0,82.0,42.6,31,204,113,185,117.01,2,2,2]

# Create a dictionary with the columns and starting values
startingData = dict(zip(columns, startingValue))

# Create the home page with the input form
@app.route('/', methods=['GET', 'POST'])
def home():

  # If the form is submitted, which means the request method is POST, we will get the data from the form and store in data variable
  # Then we will create a dataframe with the input data and set test to the pandas format prepare to training
  # Use the model to predict the probability of having a heart attack, if probability is greater than 0.5, the result will be "High", otherwise "Low"
  # Create a dictionary with the input data and return the home page with the result and the input data
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
