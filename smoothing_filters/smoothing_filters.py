# INSTITUTO FEDERAL DE CIÊNCIA E TECNOLOGIA DO CEARÁ - CAMPUS FORTALEZA
# PDI - PPGCC 2022.2 (OUVINTE) - Prof. Dr. Pedro Pedrosa Rebouças Filho
# Trabalho 1 - Operações Básicas
# Hector Leonardo Mota Moreira

# Low pass filters functions

# IMPORTS ===========================================================================================

import numpy as np
import math as m

# MEAN FILTER =======================================================================================

def meanFilter(image_content, img, k, n, padding):
       

    filtering_parameters_list = []
    
    filtering_parameters_list.append(image_content)
    filtering_parameters_list.append(k)
    filtering_parameters_list.append(n)
    filtering_parameters_list.append(padding)

    kernel = (1/k**2)*np.ones((k, k))

    c = int(k/2) # Just do simplify; k is the kernel dimension (k x k)
 

    if padding == 1:

        line, column = (img.shape)

        holdpdd = np.zeros(((line + 2 * c), (column + 2 * c))).astype(np.uint8)  

        new_line, new_column = (holdpdd.shape)

        # Based on the Professor Navar's lecture.

        holdpdd[c: new_line - c, c: new_column - c] = img
        
        mean_image = holdpdd.copy()
       
        #print('Padded image dimensions:', holdpdd.shape)


        # Convolution

        for i in range(n): 
            for x in range(c,mean_image.shape[0]-c):
                for y in range(c,mean_image.shape[1]-c):
            
                    lol = mean_image[ x - c : x + c + 1 , y - c : y + c + 1 ]
                    
                    mean = (lol * kernel).sum()
                    
                    mean_image [x,y] = round(mean)

        # To remove the padding

        final_image = np.zeros((img.shape[0] , img.shape[1]))

        final_image = mean_image[ c : new_line - c , c : new_column - c ] 


    # If padding is not wanted

    else:

        mean_image = img.copy()

        for i in range(n): 
            for x in range(c,mean_image.shape[0]-c):
                for y in range(c,mean_image.shape[1]-c):
            
                    lol = mean_image[ x - c : x + c + 1 , y - c : y + c + 1 ]
                    
                    mean = (lol * kernel).sum()
                                            
                    mean_image [x,y] = round(mean)
        
        final_image = np.zeros((img.shape[0] , img.shape[1]))
        final_image = mean_image

    
    
    return final_image, filtering_parameters_list


# MEDIAN FILTER =====================================================================================

def medianFilter(image_content, img, k, n, padding):

    filtering_parameters_list = []
    
    filtering_parameters_list.append(image_content)
    filtering_parameters_list.append(k)
    filtering_parameters_list.append(n)
    filtering_parameters_list.append(padding)

    kernel = np.ones((k, k))

    c = int(k/2) # Just do simplify; k is the kernel dimension (k x k)
 

    if padding == 1:

        line, column = (img.shape)

        holdpdd = np.zeros(((line + 2 * c), (column + 2 * c))).astype(np.uint8)  

        new_line, new_column = (holdpdd.shape)

        # Based on the Professor Navar's lecture.

        holdpdd[c: new_line - c, c: new_column - c] = img
        
        median_image = holdpdd.copy()
       
        #print('Padded image dimensions:', holdpdd.shape)


        # Convolution

        for i in range(n): 
            for x in range(c,median_image.shape[0]-c):
                for y in range(c,median_image.shape[1]-c):
            
                    lol = median_image[ x - c : x + c + 1 , y - c : y + c + 1 ]
                    
                    median = np.median(lol * kernel)
                    
                    median_image[x,y] = m.ceil(median)

        # To remove the padding

        final_image = np.zeros((img.shape[0] , img.shape[1]))

        final_image = median_image[ c : new_line - c , c : new_column - c ] 


    # If padding is not wanted

    else:

        median_image = img.copy()

        for i in range(n): 
            for x in range(c,median_image.shape[0]-c):
                for y in range(c,median_image.shape[1]-c):
            
                    lol = median_image[ x - c : x + c + 1 , y - c : y + c + 1 ]
                    
                    median = lol * kernel

                    median_list = []

                    #Alternative to the np.median() method

                    for h in range(median.shape[0]):
                        for j in range(median.shape[1]):

                            median_list.append(median[h][j]) # Could have used numpy reshape
                            
                            sorted_list = sorted(median_list)


                    median_pixel_value = sorted_list[m.floor(len(median_list)/2)]

                    median_image [x,y] = round(median_pixel_value)
        

        final_image = np.zeros((img.shape[0] , img.shape[1]))
        final_image = median_image
   
    
    return final_image, filtering_parameters_list


# GAUSSIAN FILTER ===================================================================================

# To generate the gaussian kernel. Based on the Professor Navar's code and Gonzalez and Woods (2008)

def gaussianKernel(d1, d2):
  
  x, y = np.mgrid[0:d2, 0:d1]
  x = x-d2/2
  y = y-d1/2
  sigma = 4 # std deviation
  a = np.exp( -(x**2 + y**2) / (2 * sigma**2) )
  return a / a.sum()


def gaussianFilter(image_content, img, k, n, padding):

    filtering_parameters_list = []
    
    filtering_parameters_list.append(image_content)
    filtering_parameters_list.append(k)
    filtering_parameters_list.append(n)
    filtering_parameters_list.append(padding)

    gaussian_kernel = gaussianKernel(k, k)

    c = int(k/2) # Just do simplify; k is the kernel dimension (k x k)

    # With Padding

    if padding == 1:

        line, column = (img.shape) 

        holdpdd = np.zeros( ((line + 2 * c), (column + 2 * c)) ).astype(np.uint8)   

        new_line, new_column = (holdpdd.shape)

        holdpdd [ c : new_line - c , c : new_column - c ] = img # Based on the Professor Navar's lecture.

        gaussian_image = holdpdd.copy()
            
        print(holdpdd.shape)

        # Convolution

        for i in range(n): 
            for x in range(c,gaussian_image.shape[0]-c):
                for y in range(c,gaussian_image.shape[1]-c):
                    
                    lol = gaussian_image[ x - c : x + c + 1 , y - c : y + c + 1 ]
                    
                    gaussian_conv = (lol * gaussian_kernel).sum()
                    
                    gaussian_image [x,y] = round(gaussian_conv)

        # To remove the padding

        final_image = np.zeros((img.shape[0] , img.shape[1]))

        final_image = gaussian_image[ c : new_line - c , c : new_column - c ] 


    # Without padding

    else:
 
        gaussian_image = img.copy()

        for i in range(n): 
            for x in range(c,gaussian_image.shape[0]-c):
                for y in range(c,gaussian_image.shape[1]-c):
                
                    lol = gaussian_image[ x - c : x + c + 1 , y - c : y + c + 1 ]
                    
                    gaussian_conv = (lol * gaussian_kernel).sum()
                        
                    gaussian_image [x,y] = round(gaussian_conv)
        
        final_image = np.zeros((img.shape[0] , img.shape[1]))
        final_image = gaussian_image

    return final_image, filtering_parameters_list