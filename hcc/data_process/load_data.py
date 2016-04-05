from hcc.data_process.partite_converter import *
import pandas as pd
import numpy as np
import os
__author__ = 'Memray'

if __name__=='__main__':
    '''
     read data by pandas, 1318 records in total
    '''
    data_path = '../../data/LungCombinedDataS.csv'
    data_frame = pd.read_csv(data_path)

    '''
    strip the column names as they contain annoying space
    '''
    data_frame.columns = [name.strip() for name in data_frame.columns.values]

    '''
    totally 1587 attributes, but only 38 are of interest
    '''
    col_names = ["ID","HOSPITAL","PROCEDURE_CODE","DIAGNOSIS_CODE","FINANCIAL_CLASS_DESCRIPTION","DRG_CODE","SEVERITY_OF_ILLNESS","Smoking","AGE_ON_CONTACT_DATE","FEM","BMI","BP_SYSTOLIC","DIAB","COPD_DX","GLUCOSE","POTASSIUM(K)","SODIUM(NA)","TOTAL_PROTEIN","PROTHROMBIN_GENE_ANALYSIS","ACTIVATED_PTT","ASPARTATE_AMINOT.(AST)","TOTAL_BILIRUBIN","ALBUMIN","ALKALINE_PHOSPHATASE","UREA_NITROGEN","CALCIUM(CA)","HGB","HEMATOCRIT(HCT)","RBC","MCH","MCV","MCHC","RDW","CREATININE","PLATELETS","WBC","ABS_NEUTROPHILS","ABS_LYMPHOCYTES","ABS_MONOCYTES","CARBON_DIOXIDE(CO2)"]
    # data_frame = data_frame.ix[: , col_names]

    '''
    Again, strip all the values
    '''
    for col in data_frame:
        if data_frame[col].dtype=='object':
            data_frame[col] = data_frame[col].str.strip()
            # data_frame["Make"] = df["Make"].map(str.strip)
            pass
            # for row in data_frame.ix[: , col]:
            #     pass
    '''
    revalue the data by mapping into the 10-level scale
    '''
    partite_data = []

    for col in data_frame:
        print(col+':'+str(len(data_frame[col].unique())))
        print(data_frame[col].unique())
        pass

    for d in data_frame.iterrows():
        partite_data.append(convert_into_PartiteGraph(d[1]))
    # print(d[1])
# calculate coordinate in terms of given two landmarks
# coordinate = get_coordinate(scale_df, lm1, lm2)