import pandas as pd


pd.set_option('display.max_columns', None)
pd.set_option('display.width', 0)

# len(index) = 58976
ADMISSIONS = pd.read_csv('./mimic-iii-clinical-database-1.4/ADMISSIONS.csv.gz', compression='gzip', dtype={'ROW_ID'               : "int64",
                                                                                                           'SUBJECT_ID'           : "int64",
                                                                                                           'HADM_ID'              : "int64",
                                                                                                           'ADMITTIME'            : "string",
                                                                                                           'DISCHTIME'            : "string",
                                                                                                           'DEATHTIME'            : "string",
                                                                                                           'ADMISSION_TYPE'       : "string",
                                                                                                           'ADMISSION_LOCATION'   : "string",
                                                                                                           'DISCHARGE_LOCATION'   : "string",
                                                                                                           'INSURANCE'            : "string",
                                                                                                           'LANGUAGE'             : "string",
                                                                                                           'RELIGION'             : "string",
                                                                                                           'MARITAL_STATUS'       : "string",
                                                                                                           'ETHNICITY'            : "string",
                                                                                                           'EDREGTIME'            : "string",
                                                                                                           'EDOUTTIME'            : "string",
                                                                                                           'DIAGNOSIS'            : "string",
                                                                                                           'HOSPITAL_EXPIRE_FLAG' : "int64",
                                                                                                           'HAS_CHARTEVENTS_DATA' : "int64"})
print(ADMISSIONS.head(20))

# # len(index) = 34499
# CALLOUT = pd.read_csv('./mimic-iii-clinical-database-1.4/CALLOUT.csv.gz', compression='gzip', dtype={'ROW_ID'                 : "int64",
#                                                                                                      'SUBJECT_ID'             : "int64",
#                                                                                                      'HADM_ID'                : "int64",
#                                                                                                      'SUBMIT_WARDID'          : "float64",
#                                                                                                      'SUBMIT_CAREUNIT'        : "string",
#                                                                                                      'CURR_WARDID'            : "float64",
#                                                                                                      'CURR_CAREUNIT'          : "string",
#                                                                                                      'CALLOUT_WARDID'         : "int64",
#                                                                                                      'CALLOUT_SERVICE'        : "string",
#                                                                                                      'REQUEST_TELE'           : "int64",
#                                                                                                      'REQUEST_RESP'           : "int64",
#                                                                                                      'REQUEST_CDIFF'          : "int64",
#                                                                                                      'REQUEST_MRSA'           : "int64",
#                                                                                                      'REQUEST_VRE'            : "int64",
#                                                                                                      'CALLOUT_STATUS'         : "string",
#                                                                                                      'CALLOUT_OUTCOME'        : "string",
#                                                                                                      'DISCHARGE_WARDID'       : "float64",
#                                                                                                      'ACKNOWLEDGE_STATUS'     : "string",
#                                                                                                      'CREATETIME'             : "string",
#                                                                                                      'UPDATETIME'             : "string",
#                                                                                                      'ACKNOWLEDGETIME'        : "string",
#                                                                                                      'OUTCOMETIME'            : "string",
#                                                                                                      'FIRSTRESERVATIONTIME'   : "string",
#                                                                                                      'CURRENTRESERVATIONTIME' : "string"})


# # len(index) = 7567
# CAREGIVERS = pd.read_csv('./mimic-iii-clinical-database-1.4/CAREGIVERS.csv.gz', compression='gzip', dtype={'ROW_ID'      : "int64",
#                                                                                                            'CGID'        : "int64",
#                                                                                                            'LABEL'       : "string",
#                                                                                                            'DESCRIPTION' : "string"})

# # len(index) = 100000000 + 100000000 + 100000000 + 30712483 = 330712483
# row = 100000000

