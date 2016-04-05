import pandas as pd
import numpy as np
import os
__author__ = 'Memray'

'''
Initialization part
'''
convert_dict = {}
vert_name = ["HOSPITAL","HOSPITAL","HOSPITAL","HOSPITAL","HOSPITAL","HOSPITAL","HOSPITAL","HOSPITAL","HOSPITAL","HOSPITAL","PROCEDURE_CODE","PROCEDURE_CODE","PROCEDURE_CODE","PROCEDURE_CODE","PROCEDURE_CODE","PROCEDURE_CODE","PROCEDURE_CODE","PROCEDURE_CODE","PROCEDURE_CODE","PROCEDURE_CODE","DIAGNOSIS_CODE","DIAGNOSIS_CODE","DIAGNOSIS_CODE","DIAGNOSIS_CODE","DIAGNOSIS_CODE","DIAGNOSIS_CODE","DIAGNOSIS_CODE","DIAGNOSIS_CODE","DIAGNOSIS_CODE","DIAGNOSIS_CODE","FINANCIAL_CLASS_DESCRIPTION","FINANCIAL_CLASS_DESCRIPTION","FINANCIAL_CLASS_DESCRIPTION","FINANCIAL_CLASS_DESCRIPTION","FINANCIAL_CLASS_DESCRIPTION","FINANCIAL_CLASS_DESCRIPTION","FINANCIAL_CLASS_DESCRIPTION","FINANCIAL_CLASS_DESCRIPTION","FINANCIAL_CLASS_DESCRIPTION","FINANCIAL_CLASS_DESCRIPTION","DRG_CODE","DRG_CODE","DRG_CODE","DRG_CODE","DRG_CODE","DRG_CODE","DRG_CODE","DRG_CODE","DRG_CODE","DRG_CODE","SEVERITY_OF_ILLNESS","SEVERITY_OF_ILLNESS","SEVERITY_OF_ILLNESS","SEVERITY_OF_ILLNESS","SEVERITY_OF_ILLNESS","SEVERITY_OF_ILLNESS","SEVERITY_OF_ILLNESS","SEVERITY_OF_ILLNESS","SEVERITY_OF_ILLNESS","SEVERITY_OF_ILLNESS","Smoking","Smoking","Smoking","Smoking","Smoking","Smoking","Smoking","Smoking","Smoking","Smoking","AGE_ON_CONTACT_DATE","AGE_ON_CONTACT_DATE","AGE_ON_CONTACT_DATE","AGE_ON_CONTACT_DATE","AGE_ON_CONTACT_DATE","AGE_ON_CONTACT_DATE","AGE_ON_CONTACT_DATE","AGE_ON_CONTACT_DATE","AGE_ON_CONTACT_DATE","AGE_ON_CONTACT_DATE","FEMALE","FEMALE","FEMALE","FEMALE","FEMALE","FEMALE","FEMALE","FEMALE","FEMALE","FEMALE","BMI","BMI","BMI","BMI","BMI","BMI","BMI","BMI","BMI","BMI","BP_SYSTOLIC","BP_SYSTOLIC","BP_SYSTOLIC","BP_SYSTOLIC","BP_SYSTOLIC","BP_SYSTOLIC","BP_SYSTOLIC","BP_SYSTOLIC","BP_SYSTOLIC","BP_SYSTOLIC","DIAB","DIAB","DIAB","DIAB","DIAB","DIAB","DIAB","DIAB","DIAB","DIAB","COPD_DX","COPD_DX","COPD_DX","COPD_DX","COPD_DX","COPD_DX","COPD_DX","COPD_DX","COPD_DX","COPD_DX","GLUCOSE","GLUCOSE","GLUCOSE","GLUCOSE","GLUCOSE","GLUCOSE","GLUCOSE","GLUCOSE","GLUCOSE","GLUCOSE","POTASSIUM(K)","POTASSIUM(K)","POTASSIUM(K)","POTASSIUM(K)","POTASSIUM(K)","POTASSIUM(K)","POTASSIUM(K)","POTASSIUM(K)","POTASSIUM(K)","POTASSIUM(K)","SODIUM(NA)","SODIUM(NA)","SODIUM(NA)","SODIUM(NA)","SODIUM(NA)","SODIUM(NA)","SODIUM(NA)","SODIUM(NA)","SODIUM(NA)","SODIUM(NA)","TOTAL_PROTEIN","TOTAL_PROTEIN","TOTAL_PROTEIN","TOTAL_PROTEIN","TOTAL_PROTEIN","TOTAL_PROTEIN","TOTAL_PROTEIN","TOTAL_PROTEIN","TOTAL_PROTEIN","TOTAL_PROTEIN","PROTHROMBIN_GENE_ANALYSIS","PROTHROMBIN_GENE_ANALYSIS","PROTHROMBIN_GENE_ANALYSIS","PROTHROMBIN_GENE_ANALYSIS","PROTHROMBIN_GENE_ANALYSIS","PROTHROMBIN_GENE_ANALYSIS","PROTHROMBIN_GENE_ANALYSIS","PROTHROMBIN_GENE_ANALYSIS","PROTHROMBIN_GENE_ANALYSIS","PROTHROMBIN_GENE_ANALYSIS","ACTIVATED_PTT","ACTIVATED_PTT","ACTIVATED_PTT","ACTIVATED_PTT","ACTIVATED_PTT","ACTIVATED_PTT","ACTIVATED_PTT","ACTIVATED_PTT","ACTIVATED_PTT","ACTIVATED_PTT","ASPARTATE_AMINOT.(AST)","ASPARTATE_AMINOT.(AST)","ASPARTATE_AMINOT.(AST)","ASPARTATE_AMINOT.(AST)","ASPARTATE_AMINOT.(AST)","ASPARTATE_AMINOT.(AST)","ASPARTATE_AMINOT.(AST)","ASPARTATE_AMINOT.(AST)","ASPARTATE_AMINOT.(AST)","ASPARTATE_AMINOT.(AST)","TOTAL_BILIRUBIN","TOTAL_BILIRUBIN","TOTAL_BILIRUBIN","TOTAL_BILIRUBIN","TOTAL_BILIRUBIN","TOTAL_BILIRUBIN","TOTAL_BILIRUBIN","TOTAL_BILIRUBIN","TOTAL_BILIRUBIN","TOTAL_BILIRUBIN","ALBUMIN","ALBUMIN","ALBUMIN","ALBUMIN","ALBUMIN","ALBUMIN","ALBUMIN","ALBUMIN","ALBUMIN","ALBUMIN","ALKALINE_PHOSPHATASE","ALKALINE_PHOSPHATASE","ALKALINE_PHOSPHATASE","ALKALINE_PHOSPHATASE","ALKALINE_PHOSPHATASE","ALKALINE_PHOSPHATASE","ALKALINE_PHOSPHATASE","ALKALINE_PHOSPHATASE","ALKALINE_PHOSPHATASE","ALKALINE_PHOSPHATASE","UREA_NITROGEN","UREA_NITROGEN","UREA_NITROGEN","UREA_NITROGEN","UREA_NITROGEN","UREA_NITROGEN","UREA_NITROGEN","UREA_NITROGEN","UREA_NITROGEN","UREA_NITROGEN","CALCIUM(CA)","CALCIUM(CA)","CALCIUM(CA)","CALCIUM(CA)","CALCIUM(CA)","CALCIUM(CA)","CALCIUM(CA)","CALCIUM(CA)","CALCIUM(CA)","CALCIUM(CA)","HGB","HGB","HGB","HGB","HGB","HGB","HGB","HGB","HGB","HGB","HEMATOCRIT(HCT)","HEMATOCRIT(HCT)","HEMATOCRIT(HCT)","HEMATOCRIT(HCT)","HEMATOCRIT(HCT)","HEMATOCRIT(HCT)","HEMATOCRIT(HCT)","HEMATOCRIT(HCT)","HEMATOCRIT(HCT)","HEMATOCRIT(HCT)","RBC","RBC","RBC","RBC","RBC","RBC","RBC","RBC","RBC","RBC","MCH","MCH","MCH","MCH","MCH","MCH","MCH","MCH","MCH","MCH","MCV","MCV","MCV","MCV","MCV","MCV","MCV","MCV","MCV","MCV","MCHC","MCHC","MCHC","MCHC","MCHC","MCHC","MCHC","MCHC","MCHC","MCHC","RDW","RDW","RDW","RDW","RDW","RDW","RDW","RDW","RDW","RDW","CREATININE","CREATININE","CREATININE","CREATININE","CREATININE","CREATININE","CREATININE","CREATININE","CREATININE","CREATININE","PLATELETS","PLATELETS","PLATELETS","PLATELETS","PLATELETS","PLATELETS","PLATELETS","PLATELETS","PLATELETS","PLATELETS","WBC","WBC","WBC","WBC","WBC","WBC","WBC","WBC","WBC","WBC","ABS_NEUTROPHILS","ABS_NEUTROPHILS","ABS_NEUTROPHILS","ABS_NEUTROPHILS","ABS_NEUTROPHILS","ABS_NEUTROPHILS","ABS_NEUTROPHILS","ABS_NEUTROPHILS","ABS_NEUTROPHILS","ABS_NEUTROPHILS","ABS_LYMPHOCYTES","ABS_LYMPHOCYTES","ABS_LYMPHOCYTES","ABS_LYMPHOCYTES","ABS_LYMPHOCYTES","ABS_LYMPHOCYTES","ABS_LYMPHOCYTES","ABS_LYMPHOCYTES","ABS_LYMPHOCYTES","ABS_LYMPHOCYTES","ABS_MONOCYTES","ABS_MONOCYTES","ABS_MONOCYTES","ABS_MONOCYTES","ABS_MONOCYTES","ABS_MONOCYTES","ABS_MONOCYTES","ABS_MONOCYTES","ABS_MONOCYTES","ABS_MONOCYTES","CARBON_DIOXIDE(CO2)","CARBON_DIOXIDE(CO2)","CARBON_DIOXIDE(CO2)","CARBON_DIOXIDE(CO2)","CARBON_DIOXIDE(CO2)","CARBON_DIOXIDE(CO2)","CARBON_DIOXIDE(CO2)","CARBON_DIOXIDE(CO2)","CARBON_DIOXIDE(CO2)","CARBON_DIOXIDE(CO2)"]
vert_vals = ["PAS","SHY","PUH","SMH","MER","MCK","NWH","HRY","HAM","N/A","3241","3249","3220","3230","3224","3229","3259","3239","3452","N/A","1623","1625","1629","1624","1628","1622","-","-","-","N/A","MEDICARE_PART_A","SECURITY_BLUE_HMO","UPMC_HP_MEDICARE_HMO","B/C_KEYSTONE","UPMC_HEALTH_NETWORK","ADVANTRA_MC_HMO","OTHER_MC_HMO","BEST_HEALTH_CARE","HLTH_AMER_COMM_MN_CR","N/A","164","163","3","165","167","168","166","75","-","N/A","2","3","4","1","-","-","-","-","-","N/A","Quit","Yes","Never","Not_Asked","Passive","-","-","-","-","N/A","<48","48-59","59-69","69-80",">80","-","-","-","-","N/A","Male","Female","-","-","-","-","-","-","-","N/A","<18","18-25","25-31","31-38",">38","-","-","-","-","N/A","<102","102-114","114-127","127-137","137-148","148-160",">160","-","-","N/A","No","Yes","-","-","-","-","-","-","-","N/A","No","Yes","-","-","-","-","-","-","-","N/A","<70","70-88","88-107","107-124","124-144",">144","-","-","-","N/A","<3.6","3.6-4.6","4.6-5.1",">5.1","-","-","-","-","-","N/A","<130","130-133","133-136","-136-140",">140","-","-","-","-","N/A","<6","6-7","7-7.8","7.8-8.2",">8.2","-","-","-","-","N/A","<10","10-16",">16","-","-","-","-","-","-","N/A","<34","34-42",">42","-","-","-","-","-","-","N/A","<14","14-21","21-28","28-36",">36","-","-","-","-","N/A","<0.25","0.25-0.45","0.45-0.75",">0.75","-","-","-","-","-","N/A","<2.8","2.8-3.5",">3.5","-","-","-","-","-","-","N/A","<65","65-110","110-175",">175","-","-","-","-","-","N/A","<10","10-15.5","15.5-22.5","22.5-33",">33","-","-","-","-","N/A","<8.5","8.5-10",">10","-","-","-","-","-","-","N/A","<9","9-11","11-13.5","13.5-15",">15","","-","-","-","N/A","<28","28-34","34-37","37-40","40-45",">45","-","-","-","N/A","<2.9","2.9-3.5","3.5-4","4-4.9",">4.9","-","-","-","-","N/A","<28","28-34",">34","-","-","-","-","-","-","N/A","<81","81-88","88-93","93-100",">100","-","-","-","-","N/A","<32","32-33","33-34.2","34.2-35",">35","-","-","-","-","N/A","<13","13-15","15-17",">17","-","-","-","-","-","N/A","<1.3",">1.3","-","-","-","-","-","-","-","N/A","<140","140-275","275-320","320-485",">485","-","-","-","-","N/A","<5.2","5.2-7","7-11","11-14",">14","-","-","-","-","N/A","<3","3-4.5","4.5-6.5","6.5-10",">10","-","-","-","-","N/A","<0.95","0.95-2","2-3",">3","-","-","-","-","-","N/A","<0.3","0.3-10",">10","-","-","-","-","-","-","N/A","<24","24-27","27-32",">32","-","-","-","-","-","N/A"]

