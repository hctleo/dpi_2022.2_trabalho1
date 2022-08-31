# INSTITUTO FEDERAL DE CIÊNCIA E TECNOLOGIA DO CEARÁ - CAMPUS FORTALEZA
# PDI - PPGCC 2022.2 (OUVINTE) - Prof. Dr. Pedro Pedrosa Rebouças Filho
# Trabalho 1 - Operações Básicas
# Hector Leonardo Mota Moreira


# Q4 - Laplacian Filter

# Imports ===========================================================================================

from pickletools import uint8
import cv2

from enhancement_filters import laplacianFilter


# Image loading =====================================================================================

image_content = 'dragonball'

img_path = '_image sample/dragonball.png'

img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)


# Filtering =========================================================================================

kernel_type_list = [0, 1, 2, 3]

number_of_iterations_list = [1]

for k_type in kernel_type_list:
    for n in number_of_iterations_list:

        filtered_image, filtering_parameters = laplacianFilter(image_content, img, k_type, n, 1)

        print('filtering parameters:', filtering_parameters)

        # image saving

        file_name = './enhancement_filetrs/results_laplacian_filtering/{}_ktype{}n{}pdd{}_laplacian_filter.png'
        
        saved_image = cv2.imwrite(file_name.format(  
            filtering_parameters[0],  # image content
            filtering_parameters[1],  # kernel type
            filtering_parameters[2],  # number of iterations
            filtering_parameters[3]), # padding
            filtered_image)
        
        print(saved_image)


print(filtered_image.min(), filtered_image.max())

cv2.imshow('laplacian', filtered_image)

cv2.waitKey(0)

print(filtered_image)
        