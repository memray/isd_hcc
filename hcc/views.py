#coding: utf-8
from django.shortcuts import render
from django.http import JsonResponse
from json import *
from hcc.data_process.coordinate_func import *
from hcc.data_process.partite_converter import *
from hcc.data_process.difference_func import *

# def sample(request):
#     request.encoding='utf-8'
#     if 'q' in request.GET:
#         message = '你搜索的内容为: ' + request.GET['q'].encode('utf-8')
#     else:
#         message = '你提交了空表单'
#     return render(request, 'index.html', {'message': message})


from django.http import HttpResponse

def index(request):
    # return HttpResponse(u"Hello world!")
    string = u'Welcome to Jungle!'
    return render(request, 'index.html', {'string': string})

def load_cache(file_path):
    cache = open(file_path,'r')
    record_list = []
    for line in cache:
        tokens = line.split(',')
        record = {}
        record['time']=tokens[0].strip()
        record['intensity']=tokens[1].strip()
        record['group_name']=tokens[2].strip()
        record['group']=tokens[3].strip()
        record['radius']=3.5
        record_list.append(record)
    return record_list


from django.views.decorators.csrf import csrf_exempt
import os

def create_patient_node(coordinate):
    record = {}
    record['time'] = coordinate[0]
    record['intensity'] = coordinate[1]
    record['group_name'] = 'This patient'
    record['group'] = 'G3'
    record['radius'] = 100
    return record


landmark_dict = load_landmarks()
mask_dict = load_masks()
@csrf_exempt
def get_all(request):
    record_list = load_cache('data/output/coordinates.csv')

    form_json = request.body.decode('utf-8')
    form_list = loads(form_json)
    raw_data = {}
    for field in form_list:
        raw_data[field['name'].upper()] = field['value']
    partite_data = convert_into_PartiteGraph(raw_data)

    difference = {}
    edges = convert_to_edges(partite_data)
    for landmark_number, landmark_list in landmark_dict.items():
        intersection = [edge for edge in edges if edge in landmark_list]
        difference[landmark_number] = len(intersection) - 39

    matrix = convert_to_matrix(partite_data)
    coordinate = compute_coordinates_for_G1_G2_G3(matrix, difference, mask_dict)

    record = create_patient_node(coordinate)
    record_list.append(record)

    return JsonResponse(JSONEncoder().encode(record_list), safe=False)

@csrf_exempt
def get_group1(request):
    record_list = load_cache('data/output/coordinates_g1.csv')

    form_json = request.body.decode('utf-8')
    form_list = loads(form_json)
    raw_data = {}
    for field in form_list:
        raw_data[field['name'].upper()] = field['value']
    partite_data = convert_into_PartiteGraph(raw_data)

    difference = {}
    edges = convert_to_edges(partite_data)
    for landmark_number, landmark_list in landmark_dict.items():
        intersection = [edge for edge in edges if edge in landmark_list]
        difference[landmark_number] = len(intersection) - 39

    matrix = convert_to_matrix(partite_data)
    coordinate = compute_coordinates_for_G1_G2_G3(matrix, difference, mask_dict)

    group = classify_group_for_G1_G2_G3(coordinate)

    if (group=='G1'):
        coordinate = compute_coordinates_for_G1(matrix, difference, mask_dict)
        record = create_patient_node(coordinate)
        record_list.append(record)

    return JsonResponse(JSONEncoder().encode(record_list), safe=False)

@csrf_exempt
def get_group2(request):
    record_list = load_cache('data/output/coordinates_g2.csv')

    form_json = request.body.decode('utf-8')
    form_list = loads(form_json)
    raw_data = {}
    for field in form_list:
        raw_data[field['name'].upper()] = field['value']
    partite_data = convert_into_PartiteGraph(raw_data)

    difference = {}
    edges = convert_to_edges(partite_data)
    for landmark_number, landmark_list in landmark_dict.items():
        intersection = [edge for edge in edges if edge in landmark_list]
        difference[landmark_number] = len(intersection) - 39

    matrix = convert_to_matrix(partite_data)
    coordinate = compute_coordinates_for_G1_G2_G3(matrix, difference, mask_dict)

    group = classify_group_for_G1_G2_G3(coordinate)

    if (group=='G2'):
        coordinate = compute_coordinates_for_G2(matrix, difference, mask_dict)
        record = create_patient_node(coordinate)
        record_list.append(record)

    return JsonResponse(JSONEncoder().encode(record_list), safe=False)

@csrf_exempt
def get_group3(request):
    record_list = load_cache('data/output/coordinates_g3.csv')

    form_json = request.body.decode('utf-8')
    form_list = loads(form_json)
    raw_data = {}
    for field in form_list:
        raw_data[field['name'].upper()] = field['value']
    partite_data = convert_into_PartiteGraph(raw_data)

    difference = {}
    edges = convert_to_edges(partite_data)
    for landmark_number, landmark_list in landmark_dict.items():
        intersection = [edge for edge in edges if edge in landmark_list]
        difference[landmark_number] = len(intersection) - 39

    matrix = convert_to_matrix(partite_data)
    coordinate = compute_coordinates_for_G1_G2_G3(matrix, difference, mask_dict)

    group = classify_group_for_G1_G2_G3(coordinate)

    if (group=='G3'):
        coordinate = compute_coordinates_for_G3(matrix, difference, mask_dict)
        record = create_patient_node(coordinate)
        record_list.append(record)

    return JsonResponse(JSONEncoder().encode(record_list), safe=False)