# CHARTEVENTS0 = pd.read_csv('./mimic-iii-clinical-database-1.4/CHARTEVENTS.csv.gz', compression='gzip', dtype={'ROW_ID'      : "int64",
#                                                                                                              'SUBJECT_ID'  : "int64",
#                                                                                                              'HADM_ID'     : "int64",
#                                                                                                             #  'ICUSTAY_ID'  : "int64",
#                                                                                                              'ITEMID'      : "int64",
#                                                                                                             #  'CHARTTIME'   : "string",
#                                                                                                             #  'STORETIME'   : "string",
#                                                                                                             #  'CGID'        : "int64",
#                                                                                                             #  'VALUE'       : "float64",
#                                                                                                             #  'VALUENUM'    : "float64",
#                                                                                                              'VALUEUOM'    : "string",
#                                                                                                             #  'WARNING'     : "int64",
#                                                                                                             #  'ERROR'       : "int64",
#                                                                                                             #  'RESULTSTATUS': "float64",
#                                                                                                             #  'STOPPED'     : "float64"
#                                                                                                              }, keep_default_na=False, na_filter=False, nrows=row)
# wCount = 0
# hCount = 0
# for row in CHARTEVENTS0.itertuples():
#   if row.ITEMID in {762, 763, 3723, 3580, 3582} and wCount < 10:
#     print(row)
#     wCount += 1
#   if row.ITEMID in {920, 1394, 4187, 3486, 3485, 4188} and hCount < 10:
#     print(row)
#     hCount += 1
#   if wCount == 10 and hCount == 10:
#     break

# CHARTEVENTS1 = pd.read_csv('./mimic-iii-clinical-database-1.4/CHARTEVENTS.csv.gz', compression='gzip', dtype={'ROW_ID'      : "int64",
#                                                                                                              'SUBJECT_ID'  : "int64",
#                                                                                                              'HADM_ID'     : "int64",
#                                                                                                             #  'ICUSTAY_ID'  : "int64",
#                                                                                                              'ITEMID'      : "int64",
#                                                                                                             #  'CHARTTIME'   : "string",
#                                                                                                             #  'STORETIME'   : "string",
#                                                                                                             #  'CGID'        : "int64",
#                                                                                                             #  'VALUE'       : "float64",
#                                                                                                             #  'VALUENUM'    : "float64",
#                                                                                                              'VALUEUOM'    : "string",
#                                                                                                             #  'WARNING'     : "int64",
#                                                                                                             #  'ERROR'       : "int64",
#                                                                                                             #  'RESULTSTATUS': "float64",
#                                                                                                             #  'STOPPED'     : "float64"
#                                                                                                              }, keep_default_na=False, na_filter=False, nrows=row, skiprows=[i for i in range(1, row+1)])

# CHARTEVENTS2 = pd.read_csv('./mimic-iii-clinical-database-1.4/CHARTEVENTS.csv.gz', compression='gzip', dtype={'ROW_ID'      : "int64",
#                                                                                                              'SUBJECT_ID'  : "int64",
#                                                                                                              'HADM_ID'     : "int64",
#                                                                                                             #  'ICUSTAY_ID'  : "int64",
#                                                                                                              'ITEMID'      : "int64",
#                                                                                                             #  'CHARTTIME'   : "string",
#                                                                                                             #  'STORETIME'   : "string",
#                                                                                                             #  'CGID'        : "int64",
#                                                                                                             #  'VALUE'       : "float64",
#                                                                                                             #  'VALUENUM'    : "float64",
#                                                                                                              'VALUEUOM'    : "string",
#                                                                                                             #  'WARNING'     : "int64",
#                                                                                                             #  'ERROR'       : "int64",
#                                                                                                             #  'RESULTSTATUS': "float64",
#                                                                                                             #  'STOPPED'     : "float64"
#                                                                                                              }, keep_default_na=False, na_filter=False, nrows=row, skiprows=[i for i in range(1, row * 2 + 1)])

# CHARTEVENTS3 = pd.read_csv('./mimic-iii-clinical-database-1.4/CHARTEVENTS.csv.gz', compression='gzip', dtype={'ROW_ID'      : "int64",
#                                                                                                              'SUBJECT_ID'  : "int64",
#                                                                                                              'HADM_ID'     : "int64",
#                                                                                                             #  'ICUSTAY_ID'  : "int64",
#                                                                                                              'ITEMID'      : "int64",
#                                                                                                             #  'CHARTTIME'   : "string",
#                                                                                                             #  'STORETIME'   : "string",
#                                                                                                             #  'CGID'        : "int64",
#                                                                                                             #  'VALUE'       : "float64",
#                                                                                                             #  'VALUENUM'    : "float64",
#                                                                                                              'VALUEUOM'    : "string",
#                                                                                                             #  'WARNING'     : "int64",
#                                                                                                             #  'ERROR'       : "int64",
#                                                                                                             #  'RESULTSTATUS': "float64",
#                                                                                                             #  'STOPPED'     : "float64"
#                                                                                                              }, keep_default_na=False, na_filter=False, nrows=row, skiprows=[i for i in range(1, row * 3 + 1)])


