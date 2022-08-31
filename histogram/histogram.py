# INSTITUTO FEDERAL DE CIÊNCIA E TECNOLOGIA DO CEARÁ - CAMPUS FORTALEZA
# PDI - PPGCC 2022.2 (OUVINTE) - Prof. Dr. Pedro Pedrosa Rebouças Filho
# Trabalho 1 - Operações Básicas
# Hector Leonardo Mota Moreira

# Histogram functions

# IMPORTS ===========================================================================================

import numpy as np
import matplotlib.pyplot as plt 

# HISTOGRAM =========================================================================================

def histogramCalc(image_content, img):
    
    frequency_vector = np.zeros(2**8)

    for i in range(img.shape[0]):
        for j in range(img.shape[1]):

            frequency_vector[img[i][j]] = frequency_vector[img[i][j]] + 1

    intensity_values = []

    for i in range(256):
        intensity_values.append(i)


    plt.rcParams.update({'font.size': 16})

    histogram = plt.figure(figsize=(12,8))  

    plt.title('Histogram', fontsize=22, fontweight = 'bold') #, fontname='Times New Roman')
    plt.xlabel('Intensity values', fontsize=18)
    plt.ylabel('Frequency', fontsize=18)
    plt.bar(intensity_values, frequency_vector, color = '#172381')
    #plt.show()
    histogram.savefig('histogram/results_histogram/{}_histogram.png'.format(image_content), dpi = 150)

    hist_save = 'histogram/results_histogram/{}_histogram.png'.format(image_content)

    return hist_save


# HISTOGRAM EQUALIZATION ============================================================================

def histogramEqualization(image_content, img):

    # Plot image histogram
    frequency_vector = np.zeros(2**8)

    for i in range(img.shape[0]):
        for j in range(img.shape[1]):

            frequency_vector[img[i][j]] = frequency_vector[img[i][j]] + 1

    intensity_values = []

    for i in range(256):
        intensity_values.append(i)

    # Configure, plot and save histogram

    plt.rcParams.update({'font.size': 16})

    histogram = plt.figure(figsize=(12,8))  

    cdf = frequency_vector.cumsum()
    cdf_normalized = cdf * float(frequency_vector.max()) / cdf.max()


    plt.plot(cdf_normalized, color = 'r')
    plt.title('Histogram', fontsize=22, fontweight = 'bold')#, fontname='Times New Roman')
    plt.xlabel('Intensity values', fontsize=18)
    plt.ylabel('Frequency', fontsize=18)
    plt.bar(intensity_values, frequency_vector, color = '#172381')
    plt.legend(('CDF','Histogram'), loc = 'upper center')
    #plt.show()
    histogram.savefig(
        'histogram/results_histogram_equalization/{}_cdf_equalized_histogram.png'.format(image_content),
         dpi = 150)

    hist_save = 'histogram/results_histogram_equalization/{}_cdf_equalized_histogram.png'.format(image_content)


    # Histogram Equlization begins ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    # Vector to compute intensity values occurrence

    frequency_vector = np.zeros(2**8)

    # Cumulative distribution function vector

    cdf = np.zeros(2**8)

    for i in range(img.shape[0]):
        for j in range(img.shape[1]):

            frequency_vector[img[i][j]] = frequency_vector[img[i][j]] + 1

    # Intensity values list

    intensity_values = []

    for i in range(256):
        intensity_values.append(i)

    # Probability density function

    pdf = frequency_vector / (img.shape[0] * img.shape[1])

    # Cumulative distribution function vector

    for j in range(1, frequency_vector.shape[0]):

        cdf[j] = cdf[j-1] + pdf[j]

    # sk
    
    equalized_frequency = np.round(cdf*img.max()) 

    # 
    equalized_image = img.copy()

    for m in range(equalized_image.shape[0]):
        for n in range(equalized_image.shape[1]):

            equalized_image[m][n] = equalized_frequency[equalized_image[m][n]]

    # Recalculate histogram vector

    eqalized_frequency_vector = np.zeros(2**8)

    for i in range(equalized_image.shape[0]):
        for j in range(equalized_image.shape[1]):

            eqalized_frequency_vector[equalized_image[i][j]] = eqalized_frequency_vector[equalized_image[i][j]] + 1

    intensity_values = []

    for i in range(256):
        intensity_values.append(i)

    # Calculate cumulative sum using numpy

    equalized_cdf_normalized =  np.cumsum(eqalized_frequency_vector) * float(eqalized_frequency_vector.max()) / np.cumsum(eqalized_frequency_vector).max()

    plt.rcParams.update({'font.size': 16})

    equalized_histogram = plt.figure(figsize=(12,8))

    # Histogram plotting and saving   

    plt.plot(equalized_cdf_normalized, color = 'r')
    plt.title('Equalized histogram', fontsize=22, fontweight = 'bold') #, fontname = 'Times New Roman')
    plt.xlabel('Intensity values', fontsize=18)
    plt.ylabel('Frequency', fontsize=18)
    plt.bar(intensity_values, eqalized_frequency_vector, color = '#172381')
    plt.legend(('CDF','Histogram'), loc = 'upper center')#, fontsize = 'small')
    #plt.show()
    equalized_histogram.savefig(
        'histogram/results_histogram_equalization/{}_equalized_histogram.png'.format(image_content), 
        dpi = 150)

    eq_hist_save = 'histogram/results_histogram_equalization/{}_cdf_equalized_histogram.png'.format(image_content)

    return hist_save, eq_hist_save, equalized_image