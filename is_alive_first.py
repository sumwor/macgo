import numpy as np
import math
import copy

def init_matrix(n, p):

    #initialize the dict with color
    color_dict = {}
    rand = np.random.rand(n, n)
    rand[rand >= 1] = 1
    rand[ - (rand >= 1)] = 0   #transform random digit into color
    list_color = list(rand)

    for up in range(n):
        for down in range(n):
            key  = (up, down)
            color_dict[key] = rand[up][down]
    return color_dict

#print out the color matrix properly for testing
def print_matrix(dictionary):
    dim = int(math.sqrt(len(dictionary)))
    matrix = list(np.zeros(dim, dim))
    for key in dictionary.keys():
        matrix[key[0]][key[1]] = dictionary[key]
    for x in range(len(matrix)):
        print matrix[x]

def caculate_list(whole):
    iteration_list = [up for up in whole.keys() if whole[up] == 1]
    if len(iteration_list) == 0:
        return 0
    else:
        area_list = []
        i = 0
        records = []
        for t in iteration_list:
            if t not in records:
                su, area,records_aloop = calculate_a_area(whole, list((t,)))
                area_list.append(su)
                i += 1
                records += records_aloop
        return area_list

def calculate_a_area(whole, area):
    up, down, right, left = (1, 1, 1, 1)
    su = 1
    area_records = copy.deepcopy(area)
    while up | down | right | left | (area != []):
        for coo in area:
            up = (int(coo[0] - 1)) % math.sqrt(len(whole)),coo[1])) not in area_records and whole[(int((coo[0] - 1) % math.sqrt(len(whole))), coo[1])] == 1

            if up:
