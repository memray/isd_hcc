# encoding: utf-8
import pandas as pd
import numpy as np
import math
import os
__author__ = 'Memray'

'''
Initialization part
'''
convert_dict = {}
vert_name = ["HOSPITAL","HOSPITAL","HOSPITAL","HOSPITAL","HOSPITAL","HOSPITAL","HOSPITAL","HOSPITAL","HOSPITAL","HOSPITAL","PROCEDURE_CODE","PROCEDURE_CODE","PROCEDURE_CODE","PROCEDURE_CODE","PROCEDURE_CODE","PROCEDURE_CODE","PROCEDURE_CODE","PROCEDURE_CODE","PROCEDURE_CODE","PROCEDURE_CODE","DIAGNOSIS_CODE","DIAGNOSIS_CODE","DIAGNOSIS_CODE","DIAGNOSIS_CODE","DIAGNOSIS_CODE","DIAGNOSIS_CODE","DIAGNOSIS_CODE","DIAGNOSIS_CODE","DIAGNOSIS_CODE","DIAGNOSIS_CODE","FINANCIAL_CLASS_DESCRIPTION","FINANCIAL_CLASS_DESCRIPTION","FINANCIAL_CLASS_DESCRIPTION","FINANCIAL_CLASS_DESCRIPTION","FINANCIAL_CLASS_DESCRIPTION","FINANCIAL_CLASS_DESCRIPTION","FINANCIAL_CLASS_DESCRIPTION","FINANCIAL_CLASS_DESCRIPTION","FINANCIAL_CLASS_DESCRIPTION","FINANCIAL_CLASS_DESCRIPTION","DRG_CODE","DRG_CODE","DRG_CODE","DRG_CODE","DRG_CODE","DRG_CODE","DRG_CODE","DRG_CODE","DRG_CODE","DRG_CODE","SEVERITY_OF_ILLNESS","SEVERITY_OF_ILLNESS","SEVERITY_OF_ILLNESS","SEVERITY_OF_ILLNESS","SEVERITY_OF_ILLNESS","SEVERITY_OF_ILLNESS","SEVERITY_OF_ILLNESS","SEVERITY_OF_ILLNESS","SEVERITY_OF_ILLNESS","SEVERITY_OF_ILLNESS","SMOKING","SMOKING","SMOKING","SMOKING","SMOKING","SMOKING","SMOKING","SMOKING","SMOKING","SMOKING","AGE_ON_CONTACT_DATE","AGE_ON_CONTACT_DATE","AGE_ON_CONTACT_DATE","AGE_ON_CONTACT_DATE","AGE_ON_CONTACT_DATE","AGE_ON_CONTACT_DATE","AGE_ON_CONTACT_DATE","AGE_ON_CONTACT_DATE","AGE_ON_CONTACT_DATE","AGE_ON_CONTACT_DATE","FEM","FEM","FEM","FEM","FEM","FEM","FEM","FEM","FEM","FEM","BMI","BMI","BMI","BMI","BMI","BMI","BMI","BMI","BMI","BMI","BP_SYSTOLIC","BP_SYSTOLIC","BP_SYSTOLIC","BP_SYSTOLIC","BP_SYSTOLIC","BP_SYSTOLIC","BP_SYSTOLIC","BP_SYSTOLIC","BP_SYSTOLIC","BP_SYSTOLIC","DIAB","DIAB","DIAB","DIAB","DIAB","DIAB","DIAB","DIAB","DIAB","DIAB","COPD_DX","COPD_DX","COPD_DX","COPD_DX","COPD_DX","COPD_DX","COPD_DX","COPD_DX","COPD_DX","COPD_DX","GLUCOSE","GLUCOSE","GLUCOSE","GLUCOSE","GLUCOSE","GLUCOSE","GLUCOSE","GLUCOSE","GLUCOSE","GLUCOSE","POTASSIUM(K)","POTASSIUM(K)","POTASSIUM(K)","POTASSIUM(K)","POTASSIUM(K)","POTASSIUM(K)","POTASSIUM(K)","POTASSIUM(K)","POTASSIUM(K)","POTASSIUM(K)","SODIUM(NA)","SODIUM(NA)","SODIUM(NA)","SODIUM(NA)","SODIUM(NA)","SODIUM(NA)","SODIUM(NA)","SODIUM(NA)","SODIUM(NA)","SODIUM(NA)","TOTAL_PROTEIN","TOTAL_PROTEIN","TOTAL_PROTEIN","TOTAL_PROTEIN","TOTAL_PROTEIN","TOTAL_PROTEIN","TOTAL_PROTEIN","TOTAL_PROTEIN","TOTAL_PROTEIN","TOTAL_PROTEIN","PROTHROMBIN_TIME","PROTHROMBIN_TIME","PROTHROMBIN_TIME","PROTHROMBIN_TIME","PROTHROMBIN_TIME","PROTHROMBIN_TIME","PROTHROMBIN_TIME","PROTHROMBIN_TIME","PROTHROMBIN_TIME","PROTHROMBIN_TIME","ACTIVATED_PTT","ACTIVATED_PTT","ACTIVATED_PTT","ACTIVATED_PTT","ACTIVATED_PTT","ACTIVATED_PTT","ACTIVATED_PTT","ACTIVATED_PTT","ACTIVATED_PTT","ACTIVATED_PTT","ASPARTATE_AMINOT.(AST)","ASPARTATE_AMINOT.(AST)","ASPARTATE_AMINOT.(AST)","ASPARTATE_AMINOT.(AST)","ASPARTATE_AMINOT.(AST)","ASPARTATE_AMINOT.(AST)","ASPARTATE_AMINOT.(AST)","ASPARTATE_AMINOT.(AST)","ASPARTATE_AMINOT.(AST)","ASPARTATE_AMINOT.(AST)","TOTAL_BILIRUBIN","TOTAL_BILIRUBIN","TOTAL_BILIRUBIN","TOTAL_BILIRUBIN","TOTAL_BILIRUBIN","TOTAL_BILIRUBIN","TOTAL_BILIRUBIN","TOTAL_BILIRUBIN","TOTAL_BILIRUBIN","TOTAL_BILIRUBIN","ALBUMIN","ALBUMIN","ALBUMIN","ALBUMIN","ALBUMIN","ALBUMIN","ALBUMIN","ALBUMIN","ALBUMIN","ALBUMIN","ALKALINE_PHOSPHATASE","ALKALINE_PHOSPHATASE","ALKALINE_PHOSPHATASE","ALKALINE_PHOSPHATASE","ALKALINE_PHOSPHATASE","ALKALINE_PHOSPHATASE","ALKALINE_PHOSPHATASE","ALKALINE_PHOSPHATASE","ALKALINE_PHOSPHATASE","ALKALINE_PHOSPHATASE","UREA_NITROGEN","UREA_NITROGEN","UREA_NITROGEN","UREA_NITROGEN","UREA_NITROGEN","UREA_NITROGEN","UREA_NITROGEN","UREA_NITROGEN","UREA_NITROGEN","UREA_NITROGEN","CALCIUM(CA)","CALCIUM(CA)","CALCIUM(CA)","CALCIUM(CA)","CALCIUM(CA)","CALCIUM(CA)","CALCIUM(CA)","CALCIUM(CA)","CALCIUM(CA)","CALCIUM(CA)","HGB","HGB","HGB","HGB","HGB","HGB","HGB","HGB","HGB","HGB","HEMATOCRIT(HCT)","HEMATOCRIT(HCT)","HEMATOCRIT(HCT)","HEMATOCRIT(HCT)","HEMATOCRIT(HCT)","HEMATOCRIT(HCT)","HEMATOCRIT(HCT)","HEMATOCRIT(HCT)","HEMATOCRIT(HCT)","HEMATOCRIT(HCT)","RBC","RBC","RBC","RBC","RBC","RBC","RBC","RBC","RBC","RBC","MCH","MCH","MCH","MCH","MCH","MCH","MCH","MCH","MCH","MCH","MCV","MCV","MCV","MCV","MCV","MCV","MCV","MCV","MCV","MCV","MCHC","MCHC","MCHC","MCHC","MCHC","MCHC","MCHC","MCHC","MCHC","MCHC","RDW","RDW","RDW","RDW","RDW","RDW","RDW","RDW","RDW","RDW","CREATININE","CREATININE","CREATININE","CREATININE","CREATININE","CREATININE","CREATININE","CREATININE","CREATININE","CREATININE","PLATELETS","PLATELETS","PLATELETS","PLATELETS","PLATELETS","PLATELETS","PLATELETS","PLATELETS","PLATELETS","PLATELETS","WBC","WBC","WBC","WBC","WBC","WBC","WBC","WBC","WBC","WBC","ABS_NEUTROPHILS","ABS_NEUTROPHILS","ABS_NEUTROPHILS","ABS_NEUTROPHILS","ABS_NEUTROPHILS","ABS_NEUTROPHILS","ABS_NEUTROPHILS","ABS_NEUTROPHILS","ABS_NEUTROPHILS","ABS_NEUTROPHILS","ABS_LYMPHOCYTES","ABS_LYMPHOCYTES","ABS_LYMPHOCYTES","ABS_LYMPHOCYTES","ABS_LYMPHOCYTES","ABS_LYMPHOCYTES","ABS_LYMPHOCYTES","ABS_LYMPHOCYTES","ABS_LYMPHOCYTES","ABS_LYMPHOCYTES","ABS_MONOCYTES","ABS_MONOCYTES","ABS_MONOCYTES","ABS_MONOCYTES","ABS_MONOCYTES","ABS_MONOCYTES","ABS_MONOCYTES","ABS_MONOCYTES","ABS_MONOCYTES","ABS_MONOCYTES","CARBON_DIOXIDE(CO2)","CARBON_DIOXIDE(CO2)","CARBON_DIOXIDE(CO2)","CARBON_DIOXIDE(CO2)","CARBON_DIOXIDE(CO2)","CARBON_DIOXIDE(CO2)","CARBON_DIOXIDE(CO2)","CARBON_DIOXIDE(CO2)","CARBON_DIOXIDE(CO2)","CARBON_DIOXIDE(CO2)"]
vert_vals = ["PAS","SHY","PUH","SMH","MER","MCK","NWH","HRY","HAM","N/A","3241","3249","3220","3230","3224","3229","3259","3239","3452","N/A","1623","1625","1629","1624","1628","1622","-","-","-","N/A","MEDICARE_PART_A","SECURITY_BLUE_HMO","UPMC_HP_MEDICARE_HMO","B/C_KEYSTONE","UPMC_HEALTH_NETWORK","ADVANTRA_MC_HMO","OTHER_MC_HMO","BEST_HEALTH_CARE","HLTH_AMER_COMM_MN_CR","N/A","164","163","3","165","167","168","166","75","-","N/A","2","3","4","1","-","-","-","-","-","N/A","Quit","Yes","Never","Not_Asked","Passive","-","-","-","-","N/A","<48","48-59","59-69","69-80",">80","-","-","-","-","N/A","Male","Female","-","-","-","-","-","-","-","N/A","<18","18-25","25-31","31-38",">38","-","-","-","-","N/A","<102","102-114","114-127","127-137","137-148","148-160",">160","-","-","N/A","No","Yes","-","-","-","-","-","-","-","N/A","No","Yes","-","-","-","-","-","-","-","N/A","<70","70-88","88-107","107-124","124-144",">144","-","-","-","N/A","<3.6","3.6-4.6","4.6-5.1",">5.1","-","-","-","-","-","N/A","<130","130-133","133-136","-136-140",">140","-","-","-","-","N/A","<6","6-7","7-7.8","7.8-8.2",">8.2","-","-","-","-","N/A","<10","10-16",">16","-","-","-","-","-","-","N/A","<34","34-42",">42","-","-","-","-","-","-","N/A","<14","14-21","21-28","28-36",">36","-","-","-","-","N/A","<0.25","0.25-0.45","0.45-0.75",">0.75","-","-","-","-","-","N/A","<2.8","2.8-3.5",">3.5","-","-","-","-","-","-","N/A","<65","65-110","110-175",">175","-","-","-","-","-","N/A","<10","10-15.5","15.5-22.5","22.5-33",">33","-","-","-","-","N/A","<8.5","8.5-10",">10","-","-","-","-","-","-","N/A","<9","9-11","11-13.5","13.5-15",">15","","-","-","-","N/A","<28","28-34","34-37","37-40","40-45",">45","-","-","-","N/A","<2.9","2.9-3.5","3.5-4","4-4.9",">4.9","-","-","-","-","N/A","<28","28-34",">34","-","-","-","-","-","-","N/A","<81","81-88","88-93","93-100",">100","-","-","-","-","N/A","<32","32-33","33-34.2","34.2-35",">35","-","-","-","-","N/A","<13","13-15","15-17",">17","-","-","-","-","-","N/A","<1.3",">1.3","-","-","-","-","-","-","-","N/A","<140","140-275","275-320","320-485",">485","-","-","-","-","N/A","<5.2","5.2-7","7-11","11-14",">14","-","-","-","-","N/A","<3","3-4.5","4.5-6.5","6.5-10",">10","-","-","-","-","N/A","<0.95","0.95-2","2-3",">3","-","-","-","-","-","N/A","<0.3","0.3-10",">10","-","-","-","-","-","-","N/A","<24","24-27","27-32",">32","-","-","-","-","-","N/A"]