# # len(index) = 573146
# CPTEVENTS = pd.read_csv('./mimic-iii-clinical-database-1.4/CPTEVENTS.csv.gz', compression='gzip', dtype={'ROW_ID'          : "int64",
#                                                                                                          'SUBJECT_ID'      : "int64",
#                                                                                                          'HADM_ID'         : "int64",
#                                                                                                          'COSTCENTER'      : "string",
#                                                                                                          'CHARTDATE'       : "string",
#                                                                                                          'CPT_CD'          : "string",
#                                                                                                          'CPT_NUMBER'      : "float64",
#                                                                                                          'CPT_SUFFIX'      : "string",
#                                                                                                          'TICKET_ID_SEQ'   : "float64",
#                                                                                                          'SECTIONHEADER'   : "string",
#                                                                                                          'SUBSECTIONHEADER': "string",
#                                                                                                          'DESCRIPTION'     : "string"})


# # len(index) = 134
# D_CPT = pd.read_csv('./mimic-iii-clinical-database-1.4/D_CPT.csv.gz', compression='gzip', dtype={'ROW_ID'              : "int64",
#                                                                                                  'CATEGORY'            : "int64",
#                                                                                                  'SECTIONRANGE'        : "string",
#                                                                                                  'SECTIONHEADER'       : "string",
#                                                                                                  'SUBSECTIONRANGE'     : "string",
#                                                                                                  'SUBSECTIONHEADER'    : "string",
#                                                                                                  'CODESUFFIX'          : "string",
#                                                                                                  'MINCODEINSUBSECTION' : "int64",
#                                                                                                  'MAXCODEINSUBSECTION' : "int64"})


# # len(index) = 14567
# D_ICD_DIAGNOSES = pd.read_csv('./mimic-iii-clinical-database-1.4/D_ICD_DIAGNOSES.csv.gz', compression='gzip', dtype={'ROW_ID'      : "int64",
#                                                                                                                      'ICD9_CODE'   : "string", 
#                                                                                                                      'SHORT_TITLE' : "string", 
#                                                                                                                      'LONG_TITLE'  : "string"})


# # len(index) = 3882
# D_ICD_PROCEDURES = pd.read_csv('./mimic-iii-clinical-database-1.4/D_ICD_PROCEDURES.csv.gz', compression='gzip', dtype={'ROW_ID'      : "int64",
#                                                                                                                        'ICD9_CODE'   : "string",
#                                                                                                                        'SHORT_TITLE' : "string",
#                                                                                                                        'LONG_TITLE'  : "string"})


# len(index) = 12487
# weight index : 762, 763, 3723, 3580, 3581, 3582
# height index : 920, 1394, 4187, 3486, 3485, 4188
# D_ITEMS = pd.read_csv('./mimic-iii-clinical-database-1.4/D_ITEMS.csv.gz', compression='gzip', dtype={'ROW_ID'      : "int64",
#                                                                                                      'ITEMID'      : "int64",
#                                                                                                      'LABEL'       : "string",
#                                                                                                      'ABBREVIATION': "string",
#                                                                                                      'DBSOURCE'    : "string",
#                                                                                                      'LINKSTO'     : "string",
#                                                                                                      'CATEGORY'    : "string",
#                                                                                                      'UNITNAME'    : "string",
#                                                                                                      'PARAM_TYPE'  : "string",
#                                                                                                      'CONCEPTID'   : "string"})


