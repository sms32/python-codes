# Create a program to load an image and demonstrate the following operations on it
# a) Display the image
# b) Plot the image in console window
# c) Display the image size(width and height)
# d) Reduce the Image size of its half size
# e) Rotate the image 145 degrees
# f) Resize the image with 50 units in x direction and 70 units in y direction
# g) Flip the image (Left to Right, Top to Bottom)
# h) Crop the image
# i) Change the color image to GrayScale, Black and White
# j) Apply blur effect on the image





from PIL import Image
import matplotlib.pyplot as plt
from PIL import ImageFilter
img = Image.open('C:\HP PENDRIVE BACKUP\FINAL\GAME.png')
imgg = Image.open('C:\HP PENDRIVE BACKUP\FINAL\GAME.png')
img.show()
plt.imshow(img)
plt.show()
print(img.width,img.height)
newimg = img.resize((img.width//2,img.height//2))
newimg.show()
rotateimg = img.rotate(145)
rotateimg.show()
imgg.thumbnail((50,70))
imgg.show()
flippimg = img.transpose(Image.FLIP_LEFT_RIGHT)
flipimg = flippimg.transpose(Image.FLIP_TOP_BOTTOM)
flipimg.show()
area=(60,215,124,278)
croppedimg = img.crop(area)
croppedimg.show()
grayimg= img.convert('LA')
grayimg.show()
blur= img.filter(ImageFilter.GaussianBlur(radius=8))
blur.show()
