import cv2 as cv
import numpy as np
N=1

def avg_filter(mat):
    temp = mat.copy()
    for i in range(N,len(mat)-N):
        for j in range(N,len(mat[0])-N):
            temp[i][j] = (1/((2*N+1)**2))*np.array(mat[i-N:i+N+1,j-N:j+N+1]).sum()
    return temp

def median_filter(mat):
    temp = mat.copy()
    for i in range(N,len(mat)-N):
        for j in range(N,len(mat[0])-N):
            temp[i][j] = np.median(np.array(mat[i-N:i+N+1,j-N:j+N+1]))
    return temp

img = cv.imread('noise.bmp')
b,g,r = cv.split(img)

avg_b = avg_filter(b)
avg_g = avg_filter(g)
avg_r = avg_filter(r)

avg_img = cv.merge([avg_b,avg_g,avg_r])
cv.imshow("avg",avg_img)
cv.imwrite("avg.bmp",avg_img)
#######################################
b,g,r = cv.split(img)
m_b = median_filter(b)
m_g = median_filter(g)
m_r = median_filter(r)

m_img = cv.merge([m_b,m_g,m_r])
cv.imshow("median",m_img)
cv.imwrite('median..bmp',m_img)
cv.waitKey(0)
cv.destroyAllWindows()

