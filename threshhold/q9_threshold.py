# INSTITUTO FEDERAL DE CIÊNCIA E TECNOLOGIA DO CEARÁ - CAMPUS FORTALEZA
# PDI - PPGCC 2022.2 (OUVINTE) - Prof. Dr. Pedro Pedrosa Rebouças Filho
# Trabalho 1 - Operações Básicas
# Hector Leonardo Mota Moreira


# Q9 - Thresholding

# Imports ===========================================================================================

import cv2

from threshold import threshold


# Image loading =====================================================================================

image_content = 'house'

img_path = '/home/hector/Desktop/house.jpg'

img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)


# Thresholding ======================================================================================

th_image, th_value = threshold(img, 120)


# Image displaying ==================================================================================

cv2.imshow('th image', th_image)

cv2.waitKey(0)

cv2.destroyAllWindows()


# Image saving ======================================================================================

cv2.imwrite('threshhold/results_th/{}_th{}_threshold.png'.format(image_content, th_value), th_image)