def isfloat(value):
    try:
        float(value)
        return True
    except:
        return False

for i in range(len(vert_name)):
    key = vert_name[i]
    value = vert_vals[i]
    if not key in convert_dict:
        convert_dict[key] = []
    convert_dict[key].append(value)

def convert_into_PartiteGraph(raw_data):
    '''
    Our array starts from 0, but the first value is meaningless, so basically useful part is [1: 391] (the last one doesn't count).
    '''
    partite_coordinate = np.zeros(400)

    # print(raw_data)
    index_base = 0
    ########## INDEX=1 HOSPITAL >>>  ############### 1-10 'HOSPITAL'
    # index_base += 10
    key = vert_name[index_base]
    val = raw_data[key]
    for i in range(10):
        if str(val) == convert_dict[key][i]:
            partite_coordinate[index_base+i+1] = 1
    if not str(val) in convert_dict[key]:
        partite_coordinate[index_base + 10] = 1

    ########## INDEX=2 PROCEDURE CODE >>>  ############### 11-20 'PROCEDURE_CODE'
    index_base += 10
    key = vert_name[index_base]
    val = raw_data[key]
    for i in range(10):
        if str(val) == convert_dict[key][i]:
            partite_coordinate[index_base+i+1] = 1
    if not str(val) in convert_dict[key]:
        partite_coordinate[index_base + 10] = 1

    ########## INDEX=3 diagnosis code >>>  ############### 21-30 'DIAGNOSIS_CODE'
    index_base += 10
    key = vert_name[index_base]
    val = raw_data[key]
    for i in range(10):
        if str(val) == convert_dict[key][i]:
            partite_coordinate[index_base+i+1] = 1
    if not str(val) in convert_dict[key]:
        partite_coordinate[index_base + 10] = 1

    ########## INDEX=4 insurance >>>  ############### 31-40 'FINANCIAL_CLASS_DESCRIPTION'
    index_base += 10
    key = vert_name[index_base]
    val = raw_data[key]
    for i in range(10):
        if str(val) == convert_dict[key][i]:
            partite_coordinate[index_base+i+1] = 1
    if not str(val) in convert_dict[key]:
        partite_coordinate[index_base + 10] = 1

    # ########## INDEX=5 DRG >>>  ############### 41-50 'DRG_CODE'
    index_base += 10
    key = vert_name[index_base]
    val = raw_data[key]
    for i in range(10):
        if str(val) == convert_dict[key][i]:
            partite_coordinate[index_base+i+1] = 1
    if not str(val) in convert_dict[key]:
        partite_coordinate[index_base + 10] = 1

    # ########## INDEX=6 severity >>>  ############### 51-60     'SEVERITY_OF_ILLNESS'
    index_base += 10
    key = vert_name[index_base]
    val = raw_data[key]
    for i in range(10):
        if str(val) == convert_dict[key][i]:
            partite_coordinate[index_base+i+1] = 1
    if not str(val) in convert_dict[key]:
        partite_coordinate[index_base + 10] = 1

