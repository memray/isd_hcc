# encoding: utf-8
from hcc.data_process.coordinate_func import *
from hcc.data_process.partite_converter import *
from hcc.data_process.difference_func import *
import pandas as pd
__author__ = 'Memray'




if __name__=='__main__':
    '''
     read data by pandas, 1318 records in total
    '''
    data_path = '../../data/LungCombinedDataSIS.csv'
    data_frame = pd.read_csv(data_path)

    '''
    strip the column names as they contain annoying space
    '''
    data_frame.columns = [name.strip() for name in data_frame.columns.values]

    '''
    The raw data totally 1587 attributes, but only 38 are of interest
    '''
    col_names = ["ID","HOSPITAL","PROCEDURE_CODE","DIAGNOSIS_CODE","FINANCIAL_CLASS_DESCRIPTION","DRG_CODE","SEVERITY_OF_ILLNESS","Smoking","AGE_ON_CONTACT_DATE","FEM","BMI","BP_SYSTOLIC","DIAB","COPD_DX","GLUCOSE","POTASSIUM(K)","SODIUM(NA)","TOTAL_PROTEIN",'PROTHROMBIN_TIME',"ACTIVATED_PTT","ASPARTATE_AMINOT.(AST)","TOTAL_BILIRUBIN","ALBUMIN","ALKALINE_PHOSPHATASE","UREA_NITROGEN","CALCIUM(CA)","HGB","HEMATOCRIT(HCT)","RBC","MCH","MCV","MCHC","RDW","CREATININE","PLATELETS","WBC","ABS_NEUTROPHILS","ABS_LYMPHOCYTES","ABS_MONOCYTES","CARBON_DIOXIDE(CO2)"]
    data_frame = data_frame.ix[: , col_names]

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

    # for col in data_frame:
    #     print(col+':'+str(len(data_frame[col].unique())))
    #     print(data_frame[col].unique())
    #     pass

    for d in data_frame.iterrows():
        partite_data.append(convert_into_PartiteGraph(d[1]))

    '''
    compute the difference against HL7 and HL74
    landmark_dict{7}: HL7
    landmark_dict{74}: HL74
    '''
    difference_list = []
    landmark_dict = load_landmarks()
    for data in partite_data:
        difference = {}
        edges = convert_to_edges(data)
        for landmark_number, landmark_list in landmark_dict.items():
            intersection = [edge for edge in edges if edge in landmark_list]
            difference[landmark_number] = len(intersection) - 39
        difference_list.append(difference)
        # print(edges)
        # print(landmark_list)
        # print('{0}:{1}'.format(len(difference_list),difference))
    '''
    calculate coordinate in terms of given two landmarks
    '''
    coordinate_list = []
    mask_dict = load_masks()
    for i in range(len(partite_data)):
        data = partite_data[i]
        difference = difference_list[i]
        matrix = convert_to_matrix(data)
        # coordinate = compute_coordinates_for_G1_G2_G3(matrix, difference, mask_dict)
        # coordinate = compute_coordinates_for_G1(matrix, difference, mask_dict)
        # coordinate = compute_coordinates_for_G2(matrix, difference, mask_dict)
        coordinate = compute_coordinates_for_G3(matrix, difference, mask_dict)
        print(coordinate)
        pass
        # compute_coordinates_for_G1()
        # compute_coordinates_for_G2()
        # compute_coordinates_for_G3()

