from flask import Flask, render_template, request
import pickle
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)

# Senior project initial setup
# Read the data, dictionary and scaler from pickle file
data = pd.read_csv('./dataProcess/diagnosis_final.csv')
with open("./pickleFiles/diagnosisIntToLabel.pkl", "rb") as f:
  diagnosisIntToLabel = pickle.load(f)
with open("./pickleFiles/scaler.pkl", "rb") as f:
  scaler = pickle.load(f)

# Set up the model X and y
X, y = data.drop(["DIAGNOSIS"], axis=1), data["DIAGNOSIS"]
columns0 = ["WEIGHT", "HEIGHT", "GENDER", "AGE"]
startingValue0 = [72.2, 1.8, 0, 75]
startingData0 = dict(zip(columns0, startingValue0))

def prediction(input):
  result, neighbors = set(), 5
  data = scaler.transform([input])
  while len(result) < 5:
    model = KNeighborsClassifier(n_neighbors=neighbors)
    model.fit(X, y)
    for d, pred in enumerate(model.predict_proba(data)[0]):
      if pred > 0:
        result.add(diagnosisIntToLabel[d])
    neighbors += 1
  return result


# Load the model and starting value for the machine learning project 1
with open("./pickleFiles/aml1.pkl", "rb") as f:
  clf = pickle.load(f)

# Columns and starting value for for the machine learning project 1
# Then create a dictionary pass into html file for front end display
columns1=['Sex', 'Age', 'Race', 'Diastolic', 'Systolic', 'Pulse', 'BMI', 'HDL', 
         'Trig', 'LDL', 'TCHOL', 'kidneys_eGFR', 'Diabetes', 'CurrentSmoker', 'isActive']
startingValue1 = [2,50,1,66.67,104.0,82.0,42.6,31,204,113,185,117.01,2,2,2]
startingData1 = dict(zip(columns1, startingValue1))

# Create the home page with the input form, this is the main program locate
@app.route('/', methods=['GET', 'POST'])
def home():

  # If the form is submitted, which means the request method is POST, we will get the data from the form and store in data variable
  # Then we will create a dataframe with the input data and set test to the pandas format prepare to training
  # Use the model to predict the probability of having a heart attack, if probability is greater than 0.5, the result will be "High", otherwise "Low"
  # Create a dictionary with the input data and return the home page with the result and the input data
  if request.method == 'POST':
    data = dict(request.form)
    input = [float(data['WEIGHT']), float(data['HEIGHT']), float(data['GENDER']), float(data['AGE'])]
    test = pd.DataFrame([input], columns=columns0)

    result = prediction(input)
    dictData = dict(zip(columns0, input))
    
    return render_template('home.html', result=result, data=dictData)
  print(startingData0)
  return render_template('home.html', result="", data=startingData0)

# Create the machine learning project 1 page, this is for the demo purpose
@app.route('/aml1', methods=['GET', 'POST'])
def aml1():

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
    test = pd.DataFrame([input], columns=columns1)

    if clf.predict_proba(test)[0][0] >= 0.5:
      result = "High percentage has heart attack, check with doctor"
    else:
      result = "Low percentage has heart attack, keep healthy"
    
    dictData = dict(zip(columns1, input))
    
    return render_template('aml1.html', result=result, data=dictData)
  
  return render_template('aml1.html', result="", data=startingData1)

if __name__ == '__main__':
  app.run(debug=True)
