# encoding: utf-8
import os
__author__ = 'Memray'

def load_landmarks():
    print('Reading landmarks: HL7 & HL74')

    file_path_list = []

    file_dir = '../../data/HL_ForG1G3_Classification/'
    for file_name in os.listdir(file_dir):
        file_path_list.append(file_dir+file_name)
    file_dir = '../../data/HLForG1_D_A_Odds/'
    for file_name in os.listdir(file_dir):
        file_path_list.append(file_dir + file_name)
    file_dir = '../../data/HLForG2_D_A_Odds/'
    for file_name in os.listdir(file_dir):
        file_path_list.append(file_dir + file_name)
    file_dir = '../../data/HLForG3_D_A_Odds/'
    for file_name in os.listdir(file_dir):
        file_path_list.append(file_dir + file_name)

    landmarks = {}

    for file_path in file_path_list:
        file_number = int(file_path[file_path.rindex('HL')+2:-4])
        # print(file_path)
        # print(file_number)
        landmarks[file_number] = []

        file = open(file_path, 'r')

        find_edges = False
        for line in file:
            if line.strip() == '*Edges':
                find_edges = True
                continue
            if not find_edges:
                continue
            from_node = int(line.split(' ')[0].strip())
            to_node = int(line.split(' ')[1].strip())
            landmarks[file_number].append((from_node, to_node))
            # print(line)
    print('Landmarks reading complete')
    return landmarks


def convert_to_edges(data):
    '''
    Convert the value array (length = 390) to the edges
    for example, data[3]=1, data[14]=1, then add a tuple = (3,14)
    '''
    edges = []
    tens = []
    for i in range(39):
        tens.append(i)
    tens.append(0)
    # print(tens)
    for i in range(len(tens)-1):
        # print(tens[i] * 10)
        # print(tens[i+1] * 10)
        from_code = 0
        to_code = 0
        for j in range(1,11):
            # print( tens[i] * 10 + j)
            # print( tens[i+1] * 10 + j)
            if int(data[tens[i] * 10 + j])==1:
                from_code=tens[i] * 10 + j
            if int(data[tens[i+1] * 10 + j]) == 1:
                to_code = tens[i+1] * 10 + j
        edges.append((from_code, to_code))
    # print(edges)
    return edges