# ########## INDEX=7 smoking >>>  ############### 61-70 'SMOKING'
    index_base += 10
    key = vert_name[index_base]
    val = raw_data[key]
    for i in range(10):
        if str(val) == convert_dict[key][i]:
            partite_coordinate[index_base+i+1] = 1
    if not str(val) in convert_dict[key]:
        partite_coordinate[index_base + 10] = 1

# ########## INDEX=8 age >>>  ############### 71-80 'AGE_ON_CONTACT_DATE'
    index_base += 10
    key = vert_name[index_base]
    val = raw_data[key]
    if isfloat(val):
        val = float(val)
        if (val > 0) and (val < 48):
            partite_coordinate[index_base + 1] = 1
        elif (val >= 48) and (val < 59):
            partite_coordinate[index_base + 2] = 1
        elif (val >= 59) and (val < 69):
            partite_coordinate[index_base + 3] = 1
        elif (val >= 69) and (val < 80):
            partite_coordinate[index_base + 4] = 1
        elif (val > 80):
            partite_coordinate[index_base + 5] = 1
        elif (val <= 0):
            partite_coordinate[index_base + 10] = 1
    else:
        partite_coordinate[index_base + 10] = 1

# ########## INDEX=9 sex >>>  ############### 81-90 'FEM'
    index_base += 10
    key = vert_name[index_base]
    val = raw_data[key]
    if val=='0':
        partite_coordinate[index_base + 1] = 1
    elif val=='1':
        partite_coordinate[index_base + 2] = 1
    else:
        partite_coordinate[index_base + 10] = 1
