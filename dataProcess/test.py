import pandas as pd

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.width', 0)


weightCount = 0
heightCount = 0

CHARTEVENTS = pd.read_csv('./mimic-iii-clinical-database-1.4/CHARTEVENTS.csv.gz', compression='gzip', usecols=['SUBJECT_ID', "CHARTTIME", "ITEMID"])
for row in CHARTEVENTS.itertuples():
  if row.ITEMID in {762, 763, 3723, 3580, 3581, 3582}:
    weightCount += 1
  if row.ITEMID in {920, 1394, 4187, 3486, 3485, 4188}:
    heightCount += 1

print(f'weightCount: {weightCount}') # 1823774
print(f'heightCount: {heightCount}') # 340516
