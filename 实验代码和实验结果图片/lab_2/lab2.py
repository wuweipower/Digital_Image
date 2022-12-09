import cv2 as cv
import math
import numpy as np
gray = cv.imread('gray.bmp')
gamma = cv.imread('gamma.bmp')

b,g,r = cv.split(gray)
#reverse process
reverse_b= 256-1-b
reverse_g = 256-1-g
reverse_r = 256-1-r
reverse = cv.merge([reverse_b,reverse_g,reverse_r])
cv.imshow("reverse",reverse)
cv.imwrite('reverse.bmp',reverse)

#log process
c =10
log_b=b.copy()
log_g=g.copy()
log_r=r.copy()

for i in range(b.shape[0]):
    for j in range(b.shape[1]):
        log_b[i][j] = c*math.log2(1+b[i][j])
        log_g[i][j] = c*math.log2(1+g[i][j])
        log_r[i][j] = c*math.log2(1+r[i][j])
log = cv.merge([log_b,log_g,log_r])
cv.imshow("log",log)
cv.imwrite('log.bmp',log)

#power process
c=10
b,g,r = cv.split(gray)
power_b = b.copy()
power_g = g.copy()
power_r = r.copy()

#handle overflow
def handler(val):  
    if val < 0:
        return np.uint(0)
    elif val >255:       
        return np.uint(255)
    else:
        return np.uint8(val)

for i in range(len(b)):
    for j in range(len(b[0])):
        temp_b = 10*pow(int(b[i][j]),10)
        power_b[i][j] = handler(temp_b)
        temp_g = 10*(int(g[i][j])**10)
        power_g[i][j] = handler(temp_g)
        temp_r = 10*pow(int(r[i][j]),10)
        power_r[i][j] = handler(temp_r)   


power = cv.merge([power_b,power_g,power_r])
cv.imshow("power",power)
cv.imwrite("power.bmp",power)
##############################################


b,g,r = cv.split(gamma)
C = 255
def gamma_process(mat,gamma_val):
    temp = mat.copy()
    for i in range(len(temp)):
        for j in range(len(temp[0])):
            t = ((temp[i][j]/C)**(1/gamma_val))*C
            if(t>255):
                t=255
            
            temp[i][j] = t
    return temp
#0.4
g_b = gamma_process(b,0.4)
g_g = gamma_process(g,0.4)
g_r = gamma_process(r,0.4)

gamma_img = cv.merge([g_b,g_g,g_r])
cv.imshow("gamama_0.4.bmp",gamma_img)
cv.imwrite('gamama_0.4.bmp',gamma_img)

#0.6
g_b = gamma_process(b,0.6)
g_g = gamma_process(g,0.6)
g_r = gamma_process(r,0.6)

gamma_img = cv.merge([g_b,g_g,g_r])
cv.imshow("gamama_0.6.bmp",gamma_img)
cv.imwrite('gamama_0.6.bmp',gamma_img)

#0.8
g_b = gamma_process(b,0.8)
g_g = gamma_process(g,0.8)
g_r = gamma_process(r,0.8)

gamma_img = cv.merge([g_b,g_g,g_r])
cv.imshow("gamama_0.8.bmp",gamma_img)
cv.imwrite('gamama_0.8.bmp',gamma_img)

cv.waitKey(0)
cv.destroyAllWindows()