# ########## INDEX=10 BMI >>>  ############### 91-100
    index_base += 10
    key = vert_name[index_base]
    val = raw_data[key]
    if isfloat(val):
        val = float(val)
        if (val > 0) and (val < 18):
            partite_coordinate[index_base + 1] = 1
        elif (val >= 18) and (val < 25):
            partite_coordinate[index_base + 2] = 1
        elif (val >= 25) and (val < 31):
            partite_coordinate[index_base + 3] = 1
        elif (val >= 31) and (val < 38):
            partite_coordinate[index_base + 4] = 1
        elif (val >= 38):
            partite_coordinate[index_base + 5] = 1
        elif (val <= 0):
            partite_coordinate[index_base + 10] = 1
    else:
        partite_coordinate[index_base + 10] = 1
# ########## INDEX=11 Tri years >>>  ############### 101-110 'BP_SYSTOLIC'
    index_base = 100
    key = vert_name[index_base]
    val = raw_data[key]
    if isfloat(val):
        val = float(val)
        if (val > 0) and (val <= 102):
            partite_coordinate[index_base + 1] = 1
        elif (val > 102) and (val <= 114):
            partite_coordinate[index_base + 2] = 1
        elif (val > 114) and (val <= 127):
            partite_coordinate[index_base + 3] = 1
        elif (val > 127) and (val <= 137):
            partite_coordinate[index_base + 4] = 1
        elif (val > 137) and (val <= 148):
            partite_coordinate[index_base + 5] = 1
        elif (val > 148) and (val <= 160):
            partite_coordinate[index_base + 6] = 1
        elif (val > 160):
            partite_coordinate[index_base + 7] = 1
        elif (val <= 0):
            partite_coordinate[index_base + 10] = 1
    else:
        partite_coordinate[index_base + 10] = 1
# ########## INDEX=12 diabetes >>>  ############### 111-120 'DIAB'
    index_base += 10
    key = vert_name[index_base]
    val = raw_data[key]
    if val == '0':
        partite_coordinate[index_base + 1] = 1
    elif val == '1':
        partite_coordinate[index_base + 2] = 1
    else:
        partite_coordinate[index_base + 10] = 1

