# INSTITUTO FEDERAL DE CIÊNCIA E TECNOLOGIA DO CEARÁ - CAMPUS FORTALEZA
# PDI - PPGCC 2022.2 (OUVINTE) - Prof. Dr. Pedro Pedrosa Rebouças Filho
# Trabalho 1 - Operações Básicas
# Hector Leonardo Mota Moreira


# Q6 - Sobel Filter

# Imports ===========================================================================================

import cv2

from enhancement_filters import sobelFilter

# Image loading =====================================================================================

image_content = 'lavotanovo'

img_path = '_image sample/lavotanovo.jpg'

img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)

# Filtering =========================================================================================

sobel_h, sobel_v, sobel_image = sobelFilter(img)

# Image displaying ==================================================================================

cv2.imshow('h sobel',sobel_h)
cv2.imshow('v sobel', sobel_v)
cv2.imshow('sobel image', sobel_image)

cv2.waitKey(0)
cv2.destroyAllWindows()

# Image saving ======================================================================================

cv2.imwrite(
    './enhancement_filetrs/results_sobel_filtering/{}_horizontal_sobel.png'.format(image_content), sobel_h)
cv2.imwrite(
    './enhancement_filetrs/results_sobel_filtering/{}_vertical_sobel.png'.format(image_content), sobel_v)
cv2.imwrite(
    './enhancement_filetrs/results_sobel_filtering/{}_sobel_image.png'.format(image_content), sobel_image)