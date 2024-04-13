

# import pandas as pd

# pd.set_option('display.max_columns', None)
# pd.set_option('display.max_rows', None)
# pd.set_option('display.width', 0)


# weightCount = 0
# heightCount = 0
# check = {}

# CHARTEVENTS = pd.read_csv('./mimic-iii-clinical-database-1.4/CHARTEVENTS.csv.gz', compression='gzip', usecols=['SUBJECT_ID', "CHARTTIME", "ITEMID", "HADM_ID"])
# for row in CHARTEVENTS.itertuples():
#   if row.ITEMID in {762, 763, 3723, 3580, 3581, 3582}:
#     weightCount += 1
#     if (row.SUBJECT_ID, row.HADM_ID) in check:
#       check[(row.SUBJECT_ID, row.HADM_ID)].append("weight")
#     else:
#       check[(row.SUBJECT_ID, row.HADM_ID)] = ["weight"]
#   if row.ITEMID in {920, 1394, 4187, 3486, 3485, 4188}:
#     heightCount += 1
#     if (row.SUBJECT_ID, row.HADM_ID) in check:
#       check[(row.SUBJECT_ID, row.HADM_ID)].append("height")
#     else:
#       check[(row.SUBJECT_ID, row.HADM_ID)] = ["height"]

# print(f'weightCount: {weightCount}') # 1823774
# print(f'heightCount: {heightCount}') # 340516

# fullInfo = 0
# for key in check:
#   if len(check[key]) == 2:
#     fullInfo += 1

# print(fullInfo)


print("\\")