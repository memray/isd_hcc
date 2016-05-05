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
    os.chdir('../../')

    data_path = 'data/LungCombinedDataSIS.csv'
    data_frame = pd.read_csv(data_path)

    '''
    strip the column names as they contain annoying space
    '''
    data_frame.columns = [name.strip() for name in data_frame.columns.values]

    '''
    The raw data totally 1587 attributes, but only 38 are of interest
    '''
    col_names = ["ID","HOSPITAL","PROCEDURE_CODE","DIAGNOSIS_CODE","FINANCIAL_CLASS_DESCRIPTION","DRG_CODE","SEVERITY_OF_ILLNESS","SMOKING","AGE_ON_CONTACT_DATE","FEM","BMI","BP_SYSTOLIC","DIAB","COPD_DX","GLUCOSE","POTASSIUM(K)","SODIUM(NA)","TOTAL_PROTEIN",'PROTHROMBIN_TIME',"ACTIVATED_PTT","ASPARTATE_AMINOT.(AST)","TOTAL_BILIRUBIN","ALBUMIN","ALKALINE_PHOSPHATASE","UREA_NITROGEN","CALCIUM(CA)","HGB","HEMATOCRIT(HCT)","RBC","MCH","MCV","MCHC","RDW","CREATININE","PLATELETS","WBC","ABS_NEUTROPHILS","ABS_LYMPHOCYTES","ABS_MONOCYTES","CARBON_DIOXIDE(CO2)"]
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
    # write coordinates to file as cache, avoid of generating all the time
    csv_file = open('data/output/coordinates.csv','w')
    csv_file_g1 = open('data/output/coordinates_g1.csv','w')
    csv_file_g2 = open('data/output/coordinates_g2.csv','w')
    csv_file_g3 = open('data/output/coordinates_g3.csv','w')

    coordinate_list = []
    mask_dict = load_masks()

    count_dict = {}
    count_dict['G1']=0
    count_dict['G2']=0
    count_dict['G3']=0

    # compute coordinates for overview
    for i in range(len(partite_data)):
        # the first 451 patients are dead
        if i<451:
            real_group_name = 'Patients who died'
            real_group_number = 'G1'
        else:
            real_group_name = 'Patients alive'
            real_group_number = 'G2'
        data = partite_data[i]
        difference = difference_list[i]
        matrix = convert_to_matrix(data)
        coordinate = compute_coordinates_for_G1_G2_G3(matrix, difference, mask_dict)
        group = classify_group_for_G1_G2_G3(coordinate)
        count_dict[group]+=1
        print('{0}:{1}'.format(coordinate,group))

        csv_file.write('{0},{1},{2},{3}\n'.format(coordinate[0], coordinate[1], real_group_name, real_group_number))
        if group=='G1':
            coordinate = compute_coordinates_for_G1(matrix, difference, mask_dict)
            csv_file_g1.write('{0},{1},{2},{3}\n'.format(coordinate[0], coordinate[1], real_group_name, real_group_number))
        if group=='G2':
            coordinate = compute_coordinates_for_G2(matrix, difference, mask_dict)
            csv_file_g2.write('{0},{1},{2},{3}\n'.format(coordinate[0], coordinate[1], real_group_name, real_group_number))
        if group=='G3':
            coordinate = compute_coordinates_for_G3(matrix, difference, mask_dict)
            csv_file_g3.write('{0},{1},{2},{3}\n'.format(coordinate[0], coordinate[1], real_group_name, real_group_number))

    print(count_dict)
    csv_file_g1.close()
    csv_file_g2.close()
    csv_file_g3.close()

