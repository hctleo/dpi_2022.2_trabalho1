# INSTITUTO FEDERAL DE CIÊNCIA E TECNOLOGIA DO CEARÁ - CAMPUS FORTALEZA
# PDI - PPGCC 2022.2 (OUVINTE) - Prof. Dr. Pedro Pedrosa Rebouças Filho
# Trabalho 1 - Operações Básicas
# Hector Leonardo Mota Moreira


# Q7 - Histogram

# Imports ===========================================================================================

import cv2

from histogram import histogramCalc


# Image loading =====================================================================================

image_content = 'cameraman'

img_path = '/home/hector/Desktop/cameraman.jpeg'

img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)


# Histogram =========================================================================================

histogram = histogramCalc(image_content, img)


# Image displaying ==================================================================================

histogram_image = cv2.imread(histogram)

resized_histogram = cv2.resize(
    histogram_image, 
    (int (histogram_image.shape[0]*0.6), int(histogram_image.shape[1] * 0.3)), 
    interpolation = cv2.INTER_AREA)

cv2.imshow('unput image', img)
cv2.imshow('{} hisrogram'.format(image_content), resized_histogram)

cv2.waitKey(0)
cv2.destroyAllWindows()
