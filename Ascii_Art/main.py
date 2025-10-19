import cv2
import numpy as np
import sys

symbols_list = ["#","-","*",".","+","o"]
threshold_list =[0,50,100,150,200]

def print_out_ascii(array):
    '''Print the code image with symbol'''
    for row in array:
        for e in row:
            #select the symbol based on the coding
            print(symbols_list[int(e)%len(symbols_list)], end ="")
        print()
def img_to_ascii(image):
    '''return the numeric code image'''

    #resizinf parameters
    #adjust the parameter if the output doesn't fit to the screen
    height, width = image.shape
    new_width = int(width / 20)
    new_height = int(height / 40)

    #resize image to fit in the screen
    resized_image = cv2.resize(image, (new_width, new_height),)

    thresh_image = np.zeros(resized_image.shape)

    for i , threshold in enumerate(threshold_list):
        thresh_image[thresh_image>threshold] = i
    return thresh_image

if __name__ == "__main__":
    if len(sys.argv)<2:
        print("Image path is not specified")
        image_path = "sample_image.png" # Default image path

    if len(sys.argv) == 2:
        print("Using {} as Image Path\n".format(sys.argv[1]))

    image = cv2.imread(image_path,0)

    ascii_art = img_to_ascii(image)
    print_out_ascii(ascii_art)