# # len(index) = 753
# D_LABITEMS = pd.read_csv('./mimic-iii-clinical-database-1.4/D_LABITEMS.csv.gz', compression='gzip', dtype={'ROW_ID'      : "int64",
#                                                                                                            'ITEMID'      : "int64",
#                                                                                                            'LABEL'       : "string",
#                                                                                                            'FLUID'       : "string",
#                                                                                                            'CATEGORY'    : "string",
#                                                                                                            'LOINC_CODE'  : "string"})


# # len(index) = 4485937
# DATETIMEEVENTS = pd.read_csv('./mimic-iii-clinical-database-1.4/DATETIMEEVENTS.csv.gz', compression='gzip', dtype={'ROW_ID'      : "int64",
#                                                                                                                    'SUBJECT_ID'  : "int64",
#                                                                                                                    'HADM_ID'     : "float64",
#                                                                                                                    'ICUSTAY_ID'  : "float64",
#                                                                                                                    'ITEMID'      : "int64",
#                                                                                                                    'CHARTTIME'   : "string",
#                                                                                                                    'STORETIME'   : "string",
#                                                                                                                    'CGID'        : "int64",
#                                                                                                                    'VALUE'       : "string",
#                                                                                                                    'VALUEUOM'    : "string",
#                                                                                                                    'WARNING'     : "float64",
#                                                                                                                    'ERROR'       : "float64",
#                                                                                                                    'RESULTSTATUS': "float64",
#                                                                                                                    'STOPPED'     : "string"})


# # len(index) = 651047
# DIAGNOSES_ICD = pd.read_csv('./mimic-iii-clinical-database-1.4/DIAGNOSES_ICD.csv.gz', compression='gzip', dtype={'ROW_ID'     : "int64",
#                                                                                                                  'SUBJECT_ID' : "int64",
#                                                                                                                  'HADM_ID'    : "int64",
#                                                                                                                  'SEQ_NUM'    : "float64",
#                                                                                                                  'ICD9_CODE'  : "string"})


# # len(index) = 125557
# DRGCODES = pd.read_csv('./mimic-iii-clinical-database-1.4/DRGCODES.csv.gz', compression='gzip', dtype={'ROW_ID'        : "int64",
#                                                                                                        'SUBJECT_ID'    : "int64",
#                                                                                                        'HADM_ID'       : "int64",
#                                                                                                        'DRG_TYPE'      : "string",
#                                                                                                        'DRG_CODE'      : "int64",
#                                                                                                        'DESCRIPTION'   : "string",
#                                                                                                        'DRG_SEVERITY'  : "float64",
#                                                                                                        'DRG_MORTALITY' : "float64"})


# # len(index) = 61532
# ICUSTAYS = pd.read_csv('./mimic-iii-clinical-database-1.4/ICUSTAYS.csv.gz', compression='gzip', dtype={'ROW_ID'         : "int64",
#                                                                                                        'SUBJECT_ID'     : "int64",
#                                                                                                        'HADM_ID'        : "int64",
#                                                                                                        'ICUSTAY_ID'     : "int64",
#                                                                                                        'DBSOURCE'       : "string",
#                                                                                                        'FIRST_CAREUNIT' : "string",
#                                                                                                        'LAST_CAREUNIT'  : "string",
#                                                                                                        'FIRST_WARDID'   : "int64",
#                                                                                                        'LAST_WARDID'    : "int64",
#                                                                                                        'INTIME'         : "string",
#                                                                                                        'OUTTIME'        : "string",
#                                                                                                        'LOS'            : "float64"})


# # len(index) = 17527935
# INPUTEVENTS_CV = pd.read_csv('./mimic-iii-clinical-database-1.4/INPUTEVENTS_CV.csv.gz', compression='gzip', dtype={'ROW_ID'             : "int64",
#                                                                                                                    'SUBJECT_ID'        : "int64",
#                                                                                                                    'HADM_ID'           : "float64",
#                                                                                                                    'ICUSTAY_ID'        : "float64",
#                                                                                                                    'CHARTTIME'         : "string",
#                                                                                                                    'ITEMID'            : "int64",
#                                                                                                                    'AMOUNT'            : "float64",
#                                                                                                                    'AMOUNTUOM'         : "string",
#                                                                                                                    'RATE'              : "float64",
#                                                                                                                    'RATEUOM'           : "string",
#                                                                                                                    'STORETIME'         : "string",
#                                                                                                                    'CGID'              : "float64",
#                                                                                                                    'ORDERID'           : "int64",
#                                                                                                                    'LINKORDERID'       : "int64",
#                                                                                                                    'STOPPED'           : "string",
#                                                                                                                    'NEWBOTTLE'         : "float64",
#                                                                                                                    'ORIGINALAMOUNT'    : "float64",
#                                                                                                                    'ORIGINALAMOUNTUOM' : "string",
#                                                                                                                    'ORIGINALROUTE'     : "string",})


