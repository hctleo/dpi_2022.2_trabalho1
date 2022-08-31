# INSTITUTO FEDERAL DE CIÊNCIA E TECNOLOGIA DO CEARÁ - CAMPUS FORTALEZA
# PDI - PPGCC 2022.2 (OUVINTE) - Prof. Dr. Pedro Pedrosa Rebouças Filho
# Trabalho 1 - Operações Básicas
# Hector Leonardo Mota Moreira


# Q1 - Mean Filter

# Imports ===========================================================================================

import cv2

import numpy as np

from smoothing_filters import meanFilter

# Image loading =====================================================================================

img = cv2.imread('_image sample/chaplin.png', cv2.IMREAD_GRAYSCALE)

image_content = 'chaplin'

# Filtering and Saving ==============================================================================

kernel_size_list = [3]

number_of_iterations_list = [1, 5]

for k in kernel_size_list:
    for n in number_of_iterations_list:

        filtered_image, filtering_parameters = meanFilter(image_content, img, k, n, 1)

        print('filtering parameters:', filtering_parameters)

        # image saving

        file_name = './smoothing_filters/results_mean_filtering/{}_k{}n{}pdd{}_mean_filter.png'
        
        saved_image = cv2.imwrite(file_name.format(  
            filtering_parameters[0],  # image content
            filtering_parameters[1],  # kernel dimensions
            filtering_parameters[2],  # number of iterations
            filtering_parameters[3]), # padding
            filtered_image)
        
        print(saved_image)