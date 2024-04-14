# This is the main file for data organization. It will extract the data from the raw data files and organize them into a more structured format.
# The ipynb file is used to test the functions in this file step by step, for the detailed explanation of the functions, please refer to the ipynb file.

import pandas as pd
import pickle

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.width', 0)

# read ADMISSIONS.csv.gz
mainDF = pd.read_csv('../mimic-iii-clinical-database-1.4/ADMISSIONS.csv.gz', compression='gzip', usecols=["SUBJECT_ID", "HADM_ID", "ADMITTIME", "DIAGNOSIS"])
print(f'Finish reading ADMISSIONS.csv.gz')

# Change the ADMITTIME only have date
mainDF["ADMITTIME"] = pd.to_datetime(mainDF["ADMITTIME"]).dt.date.astype(str)

# Dtop the rows if DIAGNOSIS is NaN
mainDF = mainDF.dropna(subset=["DIAGNOSIS"])

# Separate the DIAGNOSIS if there are multiple, and output to dataframe
data = []
for row in mainDF.itertuples():

  if "\\" in row.DIAGNOSIS:
    diagnosisString = row.DIAGNOSIS.split("\\")[0]
  else:
    diagnosisString = row.DIAGNOSIS
  
  if ";" in diagnosisString:
    diagnosisArray = diagnosisString.split(";")
  else:
    diagnosisArray = [diagnosisString]

  for d in diagnosisArray:
    data.append([row.SUBJECT_ID, row.HADM_ID, row.ADMITTIME, d])

diagnosisDF = pd.DataFrame(data, columns=["SUBJECT_ID", "HADM_ID", "ADMITTIME", "DIAGNOSIS"])
print(f'Finish separating the diagnosis')

# read CHARTEVENTS.csv.gz and drop the missing value, and change the CHARTTIME only have date
CHARTEVENTS = pd.read_csv('../mimic-iii-clinical-database-1.4/CHARTEVENTS.csv.gz', compression='gzip', usecols=["SUBJECT_ID", "HADM_ID", "CHARTTIME", "ITEMID", "VALUE"]).dropna()
CHARTEVENTS["CHARTTIME"] = pd.to_datetime(CHARTEVENTS["CHARTTIME"]).dt.date.astype(str)

# create weightHeightDict with key = (SUBJECT_ID, HADM_ID, CHARTTIME) and value = [weight, height]
weightHeightDict = {}
for row in CHARTEVENTS.itertuples():
  key = (row.SUBJECT_ID, row.HADM_ID, row.CHARTTIME)

  if row.ITEMID == 762 or row.ITEMID == 763 or row.ITEMID == 3723 or row.ITEMID == 3580: # weight unit is alreayd in KG
    if key in weightHeightDict and weightHeightDict[key][0] == -1: weightHeightDict[key][0] = float(row.VALUE)
    else: weightHeightDict[key] = [float(row.VALUE), -1]
  
  elif row.ITEMID == 3581: # weight unit is in LB
    if key in weightHeightDict and weightHeightDict[key][0] == -1: weightHeightDict[key][0] = float(row.VALUE)*0.4536
    else: weightHeightDict[key] = [float(row.VALUE)*0.4536, -1]
  
  elif row.ITEMID == 3582: # weight unit is in OZ
    if key in weightHeightDict and weightHeightDict[key][0] == -1: weightHeightDict[key][0] = float(row.VALUE)*0.0283
    else: weightHeightDict[key] = [float(row.VALUE)*0.0283, -1]
  
  elif row.ITEMID == 920 or row.ITEMID == 1394 or row.ITEMID == 4187 or row.ITEMID == 3486: # height unit is in inches
    if key in weightHeightDict and weightHeightDict[key][1] == -1: weightHeightDict[key][1] = float(row.VALUE)*0.0254
    else: weightHeightDict[key] = [-1, float(row.VALUE)*0.0254]

  elif row.ITEMID == 3485 or row.ITEMID == 4188: # height unit is in cm
    if key in weightHeightDict and weightHeightDict[key][1] == -1: weightHeightDict[key][1] = float(row.VALUE)*0.01
    else: weightHeightDict[key] = [-1, float(row.VALUE)*0.01]
print(f'Finish creating weightHeightDict')

# filter out if the key only have weight or height
for key, value in list(weightHeightDict.items()):
  if value[0] == -1 or value[1] == -1:
    del weightHeightDict[key]

# Plug the weight and height to the main dataframe
for row in diagnosisDF.itertuples():
  if (row.SUBJECT_ID, row.HADM_ID, row.ADMITTIME) in weightHeightDict:
    weight, height = weightHeightDict[(row.SUBJECT_ID, row.HADM_ID, row.ADMITTIME)]
    diagnosisDF.at[row.Index, "WEIGHT"] = weight
    diagnosisDF.at[row.Index, "HEIGHT"] = height
print(f'Finish plugging the weight and height')

# Drop the rows if the weight or height is NaN
diagnosisDF = diagnosisDF.dropna()

# read PATIENTS.csv.gz and change the DOB only have date
PATIENTS = pd.read_csv('../mimic-iii-clinical-database-1.4/PATIENTS.csv.gz', compression='gzip')
PATIENTS["DOB"] = pd.to_datetime(PATIENTS["DOB"]).dt.date.astype(str)

# create two dictionary with key = SUBJECT
patientBrith = dict(zip(PATIENTS["SUBJECT_ID"], PATIENTS["DOB"]))
patientGender = dict(zip(PATIENTS["SUBJECT_ID"], PATIENTS["GENDER"]))

# Plug the Gender to the main dataframe
for row in diagnosisDF.itertuples():
  diagnosisDF.at[row.Index, "GENDER"] = patientGender[row.SUBJECT_ID]

# Plug the Age to the main dataframe
for row in diagnosisDF.itertuples():
  admitYear, admitMonth, admitDate = row.ADMITTIME.split("-")
  birthYear, birthMonth, birthDate = patientBrith[row.SUBJECT_ID].split("-")
  patientMonth = int(admitYear)*12+int(admitMonth) - int(birthYear)*12+int(birthMonth)
  age, remainder = patientMonth//12, patientMonth%12
  if remainder >= 6: age += 1
  diagnosisDF.at[row.Index, "AGE"] = int(age)
print(f'Finish plugging the age and gender')

# Drop the SUBJECT_ID, HADM_ID, ADMITTIME, since it is not needed anymore
diagnosisDF = diagnosisDF.drop(columns=["SUBJECT_ID", "HADM_ID", "ADMITTIME"])

# Replace the typo in the data
for index, row in data.iterrows():
  if row["DIAGNOSIS"] == "CORNARY ARTERY DISEASE":
    data.at[index, "DIAGNOSIS"] = "CORONARY ARTERY DISEASE"

# Save the dataframe to csv
diagnosisDF.to_csv('diagnosis.csv', index=False)