# # len(index) = 3618991
# INPUTEVENTS_MV = pd.read_csv('./mimic-iii-clinical-database-1.4/INPUTEVENTS_MV.csv.gz', compression='gzip', dtype={'ROW_ID'                        : "int64",
#                                                                                                                    'SUBJECT_ID'                    : "int64",
#                                                                                                                    'HADM_ID'                       : "float64",
#                                                                                                                    'ICUSTAY_ID'                    : "float64",
#                                                                                                                    'STARTTIME'                     : "string",
#                                                                                                                    'ENDTIME'                       : "string",
#                                                                                                                    'ITEMID'                        : "int64",
#                                                                                                                    'AMOUNT'                        : "float64",
#                                                                                                                    'AMOUNTUOM'                     : "string",
#                                                                                                                    'RATE'                          : "float64",
#                                                                                                                    'RATEUOM'                       : "string",
#                                                                                                                    'STORETIME'                     : "string",
#                                                                                                                    'CGID'                          : "int64",
#                                                                                                                    'ORDERID'                       : "int64",
#                                                                                                                    'LINKORDERID'                   : "int64",
#                                                                                                                    'ORDERCATEGORYNAME'             : "string",
#                                                                                                                    'SECONDARYORDERCATEGORYNAME'    : "string",
#                                                                                                                    'ORDERCOMPONENTTYPEDESCRIPTION' : "string",
#                                                                                                                    'ORDERCATEGORYDESCRIPTION'      : "string",
#                                                                                                                    'PATIENTWEIGHT'                 : "float64",
#                                                                                                                    'TOTALAMOUNT'                   : "float64",
#                                                                                                                    'TOTALAMOUNTUOM'                : "string",
#                                                                                                                    'ISOPENBAG'                     : "int64",
#                                                                                                                    'CONTINUEINNEXTDEPT'            : "int64",
#                                                                                                                    'CANCELREASON'                  : "int64",
#                                                                                                                    'STATUSDESCRIPTION'             : "string",
#                                                                                                                    'COMMENTS_EDITEDBY'             : "string",
#                                                                                                                    'COMMENTS_CANCELEDBY'           : "string",
#                                                                                                                    'COMMENTS_DATE'                 : "string",
#                                                                                                                    'ORIGINALAMOUNT'                : "float64",
#                                                                                                                    'ORIGINALRATE'                  : "float64"})


# # len(index) = 27854055
# LABEVENTS = pd.read_csv('./mimic-iii-clinical-database-1.4/LABEVENTS.csv.gz', compression='gzip', dtype={'ROW_ID'     : "int64",
#                                                                                                          'SUBJECT_ID' : "int64",
#                                                                                                          'HADM_ID'    : "float64",
#                                                                                                          'ITEMID'     : "int64",
#                                                                                                          'CHARTTIME'  : "string",
#                                                                                                          'VALUE'      : "string",
#                                                                                                          'VALUENUM'   : "float64",
#                                                                                                          'VALUEUOM'   : "string",
#                                                                                                          'FLAG'       : "string"})