# ########## INDEX=13 COPD >>>  ############### 121-130 'COPD_DX'
    index_base += 10
    key = vert_name[index_base]
    val = raw_data[key]
    if val == '0':
        partite_coordinate[index_base + 1] = 1
    elif val == '1':
        partite_coordinate[index_base + 2] = 1
    else:
        partite_coordinate[index_base + 10] = 1

# ########## INDEX=14 glucose >>>  ############### 131-140 'GLUCOSE'
    index_base += 10
    key = vert_name[index_base]
    val = raw_data[key]
    if isfloat(val):
        val = float(val)
        if (val > 0) and (val <= 70):
            partite_coordinate[index_base + 1] = 1
        elif (val > 70) and (val <= 88):
            partite_coordinate[index_base + 2] = 1
        elif (val > 88) and (val <= 107):
            partite_coordinate[index_base + 3] = 1
        elif (val > 107) and (val <= 124):
            partite_coordinate[index_base + 4] = 1
        elif (val > 124) and (val <= 144):
            partite_coordinate[index_base + 5] = 1
        elif (val > 144):
            partite_coordinate[index_base + 6] = 1
        elif (val <= 0):
            partite_coordinate[index_base + 10] = 1
    else:
        partite_coordinate[index_base + 10] = 1

# ########## INDEX=15 POtassium >>>  ############### 141-150 'POTASSIUM(K)' float
    index_base += 10
    key = vert_name[index_base]
    val = raw_data[key]
    if isfloat(val):
        val = float(val)
        if (val > 0) and (val <= 3.6):
            partite_coordinate[index_base + 1] = 1
        elif (val > 3.6) and (val <= 4.6):
            partite_coordinate[index_base + 2] = 1
        elif (val > 4.6) and (val <= 5.1):
            partite_coordinate[index_base + 3] = 1
        elif (val > 5.1):
            partite_coordinate[index_base + 4] = 1
        elif (val <= 0):
            partite_coordinate[index_base + 10] = 1
    else:
        partite_coordinate[index_base + 10] = 1

#  ########## INDEX=16 Sodium >>>  ############### 151-160 'SODIUM(NA)' float
    index_base += 10
    key = vert_name[index_base]
    val = raw_data[key]
    if isfloat(val):
        val = float(val)
        if (val > 0) and (val <= 130):
            partite_coordinate[index_base + 1] = 1
        elif (val > 130) and (val <= 133):
            partite_coordinate[index_base + 2] = 1
        elif (val > 133) and (val <= 136):
            partite_coordinate[index_base + 3] = 1
        elif (val > 136) and (val <= 140):
            partite_coordinate[index_base + 4] = 1
        elif (val > 140):
            partite_coordinate[index_base + 5] = 1
        elif (val <= 0):
            partite_coordinate[index_base + 10] = 1
    else:
        partite_coordinate[index_base + 10] = 1

# ########## INDEX=17 total protein >>>  ############### 161-170 'TOTAL_PROTEIN' float
    index_base += 10
    key = vert_name[index_base]
    val = raw_data[key]
    if isfloat(val):
        val = float(val)
        if (val > 0) and (val <= 6):
            partite_coordinate[index_base + 1] = 1
        elif (val > 6) and (val <= 7):
            partite_coordinate[index_base + 2] = 1
        elif (val > 7) and (val <= 7.8):
            partite_coordinate[index_base + 3] = 1
        elif (val > 7.8) and (val <= 8.2):
            partite_coordinate[index_base + 4] = 1
        elif (val > 8.2):
            partite_coordinate[index_base + 5] = 1
        elif (val <= 0):
            partite_coordinate[index_base + 10] = 1
    else:
        partite_coordinate[index_base + 10] = 1

# ########## INDEX=18 protothrombin >>>  ############### 171-180 PROTHROMBIN_TIME, scale in (0,10],(10,16],(16,) float
    index_base += 10
    key = vert_name[index_base]
    val = raw_data[key]
    if isfloat(val):
        val = float(val)
        if (val > 0) and (val <= 10):
            partite_coordinate[index_base + 1] = 1
        elif (val > 10) and (val <= 16):
            partite_coordinate[index_base + 2] = 1
        elif (val > 16):
            partite_coordinate[index_base + 3] = 1
        elif (val <= 0):
            partite_coordinate[index_base + 10] = 1
    else:
        partite_coordinate[index_base + 10] = 1

# ########## INDEX=19 activated PTT >>>  ############### 181-190 'ACTIVATED_PTT' float
    index_base += 10
    key = vert_name[index_base]
    val = raw_data[key]
    if isfloat(val):
        val = float(val)
        if (val > 0) and (val <= 34):
            partite_coordinate[index_base + 1] = 1
        elif (val > 34) and (val <= 42):
            partite_coordinate[index_base + 2] = 1
        elif (val > 42):
            partite_coordinate[index_base + 3] = 1
        elif (val <= 0):
            partite_coordinate[index_base + 10] = 1
    else:
        partite_coordinate[index_base + 10] = 1
