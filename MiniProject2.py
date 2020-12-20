import cv2 as cv
import sys
import os

def LoadImage(stringName):
    #this function will load an image with the specified name in the current directory
    img = cv.imread(os.getcwd()+"/TestCase1.png",1)
    if img is None:
        sys.exit("Could not read the image.")
        return None
    #if the img exist and can be loaded then will be shown in th window named "before" 
    cv.imshow("before", img)
    return img

def main():
    LoadImage("TestCase2.png")

    # print(img)
    # print(img.shape)
    # cv.imshow("Display window", img)
    k = cv.waitKey(0)
    # if k == ord("s"):
        # cv.imwrite("starry_night.png", img)
    cv.destroyAllWindows()

if __name__ == "__main__":
    main()