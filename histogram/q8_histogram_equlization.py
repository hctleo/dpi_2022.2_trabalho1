# INSTITUTO FEDERAL DE CIÊNCIA E TECNOLOGIA DO CEARÁ - CAMPUS FORTALEZA
# PDI - PPGCC 2022.2 (OUVINTE) - Prof. Dr. Pedro Pedrosa Rebouças Filho
# Trabalho 1 - Operações Básicas
# Hector Leonardo Mota Moreira


# Q8 - Histogram Equalization

# Imports ===========================================================================================

import cv2

from histogram import histogramEqualization


# Image loading =====================================================================================

image_content = 'cameraman'

img_path = 'image sample/cameraman.jpeg'

img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)


# Histogram =========================================================================================

hist, eq_hist, eq_image = histogramEqualization(image_content, img)


# Image displaying ==================================================================================

histogram_image = cv2.imread(hist)
eq_histogram_image = cv2.imread(eq_hist)

resized_histogram = cv2.resize(
    histogram_image, 
    (int (histogram_image.shape[0]*0.6), int(histogram_image.shape[1] * 0.3)), 
    interpolation = cv2.INTER_AREA)

resized_eq_histogram = cv2.resize(
    eq_histogram_image, 
    (int (eq_histogram_image.shape[0]*0.6), int(eq_histogram_image.shape[1] * 0.3)), 
    interpolation = cv2.INTER_AREA)


cv2.imshow('equalized image', eq_image)
cv2.imshow('unput image', img)
cv2.imshow('{} hisrogram'.format(image_content), resized_histogram)
cv2.imshow('{} hisrogram'.format(image_content), resized_eq_histogram)

cv2.waitKey(0)
cv2.destroyAllWindows()

# Image saving ======================================================================================

cv2.imwrite(
    'histogram/results_histogram_equalization/equalized_histogram_images/{}_equalized_histogram.png'.
    format(image_content),
    eq_image)

    