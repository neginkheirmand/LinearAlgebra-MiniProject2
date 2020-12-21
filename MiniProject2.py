import cv2 as cv
import sys
import os
import numpy as np

def isWhite(color):
    #this method takes in a list representing the color list : [b, g, r]
    #returns true if a pixel with such color can be considered white
    #the function of this method is to reduce the noise

    sumRGB=0
    for i in range(0, len(color)):
        sumRGB+=color[i]
    if (sumRGB/len(color))>250:
        return True
    return False 

def LoadImage(stringName):
    #this function will load an image with the specified name in the current directory
    img = cv.imread(os.getcwd()+"/"+stringName,1)
    #check if the image exists and can be loaded
    if img is None:
        sys.exit("Could not read the image.")
        exit()
    #if the img exist and can be loaded then will be shown in the window named "before" 
    cv.imshow("before", img)
    return img

def shear(matrix, Costumelambda, height, width, depth ):
    newShape = [height,  width + int(height*Costumelambda) ,depth]
    whiteImage = np.zeros(newShape,dtype=np.uint8)
    whiteImage.fill(255)
    #shear transformation standard matrix is represented by variable shearMatrix
    shearMatrix = np.array([[1, 0], [Costumelambda, 1]])
    for i in range(0, height):
        for j in range(0, width):
            whitePixel = True
            for k in range(0, depth):
                if matrix[i, j, k]!=255:
                    whitePixel = False
                    break
            if not whitePixel:
                #the variable passed to the shear transformation is the [x, y] in this case [j, i]
                place = np.array([j, i])
                place=place.dot(shearMatrix)
                whiteImage[int(place[1]), int(place[0])]=[127, 127, 127]
    cv.imshow("h"+str(Costumelambda), whiteImage)
    return whiteImage
    
def createOutput(original, shadow, Costumelambda, height, width, depth):
    newShape = [height,  width + int(height*Costumelambda), depth]
    finalImage = np.zeros(newShape,dtype=np.uint8)
    finalImage.fill(255)
    # we have the base of the picture with only white pixels
    # we go through the original picture and if its not white  
    
    for i in range(0, height):
        for j in range(0, width):
            colorPixel = False
            for k in range(0, depth):
                if original[i, j, k]!=255:
                    colorPixel=True
                    break
            if colorPixel:
                #color it the same as the original picture
                finalImage[i, j]=original[i, j]
            elif shadow[i, j, 0]!=255:
                #if its the shadow color, then the output image should have the shadow in that pixel too
                finalImage[i][j]=shadow[i, j]
    cv.imshow("final image" , finalImage)
             


    

def main():
    nameImage = input("Enter the name of the image: ") 
    image = LoadImage(nameImage)
    height, width, depth = image.shape
    shearImage = shear(image, 0.3, height, width, depth)
    createOutput(image, shearImage, 0.3, height, width, depth)
    # shear(image, 3, height, width, depth)
    # print(img.shape)
    # cv.imshow("Display window", img)
    k = cv.waitKey(0)
    # if k == ord("s"):
        # cv.imwrite("starry_night.png", img)
    cv.destroyAllWindows()

if __name__ == "__main__":
    main()