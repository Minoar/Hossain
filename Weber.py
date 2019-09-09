import numpy as np
import cv2
from PIL import Image

img = Image.new('RGB', (250,250), color='white')
img.save('pil_red.png')
img2 = cv2.imread('pil_red.png',cv2.IMREAD_GRAYSCALE)
cv2.imshow('Orginal',img2)



height = img2.shape[0]
width = img2.shape[1]


brightness = 60

for i in np.arange(height):
    for j in np.arange(width):
        a = img2.item(i, j)
        b= a - brightness
        if b > 255:
            b = 255
        img2.itemset((i, j), b)

cv2.imshow('image',img2)


#brightness1 =1
#brightness1 =2
#brightness1 =3
#brightness1 =5
#brightness1 =20
brightness1 =50

for i in np.arange(height):
    for j in np.arange(width):
        if (i > 90 and i<150 and j>90 and j<150):
            a1 = img2.item(i, j)
            b1 = a1 - brightness1
            if b1 > 255:
                b1 = 255
            img2.itemset((i, j), b1)
cv2.imshow('image1',img2)
print("Weber's ratio:",brightness1/img2[1,1])

cv2.waitKey(0)
cv2.destroyAllWindows()

