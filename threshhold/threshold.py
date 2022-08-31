# INSTITUTO FEDERAL DE CIÊNCIA E TECNOLOGIA DO CEARÁ - CAMPUS FORTALEZA
# PDI - PPGCC 2022.2 (OUVINTE) - Prof. Dr. Pedro Pedrosa Rebouças Filho
# Trabalho 1 - Operações Básicas
# Hector Leonardo Mota Moreira

# Threshold functions

# IMPORTS ===========================================================================================

import numpy as np

# THRESHOLD =========================================================================================

def threshold(img, th):

    global_th_image = img.copy()

    print (img.shape)

    for i in range (0 , img.shape[0]):
        for j in range (0, img.shape[1]):

            if global_th_image[(i,j)] > th :

                global_th_image[(i,j)] = 255

            else:
                global_th_image[(i,j)] = 0


    return global_th_image.astype(np.uint8), th


# MULTIPLE THRESHOLD ==================================================================================

def multiThreshold(img, th1, th2):

    multi_th_image = img.copy()

    for rep in range (1):
        for i in range (0 , img.shape[0]):
            for j in range (0, img.shape[1]):

                if multi_th_image[(i,j)] > th2 :

                    multi_th_image[(i,j)] = 255
                    
                elif th1 < multi_th_image[(i,j)] <= th2:
                    multi_th_image[(i,j)] = 127
                    
                else:
                    multi_th_image[(i,j)] = 0


    return multi_th_image.astype(np.uint8), th1, th2