for i in range(len(vert_name)):
    key = vert_name[i]
    value = vert_vals[i]
    if not key in convert_dict:
        convert_dict[key] = []
    convert_dict[key].append(value)

def convert_into_PartiteGraph(raw_data):
    partite_coordinate = np.zeros(390)

    print(raw_data)
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

# ########## INDEX=7 smoking >>>  ############### 61-70 'Smoking'
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

    pass
# ########## INDEX=9 sex >>>  ############### 81-90 'FEMALE'
# ktery:=25:kip:=-1:
# for i from 1 to nopato do kip:=-1:
#    if HCCdatac[i,ktery] =0                                    then    cykly[i,81]:=1:kip:=1: end if:
#    if HCCdatac[i,ktery] =1                                    then    cykly[i,82]:=1:kip:=1: end if:
#  if kip<0                                                     then    cykly[i,90]:=1: end if:
# end do:
# #testcykly:=Vector(1..10,0):for i from 81 to 90 do for j from 1 to nopato do testcykly[i-80]:=testcykly[i-80]+cykly[j,i]: end do:end do:LL:=[seq([i,testcykly[i]],i=1..10)]:pointplot(LL,symbol=solidbox,symbolsize=30,title=partnames[9]);
#
# ########## INDEX=10 BMI >>>  ############### 91-100
# ktery:=26:kip:=-1:
# for i from 1 to nopato do kip:=-1:
#    if HCCdatac[i,ktery] >0 and  HCCdatac[i,ktery] <18                                     then    cykly[i,91]:=1:kip:=1: end if:
#    if HCCdatac[i,ktery] >=18 and HCCdatac[i,ktery] <25                                    then    cykly[i,92]:=1:kip:=1: end if:
#    if HCCdatac[i,ktery] >=25 and HCCdatac[i,ktery] <31                                    then    cykly[i,93]:=1:kip:=1: end if:
#    if HCCdatac[i,ktery] >=31 and HCCdatac[i,ktery] <38                                    then    cykly[i,94]:=1:kip:=1: end if:
#    if HCCdatac[i,ktery] >=38                                                              then    cykly[i,95]:=1:kip:=1: end if:
# if kip<0                                                                                  then    cykly[i,100]:=1: end if:
# end do:
# #testcykly:=Vector(1..10,0):for i from 91 to 100 do for j from 1 to nopato do testcykly[i-90]:=testcykly[i-90]+cykly[j,i]: end do:end do:LL:=[seq([i,testcykly[i]],i=1..10)]:pointplot(LL,symbol=solidbox,symbolsize=30,title=partnames[10]);
#
# ########## INDEX=11 Tri years >>>  ############### 101-110
# ktery:=28:kip:=-1:
# for i from 1 to nopato do kip:=-1:
#    if HCCdatac[i,ktery] >0 and HCCdatac[i,ktery] <=102      then    cykly[i,101]:=1:kip:=1: end if:
#    if HCCdatac[i,ktery] >102 and HCCdatac[i,ktery] <=114    then    cykly[i,102]:=1:kip:=1: end if:
#    if HCCdatac[i,ktery] >114 and HCCdatac[i,ktery] <=127    then    cykly[i,103]:=1:kip:=1: end if:
#    if HCCdatac[i,ktery] >127 and HCCdatac[i,ktery] <=137    then    cykly[i,104]:=1:kip:=1: end if:
#    if HCCdatac[i,ktery] >137 and HCCdatac[i,ktery] <=148    then    cykly[i,105]:=1:kip:=1: end if:
#    if HCCdatac[i,ktery] >148 and HCCdatac[i,ktery] <=160    then    cykly[i,106]:=1:kip:=1: end if:
#    if HCCdatac[i,ktery] >160                                then    cykly[i,107]:=1 end if:
#   if kip<0                                                  then    cykly[i,110]:=1: end if:
# end do:
# #testcykly:=Vector(1..10,0):for i from 101 to 110 do for j from 1 to nopato do testcykly[i-100]:=testcykly[i-100]+cykly[j,i]: end do:end do:LL:=[seq([i,testcykly[i]],i=1..10)]:pointplot(LL,symbol=solidbox,symbolsize=30,title=partnames[11]);
#
#
# ########## INDEX=12 diabetes >>>  ############### 111-120
# ktery:=31:kip:=-1:
# for i from 1 to nopato do kip:=-1:
#    if HCCdatac[i,ktery] =0                                    then    cykly[i,111]:=1:kip:=1: end if:
#    if HCCdatac[i,ktery] =1                                    then    cykly[i,112]:=1:kip:=1: end if:
#    if kip<0                                                   then    cykly[i,120]:=1: end if:
# end do:
# #testcykly:=Vector(1..10,0):for i from 111 to 120 do for j from 1 to nopato do testcykly[i-110]:=testcykly[i-110]+cykly[j,i]: end do:end do:LL:=[seq([i,testcykly[i]],i=1..10)]:pointplot(LL,symbol=solidbox,symbolsize=30,title=partnames[12]);
#
#
# ########## INDEX=13 COPD >>>  ############### 121-130
# ktery:=34:kip:=-1:
# for i from 1 to nopato do kip:=-1:
#    if HCCdatac[i,ktery] =0                                    then    cykly[i,121]:=1:kip:=1: end if:
#    if HCCdatac[i,ktery] =1                                    then    cykly[i,122]:=1:kip:=1: end if:
#     if kip<0                                                  then    cykly[i,130]:=1: end if:
# end do:
# #testcykly:=Vector(1..10,0):for i from 121 to 130 do for j from 1 to nopato do testcykly[i-120]:=testcykly[i-120]+cykly[j,i]: end do:end do:LL:=[seq([i,testcykly[i]],i=1..10)]:pointplot(LL,symbol=solidbox,symbolsize=30,title=partnames[13]);
#
#
# ########## INDEX=14 glucose >>>  ############### 131-140
# ktery:=41:kip:=-1:
# for i from 1 to nopato do kip:=-1:
#    if HCCdatac[i,ktery] >0 and HCCdatac[i,ktery] <=70                                     then    cykly[i,131]:=1:kip:=1: end if:
#    if HCCdatac[i,ktery] >70 and HCCdatac[i,ktery] <=88                                    then    cykly[i,132]:=1:kip:=1: end if:
#    if HCCdatac[i,ktery] >88 and HCCdatac[i,ktery] <=107                                   then    cykly[i,133]:=1:kip:=1: end if:
#    if HCCdatac[i,ktery] >107 and HCCdatac[i,ktery] <=124                                  then    cykly[i,134]:=1:kip:=1: end if:
#    if HCCdatac[i,ktery] >124 and HCCdatac[i,ktery] <=144                                  then    cykly[i,135]:=1:kip:=1: end if:
#    if HCCdatac[i,ktery] >144                                                              then    cykly[i,136]:=1:kip:=1: end if:
#     if kip<0                                                                              then    cykly[i,140]:=1: end if:
# end do:
# #testcykly:=Vector(1..10,0):for i from 131 to 140 do for j from 1 to nopato do testcykly[i-130]:=testcykly[i-130]+cykly[j,i]: end do:end do:LL:=[seq([i,testcykly[i]],i=1..10)]:pointplot(LL,symbol=solidbox,symbolsize=30,title=partnames[14]);
#
# ########## INDEX=15 POtassium >>>  ############### 141-150
# ktery:=42:kip:=-1:
# for i from 1 to nopato do kip:=-1:
#    if HCCdatac[i,ktery] >0 and HCCdatac[i,ktery] <=3.6                                      then    cykly[i,141]:=1:kip:=1: end if:
#    if HCCdatac[i,ktery] >3.6 and HCCdatac[i,ktery] <=4.6                                    then    cykly[i,142]:=1:kip:=1: end if:
#    if HCCdatac[i,ktery] >4.6 and HCCdatac[i,ktery] <=5.1                                    then    cykly[i,143]:=1:kip:=1: end if:
#     if HCCdatac[i,ktery] >5.1                                                               then    cykly[i,144]:=1:kip:=1: end if:
# if kip<0                                                                                    then    cykly[i,150]:=1: end if:
# end do:
# #testcykly:=Vector(1..10,0):for i from 141 to 150 do for j from 1 to nopato do testcykly[i-140]:=testcykly[i-140]+cykly[j,i]: end do:end do:LL:=[seq([i,testcykly[i]],i=1..10)]:pointplot(LL,symbol=solidbox,symbolsize=30,title=partnames[15]);
#
#  ########## INDEX=16 Sodium >>>  ############### 151-160
# ktery:=43:kip:=-1:
# for i from 1 to nopato do kip:=-1:
#    if HCCdatac[i,ktery] >0 and HCCdatac[i,ktery]<=130                                      then    cykly[i,151]:=1:kip:=1: end if:
#    if HCCdatac[i,ktery] >130 and HCCdatac[i,ktery]<=133                                    then    cykly[i,152]:=1:kip:=1: end if:
#    if HCCdatac[i,ktery] >133 and HCCdatac[i,ktery]<=136                                    then    cykly[i,153]:=1:kip:=1: end if:
#    if HCCdatac[i,ktery] >136 and HCCdatac[i,ktery]<=140                                    then    cykly[i,154]:=1:kip:=1: end if:
#    if HCCdatac[i,ktery] >140                                                               then    cykly[i,155]:=1:kip:=1: end if:
# if kip<0                                                                                   then    cykly[i,160]:=1: end if:
# end do:
# #testcykly:=Vector(1..10,0):for i from 151 to 160 do for j from 1 to nopato do testcykly[i-150]:=testcykly[i-150]+cykly[j,i]: end do:end do:LL:=[seq([i,testcykly[i]],i=1..10)]:pointplot(LL,symbol=solidbox,symbolsize=30,title=partnames[16]);
#
# ########## INDEX=17 total protein >>>  ############### 161-170
# ktery:=44:kip:=-1:
# for i from 1 to nopato do kip:=-1:
#    if HCCdatac[i,ktery] >0 and  HCCdatac[i,ktery]<=6                                   then    cykly[i,161]:=1:kip:=1: end if:
#    if HCCdatac[i,ktery] >6 and HCCdatac[i,ktery]<=7                                    then    cykly[i,162]:=1:kip:=1: end if:
#   if HCCdatac[i,ktery] >7 and HCCdatac[i,ktery]<=7.8                                   then    cykly[i,163]:=1:kip:=1: end if:
#    if HCCdatac[i,ktery] >7.8 and HCCdatac[i,ktery]<=8.2                                then    cykly[i,164]:=1:kip:=1: end if:
#   if HCCdatac[i,ktery] >8.2                                                            then    cykly[i,165]:=1:kip:=1: end if:
#
#   if kip<0                                                                             then    cykly[i,170]:=1: end if:
# end do:
# #testcykly:=Vector(1..10,0):for i from 161 to 170 do for j from 1 to nopato do testcykly[i-160]:=testcykly[i-160]+cykly[j,i]: end do:end do:LL:=[seq([i,testcykly[i]],i=1..10)]:pointplot(LL,symbol=solidbox,symbolsize=30,title=partnames[17]);
#
# ########## INDEX=18 protothrombin >>>  ############### 171-180 WHAT'S THIS??? I changed to PROTHROMBIN_GENE_ANALYSIS, but no similar feature has scale in (0,10],(10,16],(16,)
# ktery:=45:kip:=-1:
# for i from 1 to nopato do kip:=-1:
#    if HCCdatac[i,ktery] >0 and HCCdatac[i,ktery]<=10                                     then    cykly[i,171]:=1:kip:=1: end if:
#    if HCCdatac[i,ktery] >10 and HCCdatac[i,ktery]<=16                                    then    cykly[i,172]:=1:kip:=1: end if:
#    if HCCdatac[i,ktery] >16                                                              then    cykly[i,173]:=1:kip:=1: end if:
# if kip<0                                                                                 then    cykly[i,180]:=1: end if:
#
# end do:
# #testcykly:=Vector(1..10,0):for i from 171 to 180 do for j from 1 to nopato do testcykly[i-170]:=testcykly[i-170]+cykly[j,i]: end do:end do:LL:=[seq([i,testcykly[i]],i=1..10)]:pointplot(LL,symbol=solidbox,symbolsize=30,title=partnames[18]);
#
#
# ########## INDEX=19 activated PTT >>>  ############### 181-190
# ktery:=46:kip:=-1:
# for i from 1 to nopato do kip:=-1:
#    if HCCdatac[i,ktery] >0 and  HCCdatac[i,ktery]<=34                                    then    cykly[i,181]:=1:kip:=1: end if:
#    if HCCdatac[i,ktery] >34 and HCCdatac[i,ktery]<=42                                    then    cykly[i,182]:=1:kip:=1: end if:
#    if HCCdatac[i,ktery] >42                                                              then    cykly[i,183]:=1:kip:=1: end if:
# if kip<0                                                                                 then    cykly[i,190]:=1: end if:
#
# end do:
# #testcykly:=Vector(1..10,0):for i from 181 to 190 do for j from 1 to nopato do testcykly[i-180]:=testcykly[i-180]+cykly[j,i]: end do:end do:LL:=[seq([i,testcykly[i]],i=1..10)]:pointplot(LL,symbol=solidbox,symbolsize=30,title=partnames[19]);
#
# ########## INDEX=20 AST >>>  ############### 191-200
# ktery:=48:kip:=-1:
# for i from 1 to nopato do kip:=-1:
#    if HCCdatac[i,ktery] >0 and HCCdatac[i,ktery]<=14                                     then    cykly[i,191]:=1:kip:=1: end if:
#    if HCCdatac[i,ktery] >14 and HCCdatac[i,ktery]<=21                                    then    cykly[i,192]:=1:kip:=1: end if:
#    if HCCdatac[i,ktery] >21 and HCCdatac[i,ktery]<=28                                    then    cykly[i,193]:=1:kip:=1: end if:
#    if HCCdatac[i,ktery] >28 and HCCdatac[i,ktery]<=36                                    then    cykly[i,194]:=1:kip:=1: end if:
#    if HCCdatac[i,ktery] >36                                                              then    cykly[i,195]:=1:kip:=1: end if:
#   if kip<0                                                                               then    cykly[i,200]:=1: end if:
# end do:
# #testcykly:=Vector(1..10,0):for i from 191 to 200 do for j from 1 to nopato do testcykly[i-190]:=testcykly[i-190]+cykly[j,i]: end do:end do:LL:=[seq([i,testcykly[i]],i=1..10)]:pointplot(LL,symbol=solidbox,symbolsize=30,title=partnames[20]);
#
# ########## INDEX=21 BILI >>>  ############### 201-210
# ktery:=51:kip:=-1:
# for i from 1 to nopato do kip:=-1:
#   if HCCdatac[i,ktery] >0 then
#    if log10(HCCdatac[i,ktery])<=-0.603                                                      then    cykly[i,201]:=1:kip:=1: end if:
#    if log10(HCCdatac[i,ktery]) > -0.603 and log10(HCCdatac[i,ktery])<=-0.356                then    cykly[i,202]:=1:kip:=1: end if:
#    if log10(HCCdatac[i,ktery]) > -0.356 and log10(HCCdatac[i,ktery])<=-0.1174               then    cykly[i,203]:=1:kip:=1: end if:
#    if log10(HCCdatac[i,ktery]) > -0.1174                                                    then    cykly[i,204]:=1:kip:=1: end if:
#  end if:
# if kip<0                                                                                    then    cykly[i,210]:=1: end if:
# end do:
# #testcykly:=Vector(1..10,0):for i from 201 to 210 do for j from 1 to nopato do testcykly[i-200]:=testcykly[i-200]+cykly[j,i]: end do:end do:LL:=[seq([i,testcykly[i]],i=1..10)]:pointplot(LL,symbol=solidbox,symbolsize=30,title=partnames[21]);
#
# ########## INDEX=22 ALB >>>  ############### 211-220
# ktery:=56:kip:=-1:
# for i from 1 to nopato do kip:=-1:
#   if HCCdatac[i,ktery] >0 then
#    if log10(HCCdatac[i,ktery])<=0.442                                                       then    cykly[i,211]:=1:kip:=1: end if:
#    if log10(HCCdatac[i,ktery])>0.442 and log10(HCCdatac[i,ktery])<=0.5344                   then    cykly[i,212]:=1:kip:=1: end if:
#     if log10(HCCdatac[i,ktery]) >0.5344                                                     then    cykly[i,213]:=1:kip:=1: end if:
#   end if:
#  if kip<0                                                                                   then    cykly[i,220]:=1: end if:
# end do:
# #testcykly:=Vector(1..10,0):for i from 211 to 220 do for j from 1 to nopato do testcykly[i-210]:=testcykly[i-210]+cykly[j,i]: end do:end do:LL:=[seq([i,testcykly[i]],i=1..10)]:pointplot(LL,symbol=solidbox,symbolsize=30,title=partnames[22]);
#
#
# ########## INDEX=23 ALKP >>>  ############### 221-230
# ktery:=57:kip:=-1:
# for i from 1 to nopato do kip:=-1:
#   if HCCdatac[i,ktery] >0 then
#    if log10(HCCdatac[i,ktery]) <=1.8                                                       then    cykly[i,221]:=1:kip:=1: end if:
#    if log10(HCCdatac[i,ktery]) >1.8 and log10(HCCdatac[i,ktery])<=2.03                     then    cykly[i,222]:=1:kip:=1: end if:
#    if log10(HCCdatac[i,ktery]) >2.03 and log10(HCCdatac[i,ktery])<=2.238                   then    cykly[i,223]:=1:kip:=1: end if:
#    if log10(HCCdatac[i,ktery]) >2.238                                                      then    cykly[i,224]:=1:kip:=1: end if:
#   end if:
#  if kip<0                                                                                  then    cykly[i,230]:=1: end if:
# end do:
# #testcykly:=Vector(1..10,0):for i from 221 to 230 do for j from 1 to nopato do testcykly[i-220]:=testcykly[i-220]+cykly[j,i]: end do:end do:LL:=[seq([i,testcykly[i]],i=1..10)]:pointplot(LL,symbol=solidbox,symbolsize=30,title=partnames[23]);
#
# ########## INDEX=24 Urea N >>>  ############### 231-240
# ktery:=59:kip:=-1:
# for i from 1 to nopato do kip:=-1:
#
#    if HCCdatac[i,ktery] >0 and HCCdatac[i,ktery]<=10                                       then    cykly[i,231]:=1:kip:=1: end if:
#    if HCCdatac[i,ktery] >10 and HCCdatac[i,ktery]<=15.6                                    then    cykly[i,232]:=1:kip:=1: end if:
#    if HCCdatac[i,ktery] >15.6 and HCCdatac[i,ktery]<=22.3                                  then    cykly[i,233]:=1:kip:=1: end if:
#    if HCCdatac[i,ktery] >22.3 and HCCdatac[i,ktery]<=33                                    then    cykly[i,234]:=1:kip:=1: end if:
#    if HCCdatac[i,ktery] >33                                                                then    cykly[i,235]:=1:kip:=1: end if:
#   if kip<0                                                                                 then    cykly[i,240]:=1: end if:
# end do:
# #testcykly:=Vector(1..10,0):for i from 231 to 240 do for j from 1 to nopato do testcykly[i-230]:=testcykly[i-230]+cykly[j,i]: end do:end do:LL:=[seq([i,testcykly[i]],i=1..10)]:pointplot(LL,symbol=solidbox,symbolsize=30,title=partnames[24]);
#
#
# ########## INDEX=25 Calcium >>>  ############### 241-250
# ktery:=60:kip:=-1:
# for i from 1 to nopato do kip:=-1:
#
#    if HCCdatac[i,ktery] >0 and  HCCdatac[i,ktery]<=8.5                                    then    cykly[i,241]:=1:kip:=1: end if:
#    if HCCdatac[i,ktery] >8.5 and HCCdatac[i,ktery]<=10                                    then    cykly[i,242]:=1:kip:=1: end if:
#    if HCCdatac[i,ktery] >10                                                               then    cykly[i,243]:=1:kip:=1: end if:
#
#   if kip<0                                                                                then    cykly[i,250]:=1: end if:
#
# end do:
# #testcykly:=Vector(1..10,0):for i from 241 to 250 do for j from 1 to nopato do testcykly[i-240]:=testcykly[i-240]+cykly[j,i]: end do:end do:LL:=[seq([i,testcykly[i]],i=1..10)]:pointplot(LL,symbol=solidbox,symbolsize=30,title=partnames[25]);
#
# ########## INDEX=26 HGB >>>  ############### 251-260
# ktery:=61:kip:=-1:
# for i from 1 to nopato do kip:=-1:
#
#    if HCCdatac[i,ktery] >0 and  HCCdatac[i,ktery]<=9                                   then    cykly[i,251]:=1:kip:=1: end if:
#    if HCCdatac[i,ktery] >9 and HCCdatac[i,ktery]<=11                                   then    cykly[i,252]:=1:kip:=1: end if:
#  if HCCdatac[i,ktery] >11 and HCCdatac[i,ktery]<=13.5                                  then    cykly[i,253]:=1:kip:=1: end if:
#    if HCCdatac[i,ktery] >13.5 and HCCdatac[i,ktery]<=15                                then    cykly[i,254]:=1:kip:=1: end if:
#  if HCCdatac[i,ktery] >15                                                              then    cykly[i,255]:=1:kip:=1: end if:
#  if kip<0                                                                              then    cykly[i,260]:=1: end if:
#
# end do:
# #testcykly:=Vector(1..10,0):for i from 251 to 260 do for j from 1 to nopato do testcykly[i-250]:=testcykly[i-250]+cykly[j,i]: end do:end do:LL:=[seq([i,testcykly[i]],i=1..10)]:pointplot(LL,symbol=solidbox,symbolsize=30,title=partnames[26]);
#
# ########## INDEX=27 HECT >>>  ############### 261-270
# ktery:=62:kip:=-1:
# for i from 1 to nopato do kip:=-1:
#
#    if HCCdatac[i,ktery] >0 and HCCdatac[i,ktery]<=28                                     then    cykly[i,261]:=1:kip:=1: end if:
#    if HCCdatac[i,ktery] >28 and HCCdatac[i,ktery]<=34                                    then    cykly[i,262]:=1:kip:=1: end if:
#    if HCCdatac[i,ktery] >34 and HCCdatac[i,ktery]<=37                                    then    cykly[i,263]:=1:kip:=1: end if:
#    if HCCdatac[i,ktery] >37 and HCCdatac[i,ktery]<=40                                    then    cykly[i,264]:=1:kip:=1: end if:
#    if HCCdatac[i,ktery] >40 and HCCdatac[i,ktery]<=45                                    then    cykly[i,265]:=1:kip:=1: end if:
#    if HCCdatac[i,ktery] >45                                                              then    cykly[i,266]:=1:kip:=1: end if:
#    if kip<0                                                                              then    cykly[i,270]:=1: end if:
# end do:
# #testcykly:=Vector(1..10,0):for i from 261 to 270 do for j from 1 to nopato do testcykly[i-260]:=testcykly[i-260]+cykly[j,i]: end do:end do:LL:=[seq([i,testcykly[i]],i=1..10)]:pointplot(LL,symbol=solidbox,symbolsize=30,title=partnames[27]);
#
# ########## INDEX=28 RBC >>>  ############### 271-280
# ktery:=63:kip:=-1:
# for i from 1 to nopato do kip:=-1:
#
#    if HCCdatac[i,ktery] >0 and  HCCdatac[i,ktery]<=2.9                                   then    cykly[i,271]:=1:kip:=1: end if:
#    if HCCdatac[i,ktery] >2.9 and HCCdatac[i,ktery]<=3.5                                  then    cykly[i,272]:=1:kip:=1: end if:
#    if HCCdatac[i,ktery] >3.5 and HCCdatac[i,ktery]<=4                                    then    cykly[i,273]:=1:kip:=1: end if:
#    if HCCdatac[i,ktery] >4 and HCCdatac[i,ktery]<=4.9                                    then    cykly[i,274]:=1:kip:=1: end if:
#    if HCCdatac[i,ktery] >4.9                                                             then    cykly[i,275]:=1:kip:=1: end if:
#    if kip<0                                                                              then    cykly[i,280]:=1: end if:
#
# end do:
# #testcykly:=Vector(1..10,0):for i from 271 to 280 do for j from 1 to nopato do testcykly[i-270]:=testcykly[i-270]+cykly[j,i]: end do:end do:LL:=[seq([i,testcykly[i]],i=1..10)]:pointplot(LL,symbol=solidbox,symbolsize=30,title=partnames[28]);
#
#
# ########## INDEX=29 MCH >>>  ############### 281-290
# ktery:=65:kip:=-1:
# for i from 1 to nopato do kip:=-1:
#
#    if HCCdatac[i,ktery] >0 and HCCdatac[i,ktery]<=28                                     then    cykly[i,281]:=1:kip:=1: end if:
#    if HCCdatac[i,ktery] >28 and HCCdatac[i,ktery]<=34                                    then    cykly[i,282]:=1:kip:=1: end if:
#    if HCCdatac[i,ktery] >34                                                              then    cykly[i,283]:=1:kip:=1: end if:
# if kip<0                                                                                 then    cykly[i,290]:=1: end if:
#
# end do:
# #testcykly:=Vector(1..10,0):for i from 281 to 290 do for j from 1 to nopato do testcykly[i-280]:=testcykly[i-280]+cykly[j,i]: end do:end do:LL:=[seq([i,testcykly[i]],i=1..10)]:pointplot(LL,symbol=solidbox,symbolsize=30,title=partnames[29]);
#
# ########## INDEX=30 MCV >>>  ############### 291-300
# ktery:=64:kip:=-1:
# for i from 1 to nopato do kip:=-1:
#    if HCCdatac[i,ktery] >0 and  HCCdatac[i,ktery]<=81                                    then    cykly[i,291]:=1:kip:=1: end if:
#    if HCCdatac[i,ktery] >81 and HCCdatac[i,ktery]<=88                                    then    cykly[i,292]:=1:kip:=1: end if:
#    if HCCdatac[i,ktery] >88 and HCCdatac[i,ktery]<=93                                    then    cykly[i,293]:=1:kip:=1: end if:
#    if HCCdatac[i,ktery] >93 and HCCdatac[i,ktery]<=100                                   then    cykly[i,294]:=1:kip:=1: end if:
#    if HCCdatac[i,ktery] >100                                                             then    cykly[i,295]:=1:kip:=1: end if:
#
#
#  if kip<0                                                                                then    cykly[i,300]:=1: end if:
# end do:
# #testcykly:=Vector(1..10,0):for i from 291 to 300 do for j from 1 to nopato do testcykly[i-290]:=testcykly[i-290]+cykly[j,i]: end do:end do:LL:=[seq([i,testcykly[i]],i=1..10)]:pointplot(LL,symbol=solidbox,symbolsize=30,title=partnames[30]);
#
# ########## INDEX=31 MCHC >>>  ############### 301-310
# ktery:=66:kip:=-1:
# for i from 1 to nopato do kip:=-1:
#
#    if HCCdatac[i,ktery] >0 and HCCdatac[i,ktery]<=32                                     then    cykly[i,301]:=1:kip:=1: end if:
#    if HCCdatac[i,ktery] >32 and HCCdatac[i,ktery]<=33                                    then    cykly[i,302]:=1:kip:=1: end if:
#    if HCCdatac[i,ktery] >33 and HCCdatac[i,ktery]<=34.2                                  then    cykly[i,303]:=1:kip:=1: end if:
#    if HCCdatac[i,ktery] >34.2 and HCCdatac[i,ktery]<=35                                  then    cykly[i,304]:=1:kip:=1: end if:
#    if HCCdatac[i,ktery] >35                                                              then    cykly[i,305]:=1:kip:=1: end if:
#
#    if kip<0                                                                              then    cykly[i,310]:=1: end if:
# end do:
# #testcykly:=Vector(1..10,0):for i from 301 to 310 do for j from 1 to nopato do testcykly[i-300]:=testcykly[i-300]+cykly[j,i]: end do:end do:LL:=[seq([i,testcykly[i]],i=1..10)]:pointplot(LL,symbol=solidbox,symbolsize=30,title=partnames[31]);
#
# ########## INDEX=32 RDW >>>  ############### 311-320
# ktery:=67:kip:=-1:
# for i from 1 to nopato do kip:=-1:
#    if HCCdatac[i,ktery] >0 and  HCCdatac[i,ktery] <=13                                    then    cykly[i,311]:=1:kip:=1: end if:
#    if HCCdatac[i,ktery] >13 and HCCdatac[i,ktery] <=15                                    then    cykly[i,312]:=1:kip:=1: end if:
#    if HCCdatac[i,ktery] >15 and HCCdatac[i,ktery] <=17                                    then    cykly[i,313]:=1:kip:=1: end if:
#    if HCCdatac[i,ktery] >17                                                               then    cykly[i,314]:=1:kip:=1: end if:
#
#
#  if kip<0                                                                                 then    cykly[i,320]:=1: end if:
# end do:
# #testcykly:=Vector(1..10,0):for i from 311 to 320 do for j from 1 to nopato do testcykly[i-310]:=testcykly[i-310]+cykly[j,i]: end do:end do:LL:=[seq([i,testcykly[i]],i=1..10)]:pointplot(LL,symbol=solidbox,symbolsize=30,title=partnames[32]);
#
# ########## INDEX=33 creatinine >>>  ############### 321-330
# ktery:=68:kip:=-1:
# for i from 1 to nopato do kip:=-1:
#    if HCCdatac[i,ktery] >0 and  HCCdatac[i,ktery] <=1.3            then    cykly[i,321]:=1:kip:=1: end if:
#    if HCCdatac[i,ktery] >1.3                                       then    cykly[i,322]:=1:kip:=1: end if:
#    if kip<0                                                        then    cykly[i,330]:=1: end if:
#
# end do:
# #testcykly:=Vector(1..10,0):for i from 321 to 330 do for j from 1 to nopato do testcykly[i-320]:=testcykly[i-320]+cykly[j,i]: end do:end do:LL:=[seq([i,testcykly[i]],i=1..10)]:pointplot(LL,symbol=solidbox,symbolsize=30,title=partnames[33]);
#
#
# ########## INDEX=34 platelets >>>  ############### 331-340
# ktery:=69:kip:=-1:
# for i from 1 to nopato do kip:=-1:
#  if HCCdatac[i,ktery] >0 then
#    if log10(HCCdatac[i,ktery])<=2.15                                                                       then    cykly[i,331]:=1:kip:=1: end if:
#    if log10(HCCdatac[i,ktery]) >2.15 and  log10(HCCdatac[i,ktery])<=2.44                                   then    cykly[i,332]:=1:kip:=1: end if:
#    if log10(HCCdatac[i,ktery]) >2.44 and  log10(HCCdatac[i,ktery])<=2.5                                    then    cykly[i,333]:=1:kip:=1: end if:
#    if log10(HCCdatac[i,ktery]) >2.5 and  log10(HCCdatac[i,ktery])<=2.685                                   then    cykly[i,334]:=1:kip:=1: end if:
#    if log10(HCCdatac[i,ktery]) >2.685                                                                      then    cykly[i,335]:=1:kip:=1: end if:
#
# end if:
#    if kip<0                                                                                                then    cykly[i,340]:=1: end if:
# end do:
# #testcykly:=Vector(1..10,0):for i from 331 to 340 do for j from 1 to nopato do testcykly[i-330]:=testcykly[i-330]+cykly[j,i]: end do:end do:LL:=[seq([i,testcykly[i]],i=1..10)]:pointplot(LL,symbol=solidbox,symbolsize=30,title=partnames[34]);
#
# ########## INDEX=35 WBC >>>  ############### 341-350
# ktery:=75:kip:=-1:
# for i from 1 to nopato do kip:=-1:
#  if HCCdatac[i,ktery] >0 then
#    if log10(HCCdatac[i,ktery])<=0.7193                                                                         then    cykly[i,341]:=1:kip:=1: end if:
#    if log10(HCCdatac[i,ktery]) >0.7193 and  log10(HCCdatac[i,ktery])<=0.843                                    then    cykly[i,342]:=1:kip:=1: end if:
#    if log10(HCCdatac[i,ktery]) >0.843 and  log10(HCCdatac[i,ktery])<=1.0276                                    then    cykly[i,343]:=1:kip:=1: end if:
#    if log10(HCCdatac[i,ktery]) >1.0276 and  log10(HCCdatac[i,ktery])<=1.158                                    then    cykly[i,344]:=1:kip:=1: end if:
#    if log10(HCCdatac[i,ktery]) >1.158                                                                          then    cykly[i,345]:=1:kip:=1: end if:
#
# end if:
#    if kip<0                                                                                                    then    cykly[i,350]:=1: end if:
#
# end do:
# #testcykly:=Vector(1..10,0):for i from 341 to 350 do for j from 1 to nopato do testcykly[i-340]:=testcykly[i-340]+cykly[j,i]: end do:end do:LL:=[seq([i,testcykly[i]],i=1..10)]:pointplot(LL,symbol=solidbox,symbolsize=30,title=partnames[35]);
#
# ########## INDEX=36 abs neutrophiles >>>  ############### 351-360
# ktery:=99:kip:=-1:
# for i from 1 to nopato do kip:=-1:
#  if HCCdatac[i,ktery] >0 then
#    if log10(HCCdatac[i,ktery])<=0.465                                                                        then    cykly[i,351]:=1:kip:=1: end if:
#    if log10(HCCdatac[i,ktery]) >0.465 and  log10(HCCdatac[i,ktery])<=0.6358                                  then    cykly[i,352]:=1:kip:=1: end if:
#    if log10(HCCdatac[i,ktery]) >0.6358 and  log10(HCCdatac[i,ktery])<=0.8                                    then    cykly[i,353]:=1:kip:=1: end if:
#    if log10(HCCdatac[i,ktery]) >0.8 and  log10(HCCdatac[i,ktery])<=0.9858                                    then    cykly[i,354]:=1:kip:=1: end if:
#    if log10(HCCdatac[i,ktery]) >0.9858                                                                       then    cykly[i,355]:=1:kip:=1: end if:
#
# end if:
#    if kip<0                                                                                                  then    cykly[i,360]:=1: end if:
#
# end do:
#
# #testcykly:=Vector(1..10,0):for i from 351 to 360 do for j from 1 to nopato do testcykly[i-350]:=testcykly[i-350]+cykly[j,i]: end do:end do:LL:=[seq([i,testcykly[i]],i=1..10)]:pointplot(LL,symbol=solidbox,symbolsize=30,title=partnames[36]);
#
# ########## INDEX=37 lymphocytes >>>  ############### 361-370
# ktery:=101:kip:=-1:
# for i from 1 to nopato do kip:=-1:
#  if HCCdatac[i,ktery] >0 then
#    if log10(HCCdatac[i,ktery])<=-0.0306                                                                       then    cykly[i,361]:=1:kip:=1: end if:
#    if log10(HCCdatac[i,ktery]) >-0.0306 and  log10(HCCdatac[i,ktery])<=0.2947                                 then    cykly[i,362]:=1:kip:=1: end if:
#    if log10(HCCdatac[i,ktery]) >0.2947 and  log10(HCCdatac[i,ktery])<=0.48                                    then    cykly[i,363]:=1:kip:=1: end if:
#
#    if log10(HCCdatac[i,ktery]) >0.48                                                                          then    cykly[i,364]:=1:kip:=1: end if:
#
# end if:
#    if kip<0                                                                                                   then    cykly[i,370]:=1: end if:
#
# end do:
# #testcykly:=Vector(1..10,0):for i from 361 to 370 do for j from 1 to nopato do testcykly[i-360]:=testcykly[i-360]+cykly[j,i]: end do:end do:LL:=[seq([i,testcykly[i]],i=1..10)]:pointplot(LL,symbol=solidbox,symbolsize=30,title=partnames[37]);
#
#
# ########## INDEX=38 monocytes >>>  ############### 371-380
# ktery:=103:kip:=-1:
# for i from 1 to nopato do kip:=-1:
#  if HCCdatac[i,ktery] >0 then
#    if log10(HCCdatac[i,ktery])<=-0.5764                                                                  then    cykly[i,371]:=1:kip:=1: end if:
#    if log10(HCCdatac[i,ktery]) >-0.5764 and  log10(HCCdatac[i,ktery])<=1                                 then    cykly[i,372]:=1:kip:=1: end if:
#    if log10(HCCdatac[i,ktery]) >1                                                                        then    cykly[i,373]:=1:kip:=1: end if:
#
#
# end if:
#    if kip<0                                                                                              then    cykly[i,380]:=1: end if:
#
# end do:
# #testcykly:=Vector(1..10,0):for i from 371 to 380 do for j from 1 to nopato do testcykly[i-370]:=testcykly[i-370]+cykly[j,i]: end do:end do:LL:=[seq([i,testcykly[i]],i=1..10)]:pointplot(LL,symbol=solidbox,symbolsize=30,title=partnames[38]);
#
#
# ########## INDEX=39 CO2 >>>  ############### 381-390
# ktery:=135:kip:=-1:
# for i from 1 to nopato do kip:=-1:
#    if HCCdatac[i,ktery] >0 and  HCCdatac[i,ktery] <=24                                    then    cykly[i,381]:=1:kip:=1: end if:
#    if HCCdatac[i,ktery] >24 and HCCdatac[i,ktery] <=27                                    then    cykly[i,382]:=1:kip:=1: end if:
#    if HCCdatac[i,ktery] >27 and HCCdatac[i,ktery] <=32                                    then    cykly[i,383]:=1:kip:=1: end if:
#    if HCCdatac[i,ktery] >32                                                               then    cykly[i,384]:=1:kip:=1: end if:
#
#
#  if kip<0                                                                                 then    cykly[i,390]:=1: end if:
# end do:
# #testcykly:=Vector(1..10,0):for i from 381 to 390 do for j from 1 to nopato do testcykly[i-380]:=testcykly[i-380]+cykly[j,i]: end do:end do:LL:=[seq([i,testcykly[i]],i=1..10)]:pointplot(LL,symbol=solidbox,symbolsize=30,title=partnames[39]);
#
#