# # len(index) = 631726
# MICROBIOLOGYEVENTS = pd.read_csv('./mimic-iii-clinical-database-1.4/MICROBIOLOGYEVENTS.csv.gz', compression='gzip', dtype={'ROW_ID'              : "int64",
#                                                                                                                            'SUBJECT_ID'          : "int64",
#                                                                                                                            'HADM_ID'             : "int64",
#                                                                                                                            'CHARTDATE'           : "string",
#                                                                                                                            'CHARTTIME'           : "string",
#                                                                                                                            'SPEC_ITEMID'         : "float64",
#                                                                                                                            'SPEC_TYPE_DESC'      : "string",
#                                                                                                                            'ORG_ITEMID'          : "float64",
#                                                                                                                            'ORG_NAME'            : "string",
#                                                                                                                            'ISOLATE_NUM'         : "float64",
#                                                                                                                            'AB_ITEMID'           : "float64",
#                                                                                                                            'AB_NAME'             : "string",
#                                                                                                                            'DILUTION_TEXT'       : "string",
#                                                                                                                            'DILUTION_COMPARISON' : "string",
#                                                                                                                            'DILUTION_VALUE'      : "float64",
#                                                                                                                            'INTERPRETATION'      : "string"})


# # len(index) = 2083180
# NOTEEVENTS = pd.read_csv('./mimic-iii-clinical-database-1.4/NOTEEVENTS.csv.gz', compression='gzip', dtype={'ROW_ID'      : "int64",
#                                                                                                            'SUBJECT_ID'  : "int64",
#                                                                                                            'HADM_ID'     : "float64",
#                                                                                                            'CHARTDATE'   : "string",
#                                                                                                            'CHARTTIME'   : "string",
#                                                                                                            'STORETIME'   : "string",
#                                                                                                            'CATEGORY'    : "string",
#                                                                                                            'DESCRIPTION' : "string",
#                                                                                                            'CGID'        : "float64",
#                                                                                                            'ISERROR'     : "float64",
#                                                                                                            'TEXT'        : "string"})


# # len(index) = 4349218
# OUTPUTEVENTS = pd.read_csv('./mimic-iii-clinical-database-1.4/OUTPUTEVENTS.csv.gz', compression='gzip', dtype={'ROW_ID'     : "int64",
#                                                                                                                'SUBJECT_ID' : "int64",
#                                                                                                                'HADM_ID'    : "float64",
#                                                                                                                'ICUSTAY_ID' : "float64",
#                                                                                                                'CHARTTIME'  : "string",
#                                                                                                                'ITEMID'     : "int64",
#                                                                                                                'VALUE'      : "float64",
#                                                                                                                'VALUEUOM'   : "string",
#                                                                                                                'STORETIME'  : "string",
#                                                                                                                'CGID'       : "int64",
#                                                                                                                'STOPPED'    : "float64",
#                                                                                                                'NEWBOTTLE'  : "float64",
#                                                                                                                'ISERROR'    : "float64"})


# # len(index) = 46520
# PATIENTS = pd.read_csv('./mimic-iii-clinical-database-1.4/PATIENTS.csv.gz', compression='gzip', dtype={'ROW_ID'      : "int64",
#                                                                                                        'SUBJECT_ID'  : "int64",
#                                                                                                        'GENDER'      : "string",
#                                                                                                        'DOB'         : "string",
#                                                                                                        'DOD'         : "string",
#                                                                                                        'DOD_HOSP'    : "string",
#                                                                                                        'DOD_SSN'     : "string",
#                                                                                                        'EXPIRE_FLAG' : "int64"})
# print(PATIENTS.head(20))

# # len(index) = 4156450
# PRESCRIPTIONS = pd.read_csv('./mimic-iii-clinical-database-1.4/PRESCRIPTIONS.csv.gz', compression='gzip', type={'ROW_ID'            : "int64",
#                                                                                                                 'SUBJECT_ID'        : "int64",
#                                                                                                                 'HADM_ID'           : "int64",
#                                                                                                                 'ICUSTAY_ID'        : "float64",
#                                                                                                                 'STARTDATE'         : "string",
#                                                                                                                 'ENDDATE'           : "string",
#                                                                                                                 'DRUG_TYPE'         : "string",
#                                                                                                                 'DRUG'              : "string",
#                                                                                                                 'DRUG_NAME_POE'     : "string",
#                                                                                                                 'DRUG_NAME_GENERIC' : "string",
#                                                                                                                 'FORMULARY_DRUG_CD' : "string",
#                                                                                                                 'GSN'               : "string",
#                                                                                                                 'NDC'               : "float64",
#                                                                                                                 'PROD_STRENGTH'     : "string",
#                                                                                                                 'DOSE_VAL_RX'       : "float64",
#                                                                                                                 'DOSE_UNIT_RX'      : "string",
#                                                                                                                 'FORM_VAL_DISP'     : "float64",
#                                                                                                                 'FORM_UNIT_DISP'    : "string",
#                                                                                                                 'ROUTE'             : "string"})