# ########## INDEX=20 AST >>>  ############### 191-200 'ASPARTATE_AMINOT.(AST)'
    index_base += 10
    key = vert_name[index_base]
    val = raw_data[key]
    if isfloat(val):
        val = float(val)
        if (val > 0) and (val <= 14):
            partite_coordinate[index_base + 1] = 1
        elif (val > 14) and (val <= 21):
            partite_coordinate[index_base + 2] = 1
        elif (val > 21) and (val <= 28):
            partite_coordinate[index_base + 3] = 1
        elif (val > 28) and (val <= 36):
            partite_coordinate[index_base + 4] = 1
        elif (val > 36):
            partite_coordinate[index_base + 5] = 1
        elif (val <= 0):
            partite_coordinate[index_base + 10] = 1
    else:
        partite_coordinate[index_base + 10] = 1
# ########## INDEX=21 BILI >>>  ############### 201-210 'TOTAL_BILIRUBIN' float
    index_base = 200
    key = vert_name[index_base]
    val = raw_data[key]
    if isfloat(val):
        val = float(val)
        if val > 0:
            val = math.log10(float(val))
            if (val <= -0.603):
                partite_coordinate[index_base + 1] = 1
            elif (val > -0.603) and (val <= -0.356):
                partite_coordinate[index_base + 2] = 1
            elif (val > -0.356) and (val <= -0.1174):
                partite_coordinate[index_base + 3] = 1
            elif (val > -0.1174):
                partite_coordinate[index_base + 4] = 1
        else:
            partite_coordinate[index_base + 10] = 1
    else:
        partite_coordinate[index_base + 10] = 1
# ########## INDEX=22 ALB >>>  ############### 211-220 'ALBUMIN' float
    index_base += 10
    key = vert_name[index_base]
    val = raw_data[key]
    if isfloat(val):
        val = float(val)
        if val > 0:
            val = math.log10(float(val))
            if (val <= 0.442):
                partite_coordinate[index_base + 1] = 1
            elif (val > 0.442) and (val <= 0.5344):
                partite_coordinate[index_base + 2] = 1
            elif (val > 0.5344):
                partite_coordinate[index_base + 3] = 1
        else:
            partite_coordinate[index_base + 10] = 1
    else:
        partite_coordinate[index_base + 10] = 1
# ########## INDEX=23 ALKP >>>  ############### 221-230 'ALKALINE_PHOSPHATASE'
    index_base += 10
    key = vert_name[index_base]
    val = raw_data[key]
    if isfloat(val):
        val = float(val)
        if val > 0:
            val = math.log10(float(val))
            if (val <= 1.8):
                partite_coordinate[index_base + 1] = 1
            elif (val > 1.8) and (val <= 2.03):
                partite_coordinate[index_base + 2] = 1
            elif (val > 2.03) and (val <= 2.238):
                partite_coordinate[index_base + 3] = 1
            elif (val > 2.238):
                partite_coordinate[index_base + 4] = 1
        else:
            partite_coordinate[index_base + 10] = 1
    else:
        partite_coordinate[index_base + 10] = 1
# ########## INDEX=24 Urea N >>>  ############### 231-240 'UREA_NITROGEN'
    index_base += 10
    key = vert_name[index_base]
    val = raw_data[key]
    if isfloat(val):
        val = float(val)
        if (val > 0) and (val <= 10):
            partite_coordinate[index_base + 1] = 1
        elif (val > 10) and (val <= 15.6):
            partite_coordinate[index_base + 2] = 1
        elif (val > 15.6) and (val <= 22.3):
            partite_coordinate[index_base + 3] = 1
        elif (val > 22.3) and (val <= 33):
            partite_coordinate[index_base + 4] = 1
        elif (val > 33):
            partite_coordinate[index_base + 5] = 1
        elif (val <= 0):
            partite_coordinate[index_base + 10] = 1
    else:
        partite_coordinate[index_base + 10] = 1

# ########## INDEX=25 Calcium >>>  ############### 241-250 'CALCIUM(CA)' float
    index_base += 10
    key = vert_name[index_base]
    val = raw_data[key]
    if isfloat(val):
        val = float(val)
        if (val > 0) and (val <= 8.5):
            partite_coordinate[index_base + 1] = 1
        elif (val > 8.5) and (val <= 10):
            partite_coordinate[index_base + 2] = 1
        elif (val > 10):
            partite_coordinate[index_base + 3] = 1
        elif (val <= 0):
            partite_coordinate[index_base + 10] = 1
    else:
        partite_coordinate[index_base + 10] = 1
# ########## INDEX=26 HGB >>>  ############### 251-260 'HGB' float
    index_base += 10
    key = vert_name[index_base]
    val = raw_data[key]
    if isfloat(val):
        val = float(val)
        if (val > 0) and (val <= 9):
            partite_coordinate[index_base + 1] = 1
        elif (val > 9) and (val <= 11):
            partite_coordinate[index_base + 2] = 1
        elif (val > 11) and (val <= 13.5):
            partite_coordinate[index_base + 3] = 1
        elif (val > 13.5) and (val <= 15):
            partite_coordinate[index_base + 4] = 1
        elif (val > 15):
            partite_coordinate[index_base + 5] = 1
        elif (val <= 0):
            partite_coordinate[index_base + 10] = 1
    else:
        partite_coordinate[index_base + 10] = 1
