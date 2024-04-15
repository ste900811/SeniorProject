# This is the main file for set up the kNN model. It will read the data from the diagnosis.csv file and do the feature extraction.
# If needs the detail explanation of the functions, please refer to the ipynb file.
import pandas as pd
import pickle
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler

# Read the data
data = pd.read_csv('../dataProcess/diagnosis.csv')

# Read the dictionary from pickle file
with open("../pickleFiles/diagnosisIntToLabel.pkl", "rb") as f:
  diagnosisIntToLabel = pickle.load(f)
genderLabel = {"M": 0, "F": 1}

# Set up the model X and y
y = data["DIAGNOSIS"]
X = data.drop(["DIAGNOSIS"], axis=1)

# Standardize the data
scaler = StandardScaler()
X = scaler.fit_transform(X.to_numpy())

# Create the prediction data
result = set()
neighbors = 5
predData = scaler.transform([[72.2, 1.8, 0, 75]])
print(f'Pred Data: {predData}')

# while the result is less than input, keep increasing the neighbors
while len(result) < 5:
  model = KNeighborsClassifier(n_neighbors=neighbors)
  model.fit(X, y)
  for d, pred in enumerate(model.predict_proba(predData)[0]):
    if pred > 0:
      result.add(diagnosisIntToLabel[d])
  neighbors += 1
  
print(result)
