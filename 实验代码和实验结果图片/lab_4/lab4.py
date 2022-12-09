import cv2 as cv
import numpy as np

N=1

H1=[[0, 1, 0],
    [1,-4, 1],
    [0, 1, 0]
]
H2 =[
    [1, 1, 1],
    [1,-8, 1],
    [1, 1, 1]
]

def cov(mat1,mat2):
    sum=0
    for i in range(len(mat1)):
        for j in range(len(mat1[0])):
            sum+=mat1[i][j]*mat2[i][j]
    # if sum<0:
    #     return 0
    # elif sum>255:
    #     return 255
    # else:
    return sum
#handle overflow problem
def handler(val):
    if val < 0:
        return 0
    elif val >255:
        return 255
    else:
        return np.uint8(val)
#Laplacian transformation
def Laplacian(H,mat):
    temp = mat.copy()
    for i in range(N,len(mat)-N):
        for j in range(N,len(mat[0])-N):
            t = mat[i][j]-cov(H,mat[i-N:i+N+1,j-N:j+N+1])
            temp[i][j] = handler(t)
    return temp

img = cv.imread('Laplacian.bmp')

b,g,r = cv.split(img)

L_b = Laplacian(H1,b)
L_g = Laplacian(H1,g)
L_r = Laplacian(H1,r)

L_img = cv.merge([L_b,L_g,L_r])
cv.imshow("H1",L_img)
cv.imwrite("H1.bmp",L_img)
L_b = Laplacian(H2,b)
L_g = Laplacian(H2,g)
L_r = Laplacian(H2,r)

L_img = cv.merge([L_b,L_g,L_r])
cv.imshow("H2",L_img)
cv.imwrite("H2.bmp",L_img)
cv.waitKey(0)
cv.destroyAllWindows()
