import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

#read image
f = open('lena.bmp')
img = cv.imread('lena.bmp')
b,g,r = cv.split(img)

#separate the BGR channel
#just make other channels be zeros matrix
zeros = np.zeros(img.shape[:2], dtype='uint8')
img_r = cv.merge([zeros, zeros, r])
img_b = cv.merge([b, zeros, zeros])
img_g = cv.merge([zeros, g, zeros])

cv.imshow("r",img_r)
cv.imshow("g",img_g)
cv.imshow("b",img_b)
cv.imwrite('img_r.bmp',img=img_r)
cv.imwrite('img_g.bmp',img=img_g)
cv.imwrite('img_b.bmp',img=img_b)

#
y = np.ndarray(img.shape[:2], dtype='uint8')
u = np.ndarray(img.shape[:2], dtype='uint8')
v = np.ndarray(img.shape[:2], dtype='uint8')

#handle overflow problem
def handler(val):
    if val < 0:
        return 0
    elif val >255:
        return 255
    else:
        return np.uint8(val)
#bgr to yuv according to the formula in the slide
for i in range(img.shape[:2][0]):
    for j in range(img.shape[:2][1]):
        tmp_y = 0.229 * r[i][j] + 0.587 * g[i][j] + 0.114 * b[i][j]     
        y[i][j] = handler(tmp_y)
    
        tmp_u = 0.564 * (float(b[i][j]) - float(y[i][j]))
        u[i][j] = handler(tmp_u)

        tmp_v = 0.713 * (float(r[i][j]) - float(y[i][j]))
        v[i][j] = handler(tmp_v)

cv.imshow("y",y)
cv.imshow("u",u)
cv.imshow("v",v)
cv.imwrite('img_y.bmp',y)
cv.imwrite('img_u.bmp',u)
cv.imwrite('img_v.bmp',v)

def transform(val):
    a=100
    b=160
    c=50
    d=200

    if val>b:
        return d
    elif a<=val<=b:
        return ((d-c)/(b-a))*(val-a)+c
    elif val<a:
        return c

for i in range(len(y)):
    for j in range(len(y[0])):
        y[i][j] = transform(y[i][j])

cv.imshow("y_linear",y)
cv.imwrite('y_linear_transform.bmp',y)

cv.waitKey(0)
cv.destroyAllWindows()