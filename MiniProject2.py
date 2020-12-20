import cv2 as cv
import sys
import os

def LoadImage(stringName):
    #this function will load an image with the specified name in the current directory
    img = cv.imread(os.getcwd()+"/"+stringName,1)
    #check if the image exists and can be loaded
    if img is None:
        sys.exit("Could not read the image.")
        return None
    #if the img exist and can be loaded then will be shown in the window named "before" 
    cv.imshow("before", img)
    return img



def main():
    nameImage = input("Enter the name of the image: ") 
    image = LoadImage(nameImage)
    if image==None:
        #end the program here 
        return
    
    height, width, depth = image.shape
    # print(img.shape)
    # cv.imshow("Display window", img)
    k = cv.waitKey(0)
    # if k == ord("s"):
        # cv.imwrite("starry_night.png", img)
    cv.destroyAllWindows()

if __name__ == "__main__":
    main()