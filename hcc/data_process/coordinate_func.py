# encoding: utf-8
__author__ = 'Memray'
import numpy as np

def load_masks():
    '''
    Reading matrices from file, ranging from 0 to 389
    '''
    mask = {}
    mask['G123'] = np.loadtxt('data/Subgroup123Mask.txt')
    mask['G1'] = np.loadtxt('data/G1Mask.txt')
    mask['G2'] = np.loadtxt('data/G2Mask.txt')
    mask['G3'] = np.loadtxt('data/G3Mask.txt')
    return mask

def convert_to_matrix(data):
    matrix = np.zeros((390,390))
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
        matrix[from_code-1, to_code-1] = 1
    # print(edges)
    return matrix

nopart = 39
def compute_coordinates_for_G1_G2_G3(matrix, distances, masks):
    '''
    return a tuple (x,y), denote the coordinate
    '''
    mask = masks['G123']
    pomp = 0.0
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if mask[i,j] > 0:
                pomp += matrix[i,j]*mask[i,j]
    x = 6 * pomp +((nopart + distances[7] + 1) / 6.0)

    pomp = 0.0
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if mask[i, j] < 0:
                pomp += matrix[i, j] * mask[i, j]
    y = -6 * pomp + ((nopart + distances[74] + 1) / 6.0)

    return (x,y)

def classify_group_for_G1_G2_G3(CoorPT):
    # Definition of patients in G1

    if CoorPT[1] < 2:
        return 'G1'
    # Definition of patients in G2
    elif (CoorPT[1] >= 2 and CoorPT[0] < 3):
        return 'G2'
    # Definition of patients in G3
    elif (CoorPT[1] >= 2 and CoorPT[0] >= 3):
        return 'G3'

def compute_coordinates_for_G1(matrix, distances, masks):
    mask = masks['G1']

    pomp = 0.0
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if mask[i, j] > 0:
                pomp += matrix[i, j] * mask[i, j]
    x = 3 * pomp + (2 * (nopart + distances[58] + 1) / 6.0) + ((nopart + distances[47] + 1) / 6.0)

    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if mask[i, j] < 0:
                pomp += matrix[i, j] * mask[i, j]
    y = -6 * pomp+((nopart+distances[3]+1)/6.0)+((nopart+distances[4]+1)/6.0)+((nopart+distances[6]+1)/6.0)

    return (x, y)

def compute_coordinates_for_G2(matrix, distances, masks):
    mask = masks['G2']

    pomp = 0.0
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if mask[i, j] > 0:
                pomp += matrix[i, j] * mask[i, j]
    x = 3*pomp+(2*(nopart+distances[71]+1)/6.0)+((nopart+distances[59]+1)/6.0)

    pomp = 0.0
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if mask[i, j] < 0:
                pomp += matrix[i, j] * mask[i, j]
    y = -6*pomp+((nopart+distances[16]+1)/6.0)+((nopart+distances[14]+1)/6.0)+((nopart+distances[1]+1)/6.0)

    return (x, y)

def compute_coordinates_for_G3(matrix, distances, masks):
    mask = masks['G3']

    pomp = 0.0
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if mask[i, j] > 0:
                pomp += matrix[i, j] * mask[i, j]
    x = 3*pomp+(2*(nopart+distances[71]+1)/6.0)+((nopart+distances[48]+1)/6.0)

    pomp = 0.0
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if mask[i, j] < 0:
                pomp += matrix[i, j] * mask[i, j]
    y = -6*pomp+((nopart+distances[3]+1)/6.0)+((nopart+distances[16]+1)/6.0)+((nopart+distances[1]+1)/6.0)

    return (x, y)