# ########## INDEX=27 HECT >>>  ############### 261-270 'HEMATOCRIT(HCT)' float
    index_base += 10
    key = vert_name[index_base]
    val = raw_data[key]
    if isfloat(val):
        val = float(val)
        if (val > 0) and (val <= 28):
            partite_coordinate[index_base + 1] = 1
        elif (val > 28) and (val <= 34):
            partite_coordinate[index_base + 2] = 1
        elif (val > 34) and (val <= 37):
            partite_coordinate[index_base + 3] = 1
        elif (val > 37) and (val <= 40):
            partite_coordinate[index_base + 4] = 1
        elif (val > 40) and (val <= 45):
            partite_coordinate[index_base + 5] = 1
        elif (val > 45):
            partite_coordinate[index_base + 6] = 1
        elif (val <= 0):
            partite_coordinate[index_base + 10] = 1
    else:
        partite_coordinate[index_base + 10] = 1
# ########## INDEX=28 RBC >>>  ############### 271-280 'RBC' float
    index_base += 10
    key = vert_name[index_base]
    val = raw_data[key]
    if isfloat(val):
        val = float(val)
        if (val > 0) and (val <= 2.9):
            partite_coordinate[index_base + 1] = 1
        elif (val > 2.9) and (val <= 3.5):
            partite_coordinate[index_base + 2] = 1
        elif (val > 3.5) and (val <= 4):
            partite_coordinate[index_base + 3] = 1
        elif (val > 4) and (val <= 4.9):
            partite_coordinate[index_base + 4] = 1
        elif (val > 4.9):
            partite_coordinate[index_base + 5] = 1
        elif (val <= 0):
            partite_coordinate[index_base + 10] = 1
    else:
        partite_coordinate[index_base + 10] = 1
# ########## INDEX=29 MCH >>>  ############### 281-290 'MCH' float
    index_base += 10
    key = vert_name[index_base]
    val = raw_data[key]
    if isfloat(val):
        val = float(val)
        if (val > 0) and (val <= 28):
            partite_coordinate[index_base + 1] = 1
        elif (val > 28) and (val <= 34):
            partite_coordinate[index_base + 2] = 1
        elif (val > 34):
            partite_coordinate[index_base + 3] = 1
        elif (val <= 0):
            partite_coordinate[index_base + 10] = 1
    else:
        partite_coordinate[index_base + 10] = 1
# ########## INDEX=30 MCV >>>  ############### 291-300 'MCV' float
    index_base += 10
    key = vert_name[index_base]
    val = raw_data[key]
    if isfloat(val):
        val = float(val)
        if (val > 0) and (val <= 81):
            partite_coordinate[index_base + 1] = 1
        elif (val > 81) and (val <= 88):
            partite_coordinate[index_base + 2] = 1
        elif (val > 88) and (val <= 93):
            partite_coordinate[index_base + 3] = 1
        elif (val > 93) and (val <= 100):
            partite_coordinate[index_base + 4] = 1
        elif (val > 100):
            partite_coordinate[index_base + 5] = 1
        elif (val <= 0):
            partite_coordinate[index_base + 10] = 1
    else:
        partite_coordinate[index_base + 10] = 1
# ########## INDEX=31 MCHC >>>  ############### 301-310 'MCHC' float
    index_base = 300
    key = vert_name[index_base]
    val = raw_data[key]
    if isfloat(val):
        val = float(val)
        if (val > 0) and (val <= 32):
            partite_coordinate[index_base + 1] = 1
        elif (val > 32) and (val <= 33):
            partite_coordinate[index_base + 2] = 1
        elif (val > 33) and (val <= 34.2):
            partite_coordinate[index_base + 3] = 1
        elif (val > 34.2) and (val <= 35):
            partite_coordinate[index_base + 4] = 1
        elif (val > 35):
            partite_coordinate[index_base + 5] = 1
        elif (val <= 0):
            partite_coordinate[index_base + 10] = 1
    else:
        partite_coordinate[index_base + 10] = 1
# ########## INDEX=32 RDW >>>  ############### 311-320 'RDW' float
    index_base += 10
    key = vert_name[index_base]
    val = raw_data[key]
    if isfloat(val):
        val = float(val)
        if (val > 0) and (val <= 13):
            partite_coordinate[index_base + 1] = 1
        elif (val > 13) and (val <= 15):
            partite_coordinate[index_base + 2] = 1
        elif (val > 15) and (val <= 17):
            partite_coordinate[index_base + 3] = 1
        elif (val > 17):
            partite_coordinate[index_base + 4] = 1
        elif (val <= 0):
            partite_coordinate[index_base + 10] = 1
    else:
        partite_coordinate[index_base + 10] = 1

# ########## INDEX=33 creatinine >>>  ############### 321-330 'CREATININE' float
    index_base += 10
    key = vert_name[index_base]
    val = raw_data[key]
    if isfloat(val):
        val = float(val)
        if (val > 0) and (val <= 1.3):
            partite_coordinate[index_base + 1] = 1
        elif (val > 1.3):
            partite_coordinate[index_base + 2] = 1
        elif (val <= 0):
            partite_coordinate[index_base + 10] = 1
    else:
        partite_coordinate[index_base + 10] = 1
