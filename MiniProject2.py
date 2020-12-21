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
    if (sumRGB/len(color))>245:
        return True
    return False 

def LoadImage(stringName):
    #this function will load an image with the specified name in the current directory and return the loaded matrix of pixels
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
            if not isWhite(matrix[i, j]):
                #the variable passed to the shear transformation is the [x, y] in this case [j, i]
                place = np.array([j, i])
                place=place.dot(shearMatrix)
                #the default shadpw color is light grey= [127, 127, 127] 
                whiteImage[int(place[1]), int(place[0])]=[127, 127, 127]
    cv.imshow("h"+str(Costumelambda), whiteImage)
    return whiteImage
    
def createOutput(original, shadow, Costumelambda, height, width, depth):
    #this function will create the output image based on the colorful pixels of the original picture(in first place) and the shadow pixels of the shear image
    newShape = [height,  width + int(height*Costumelambda), depth]
    finalImage = np.zeros(newShape,dtype=np.uint8)
    finalImage.fill(255)
    # we have the base of the picture with only white pixels
    # we go through the original picture and if its not white  
    
    for i in range(0, height):
        for j in range(0, width):
            if not isWhite(original[i, j]):
                #color it the same as the original picture
                finalImage[i, j]=original[i, j]
            elif shadow[i, j, 0]!=255:
                #if its the shadow color, then the output image should have the shadow in that pixel too
                finalImage[i][j]=shadow[i, j]
    #now we iterate over the parts of shadow pic that are not part of the original one
    for i in range(0, height):
        for j in range(width, width + int(height*Costumelambda)):
            if shadow[i, j, 0]!=255:
                #if its the shadow color, then the output image should have the shadow in that pixel too
                finalImage[i][j]=shadow[i, j]
    #and we show the final version of the image, with shadow
    cv.imshow("final image" , finalImage)
    return finalImage

def main():
    nameImage = input("Enter the name of the image: ") 
    image = LoadImage(nameImage)
    height, width, depth = image.shape
    while True:
        try:
            costumeLambda = input("please enter your costume lambda(for horizontal shear transformation)")
            costumeLambda = float(costumeLambda)
            break
        except ValueError:
            print("Oops!  That was no valid number.  Try again...")
    #create the shadow containing image
    shearImage = shear(image, costumeLambda, height, width, depth)

    #create the final version of the image with shadow
    finalVersion = createOutput(image, shearImage, costumeLambda, height, width, depth)
    print("press s so save the final output")
    k = cv.waitKey(0)
    if k == ord("s"):
        cv.imwrite("finalVersionOf_"+nameImage, finalVersion)
        print("output saved as finalVersionOf_"+nameImage)
    cv.destroyAllWindows()

if __name__ == "__main__":
    main()