# # len(index) = 258066
# PROCEDUREEVENTS_MV = pd.read_csv('./mimic-iii-clinical-database-1.4/PROCEDUREEVENTS_MV.csv.gz', compression='gzip', dtype={'ROW_ID'                     : "int64",
#                                                                                                                            'SUBJECT_ID'                 : "int64",
#                                                                                                                            'HADM_ID'                    : "int64",
#                                                                                                                            'ICUSTAY_ID'                 : "float64",
#                                                                                                                            'STARTTIME'                  : "string",
#                                                                                                                            'ENDTIME'                    : "string",
#                                                                                                                            'ITEMID'                     : "int64",
#                                                                                                                            'VALUE'                      : "float64",
#                                                                                                                            'VALUEUOM'                   : "string",
#                                                                                                                            'LOCATION'                   : "string",
#                                                                                                                            'LOCATIONCATEGORY'           : "string",
#                                                                                                                            'STORETIME'                  : "string",
#                                                                                                                            'CGID'                       : "int64",
#                                                                                                                            'ORDERID'                    : "int64",
#                                                                                                                            'LINKORDERID'                : "int64",
#                                                                                                                            'ORDERCATEGORYNAME'          : "string",
#                                                                                                                            'SECONDARYORDERCATEGORYNAME' : "string",
#                                                                                                                            'ORDERCATEGORYDESCRIPTION'   : "string",
#                                                                                                                            'ISOPENBAG'                  : "int64",
#                                                                                                                            'CONTINUEINNEXTDEPT'         : "int64",
#                                                                                                                            'CANCELREASON'               : "int64",
#                                                                                                                            'STATUSDESCRIPTION'          : "string",
#                                                                                                                            'COMMENTS_EDITEDBY'          : "string",
#                                                                                                                            'COMMENTS_CANCELEDBY'        : "string",
#                                                                                                                            'COMMENTS_DATE'              : "string"})


# # len(index) = 240095
# PROCEDURES_ICD = pd.read_csv('./mimic-iii-clinical-database-1.4/PROCEDURES_ICD.csv.gz', compression='gzip', dtype={'ROW_ID'     : "int64",
#                                                                                                                    'SUBJECT_ID' : "int64",
#                                                                                                                    'HADM_ID'    : "int64",
#                                                                                                                    'SEQ_NUM'    : "int64",
#                                                                                                                    'ICD9_CODE'  : "int64"})


# # len(index) = 73343
# SERVICES = pd.read_csv('./mimic-iii-clinical-database-1.4/SERVICES.csv.gz', compression='gzip', dtype={'ROW_ID'       : "int64",
#                                                                                                        'SUBJECT_ID'   : "int64",
#                                                                                                        'HADM_ID'      : "int64",
#                                                                                                        'TRANSFERTIME' : "string",
#                                                                                                        'PREV_SERVICE' : "string",
#                                                                                                        'CURR_SERVICE' : "string"})


# # len(index) = 261897
# TRANSFERS = pd.read_csv('./mimic-iii-clinical-database-1.4/TRANSFERS.csv.gz', compression='gzip', dtype={'ROW_ID'       : "int64",
#                                                                                                          'SUBJECT_ID'   : "int64",
#                                                                                                          'HADM_ID'      : "int64",
#                                                                                                          'ICUSTAY_ID'   : "float64",
#                                                                                                          'DBSOURCE'     : "string",
#                                                                                                          'EVENTTYPE'    : "string",
#                                                                                                          'PREV_CAREUNIT': "string",
#                                                                                                          'CURR_CAREUNIT': "string",
#                                                                                                          'PREV_WARDID'  : "float64",
#                                                                                                          'CURR_WARDID'  : "float64",
#                                                                                                          'INTIME'       : "string",
#                                                                                                          'OUTTIME'      : "string",
#                                                                                                          'LOS'          : "float64"})
