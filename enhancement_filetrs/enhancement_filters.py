# INSTITUTO FEDERAL DE CIÊNCIA E TECNOLOGIA DO CEARÁ - CAMPUS FORTALEZA
# PDI - PPGCC 2022.2 (OUVINTE) - Prof. Dr. Pedro Pedrosa Rebouças Filho
# Trabalho 1 - Operações Básicas
# Hector Leonardo Mota Moreira

# High pass filters functions

# IMPORTS ===========================================================================================

from pickletools import uint8
import numpy as np
import math as m

# IMAGE NORMALIZATION ===============================================================================

def normalizeImage(v):

  v = (v - v.min()) / (v.max() - v.min())

  result = (v * 255).astype(np.uint8)

  #cv2_imshow(result)

  return result

# LAPLACIAN FILTER ==================================================================================

def laplacianFilter(image_content, img, kernel_type, n, padding):

    c = 1

    filtering_parameters_list = []
    
    filtering_parameters_list.append(image_content)
    filtering_parameters_list.append(kernel_type)
    filtering_parameters_list.append(n)
    filtering_parameters_list.append(padding)

    if kernel_type == 0:

        kernel_laplacian = np.array([[0, 1, 0], [1, -4, 1],[0, 1, 0]])
        

    elif kernel_type == 1:
        kernel_laplacian = np.array([[1, 1, 1], [1, -8, 1],[1, 1, 1]])
        

    elif kernel_type == 2:
        kernel_laplacian = np.array([[0, -1, 0], [-1, 4, -1],[0, -1, 0]])
         

    else:
        kernel_laplacian =  np.array([[-1, -1, -1], [-1, 8, -1],[-1, -1, -1]])
        

    # Padding
    if padding == 1:
        line, column = (img.shape) 

        holdpdd = np.zeros(((line + 2 * c), (column + 2 * c))) 

        new_line, new_column = (holdpdd.shape)

        holdpdd [ c : new_line - c , c : new_column - c ] = img
    
    else:

        line, column = (img.shape)

        holdpdd = img.copy()

        new_line, new_column = (holdpdd.shape)


    # Convolution

    laplacian_image = holdpdd.copy() # Based on the Professor Navar's code.

    for i in range(n):
        for x in range (c,holdpdd.shape[0]-c):
            for y in range(c,holdpdd.shape[1]-c):
                
                lol = holdpdd[ x - c : x + c + 1 , y - c : y + c + 1 ]
                    
                laplacian_conv = (lol * kernel_laplacian).sum()
                
                laplacian_image[x,y] = round(laplacian_conv)
                

    # Removing padding and image saving

    final_image = np.zeros((line,column))

    final_image = laplacian_image [ c : new_line - c , c : new_column - c ]

    print('img shape:', final_image.shape, ';', 'laplacian image shape:', laplacian_image.shape)

    
    # range [0,255]

    for i in range (0, final_image.shape[0]):
        for j in range (0, final_image.shape[1]):

            if final_image[(i,j)] > 255:

                final_image[(i,j)] = 255

            elif final_image[(i,j)] < 0:
                final_image[(i,j)] = 0

    final_image = normalizeImage(final_image)

    return final_image, filtering_parameters_list


# PREWITT FILTER ====================================================================================