# ########## INDEX=34 platelets >>>  ############### 331-340 'PLATELETS'
    index_base += 10
    key = vert_name[index_base]
    val = raw_data[key]
    if isfloat(val):
        val = float(val)
        if (val > 0) and (val <= 2.15):
            partite_coordinate[index_base + 1] = 1
        elif (val > 2.15) and (val <= 2.44):
            partite_coordinate[index_base + 2] = 1
        elif (val > 2.44) and (val <= 2.5):
            partite_coordinate[index_base + 3] = 1
        elif (val > 2.5) and (val <= 2.685):
            partite_coordinate[index_base + 4] = 1
        elif (val > 2.685):
            partite_coordinate[index_base + 5] = 1
        elif (val <= 0):
            partite_coordinate[index_base + 10] = 1
    else:
        partite_coordinate[index_base + 10] = 1

# ########## INDEX=35 WBC >>>  ############### 341-350 'WBC' float
    index_base += 10
    key = vert_name[index_base]
    val = raw_data[key]
    if isfloat(val):
        val = float(val)
        if (val > 0):
            val = math.log10(val)
            if val<=0.7193:
                partite_coordinate[index_base + 1] = 1
            elif (val > 0.7193) and (val <= 0.843):
                partite_coordinate[index_base + 2] = 1
            elif (val > 0.843) and (val <= 1.0276):
                partite_coordinate[index_base + 3] = 1
            elif (val > 1.0276) and (val <= 1.158):
                partite_coordinate[index_base + 4] = 1
            elif (val > 1.158):
                partite_coordinate[index_base + 5] = 1
        elif (val <= 0):
            partite_coordinate[index_base + 10] = 1
    else:
        partite_coordinate[index_base + 10] = 1

# ########## INDEX=36 abs neutrophiles >>>  ############### 351-360 'ABS_NEUTROPHILS' float
    index_base += 10
    key = vert_name[index_base]
    val = raw_data[key]
    if isfloat(val):
        val = float(val)
        if (val > 0):
            val = math.log10(val)
            if val <= 0.465:
                partite_coordinate[index_base + 1] = 1
            elif (val > 0.465) and (val <= 0.6358):
                partite_coordinate[index_base + 2] = 1
            elif (val > 0.6358) and (val <= 0.8):
                partite_coordinate[index_base + 3] = 1
            elif (val > 0.8) and (val <= 0.9858):
                partite_coordinate[index_base + 4] = 1
            elif (val > 0.9858):
                partite_coordinate[index_base + 5] = 1
        elif (val <= 0):
            partite_coordinate[index_base + 10] = 1
    else:
        partite_coordinate[index_base + 10] = 1

# ########## INDEX=37 lymphocytes >>>  ############### 361-370 'ABS_LYMPHOCYTES' float
    index_base += 10
    key = vert_name[index_base]
    val = raw_data[key]
    if isfloat(val):
        val = float(val)
        if (val > 0):
            val = math.log10(val)
            if val <= -0.0306:
                partite_coordinate[index_base + 1] = 1
            elif (val > -0.0306 ) and (val <= 0.2947):
                partite_coordinate[index_base + 2] = 1
            elif (val > 0.2947) and (val <= 0.48):
                partite_coordinate[index_base + 3] = 1
            elif (val > 0.48):
                partite_coordinate[index_base + 4] = 1
        elif (val <= 0):
            partite_coordinate[index_base + 10] = 1
    else:
        partite_coordinate[index_base + 10] = 1
# ########## INDEX=38 monocytes >>>  ############### 371-380 'ABS_MONOCYTES' float
    index_base += 10
    key = vert_name[index_base]
    val = raw_data[key]
    if isfloat(val):
        val = float(val)
        if (val > 0):
            val = math.log10(val)
            if val <= -0.5764:
                partite_coordinate[index_base + 1] = 1
            elif (val > -0.5764) and (val <= 1):
                partite_coordinate[index_base + 2] = 1
            elif (val > 1):
                partite_coordinate[index_base + 3] = 1
        elif (val <= 0):
            partite_coordinate[index_base + 10] = 1
    else:
        partite_coordinate[index_base + 10] = 1
# ########## INDEX=39 CO2 >>>  ############### 381-390 'CARBON_DIOXIDE(CO2)' float
    index_base += 10
    key = vert_name[index_base]
    val = raw_data[key]
    if isfloat(val):
        val = float(val)
        if (val > 0) and (val <= 24):
            partite_coordinate[index_base + 1] = 1
        elif (val > 24) and (val <= 27):
            partite_coordinate[index_base + 2] = 1
        elif (val > 27) and (val <= 32):
            partite_coordinate[index_base + 3] = 1
        elif (val > 32):
            partite_coordinate[index_base + 4] = 1
        elif (val <= 0):
            partite_coordinate[index_base + 10] = 1
    else:
        partite_coordinate[index_base + 10] = 1

    return partite_coordinate