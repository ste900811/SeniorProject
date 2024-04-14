# This is the main file for set up the kNN model. It will read the data from the diagnosis.csv file and do the feature extraction.
# If needs the detail explanation of the functions, please refer to the ipynb file.

# Read the dataframe and extraction the feature
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler

# Read the data
data = pd.read_csv('../dataProcess/diagnosis.csv')

# Do feature extraction on Diagnosis and Gender
diagnosisLabelToInt = dict([(d, index) for index, d in enumerate(set(data["DIAGNOSIS"]))])
diagnosisIntToLabel = dict([(index, d) for index, d in enumerate(set(data["DIAGNOSIS"]))])
genderLabel = {"M": 0, "F": 1}

# Replace the string with the index
data["DIAGNOSIS"] = [diagnosisLabelToInt[n] for n in data["DIAGNOSIS"]]
data["GENDER"] = [genderLabel[n] for n in data["GENDER"]]

# Set up the model X and y
y = data["DIAGNOSIS"]
X = data.drop(["DIAGNOSIS"], axis=1)

# Standardize the data
scaler = StandardScaler()
X = scaler.fit_transform(X.to_numpy())

result = set()
neighbors = 5
predData = scaler.transform([[72.2, 1.8, 0, 75]])
print(predData)

# Train the model
while len(result) < 5:
  model = KNeighborsClassifier(n_neighbors=neighbors)
  model.fit(X, y)
  print(model.predict_proba(predData)[0])
  for d, pred in enumerate(model.predict_proba(predData)[0]):
    if pred > 0:
      result.add(diagnosisIntToLabel[d])
  
print(result)