def prewittFilter(img):

    k = 3; c = 1

    horizontal_prewitt_kernel = np.ones((k,k))

    for x in range(k):
        horizontal_prewitt_kernel [(x,0)] = -1
    
    for y in range (k):
        horizontal_prewitt_kernel [(y,1)] = 0


    vertical_prewitt_kernel = np.ones((k,k))

    for i in range (k):
        vertical_prewitt_kernel [(0,i)] = -1
    for j in range (k):
        vertical_prewitt_kernel [(1,j)] = 0


    # Padding 

    line, column = img.shape

    holdpdd = np.zeros( ((line + 2 * c), (column + 2 * c)) )  

    new_line, new_column = (holdpdd.shape)

    holdpdd [ c : new_line - c , c : new_column - c ] = img # Based on the Professor Navar's lecture.


    #  Convolution  

    holdpdd_copy_horizontal = holdpdd.copy() # Based on the Professor Navar's lecture.

    holdpdd_copy_vertical = holdpdd.copy()


    # Horizontal Mask

    for x in range (c,holdpdd_copy_horizontal.shape[0]-c):
        for y in range(c,holdpdd_copy_horizontal.shape[1]-c):
            
            lol = holdpdd[ x - c:x + c + 1 , y - c: y + c + 1 ]
            
            horizontal_mask = (lol*horizontal_prewitt_kernel).sum()
            
            holdpdd_copy_horizontal[x,y] = horizontal_mask

    print('h mask:', holdpdd_copy_horizontal.min(), holdpdd_copy_horizontal.max())

    # Vertical Mask

    for x in range (c,holdpdd_copy_vertical.shape[0]-c):
        for y in range(c,holdpdd_copy_horizontal.shape[1]-c):
            
            lol = holdpdd[ x - c:x + c + 1 , y - c: y + c + 1 ]
            
            vertical_mask = (lol*vertical_prewitt_kernel).sum()
            
            holdpdd_copy_vertical[x,y] = vertical_mask

    print('v mask:', holdpdd_copy_vertical.min(), holdpdd_copy_vertical.max())

    # Normalized images

    prewitt_h_normalized = normalizeImage(holdpdd_copy_horizontal)
    prewitt_v_normalized = normalizeImage(holdpdd_copy_vertical)


    # Prewitt image adjustment

    prewitt_image = np.sqrt((holdpdd_copy_horizontal**2 + holdpdd_copy_vertical**2))

    prewitt_adjusted = normalizeImage(prewitt_image.copy())

    # To remove the padding

    final_image = np.zeros((line,column))

    final_image = prewitt_adjusted [ c : new_line - c , c : new_column - c ] 

    print(prewitt_image.shape, final_image.shape)

    return prewitt_h_normalized, prewitt_v_normalized, final_image



# SOBEL FILTER ======================================================================================

def sobelFilter(img):
    k = 3

    c = 1 # Just do simplify; k is the kernel dimension (k x k)

    horizontal_sobel_kernel = np.array(([-1,0,1],[-2,0,2],[-1,0,1]))

    vertical_sobel_kernel = np.array(([-1,-2,-1],[0,0,0],[1,2,1]))

    # Padding 

    line, column = (img.shape) 

    holdpdd = np.zeros( ((line + 2 * c), (column + 2 * c)) )  

    new_line, new_column = (holdpdd.shape)

    holdpdd [ c : new_line - c , c : new_column - c ] = img # Based on the Professor Navar's lecture.

    
    # Convolution  

    holdpdd_copy_horizontal = holdpdd.copy()  # Based on the Professor Navar's code.

    holdpdd_copy_vertical = holdpdd.copy()    # Based on the Professor Navar's code.


    # Horizontal Mask

    for x in range (c,holdpdd_copy_horizontal.shape[0]-c):
        for y in range(c,holdpdd_copy_horizontal.shape[1]-c):
            
            lol = holdpdd[ x - c:x + c + 1 , y - c: y + c + 1 ]
                
            horizontal_mask = (lol*horizontal_sobel_kernel).sum()
            
            holdpdd_copy_horizontal[x,y] = round(horizontal_mask)
        
    # Vertical Mask

    for x in range (c,holdpdd_copy_horizontal.shape[0]-c):
        for y in range(c,holdpdd_copy_horizontal.shape[1]-c):
            
            lol = holdpdd[ x - c : x + c + 1 , y - c: y + c + 1 ]
                
            vertical_mask = (lol*vertical_sobel_kernel).sum()
            
            holdpdd_copy_vertical[x,y] = round(vertical_mask)


    # Sobel image and intensity adjustment 

    sobel_image = np.sqrt((holdpdd_copy_horizontal**2 + holdpdd_copy_vertical**2)) # sobel image calc

    sobel_adjusted = sobel_image.copy()

    sobel_h_normalized = normalizeImage(holdpdd_copy_horizontal)

    sobel_v_normalized = normalizeImage(holdpdd_copy_vertical)

    final_image = normalizeImage(sobel_image)


    return sobel_h_normalized, sobel_v_normalized, final_image


