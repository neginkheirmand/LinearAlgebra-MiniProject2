### Features

- Compatible with  png, jpg, bmp, ... files.
- you can choose the shadow color from the [color scheme](https://github.com/neginkheirmand/LinearAlgebra-MiniProject2/blob/master/colorScheme.jpg?raw=true)

# Shadow creating program
[this](https://github.com/neginkheirmand/LinearAlgebra-MiniProject2/blob/master/MiniProject2.py) script takes an white background-ed image and creates shadow for the shape in the middle.
###examples:

input pic:

![](https://github.com/neginkheirmand/LinearAlgebra-MiniProject2/blob/master/TestCase2.png?raw=true)

output pic:

![](https://github.com/neginkheirmand/LinearAlgebra-MiniProject2/blob/master/finalVersionOf_TestCase2.png?raw=true) 

input pic:

![](https://github.com/neginkheirmand/LinearAlgebra-MiniProject2/blob/master/TestCase1.png?raw=true)

output pic:
(using the costume blue as shadow's color)

![](https://github.com/neginkheirmand/LinearAlgebra-MiniProject2/blob/master/finalVersionOf_TestCase1.png?raw=true) 

### Algorithm :
Create the shadow file by multiplicating the image matrix by the standard shear transformation matrix(to get a horizontal shear transformed image), then color all the non-white pixels to the shadow color. Now iterate over the original picture and color the white-pixels with the corresponding pixel color of the shadow image.

[python script](https://github.com/neginkheirmand/LinearAlgebra-MiniProject2/blob/master/MiniProject2.py)

###### **prequisites:** numpy and OpenCV library

### End
