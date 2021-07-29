from tictoc import *
import numpy as np
import matplotlib.pyplot as plt
import sys
from LinReg import *
#from Numerical_Quadrature import *
def LM(f,a,b,n):
    # Carries out the numerical integration using the Left Hand Rule
    # INPUT: f , a , b , n
    # f : function which is the integrand
    # a : lower limit of the interval
    # b : upper limit of the interval
    # n : number of sub-intervals

    # makes sure the input format is correct
    if (b < a) :
        print('Input Error: Lower limit(a) must be < Upper limit(b)')
        exit()
    # limits the maximum number of iterations to 1 million
    if (n > 1000000) :
        print('Input Error: No more than 1 million divisions are allowed!')
        exit()
    # calculate the step size or length of each sub-interval
    h = (b - a)/n
    step.append(h)
    N.append(n)
    # calculates the numerical integration using Left Hand Rule
    area = 0
    for i in range(n):
        x = a + float(i*h)
        area = area + f(x)*h
    # calculates error
    err = 1 - area
    rel_err = np.abs(err)*100
    abs_err.append(np.abs(err))
    print('---------------------------------------------------')
    print('NUMERICAL QUADRATURE RESULTS : LEFT-ENDPOINT METHOD')
    print('---------------------------------------------------')
    print('Integrating from %8.2f    to %8.2f   in %5d steps' %(a,b,n))
    print('Area           = %10.4f units\u00b2'%(area))
    print('Error          = %10.4f'%err)
    print('Absolute Error = %10.4f '%(np.abs(err)))
    print('Relative Error = %10.4f'%rel_err)
    print('---------------------------------------------------')
    
def RM(f,a,b,n):
    # Carries out the numerical integration using the Right Hand Rule
    # INPUT: f , a , b , n
    # f : function which is the integrand
    # a : lower limit of the interval
    # b : upper limit of the interval
    # n : number of sub-intervals

    # makes sure the input format is correct
    if (b < a) :
        print('Input Error: Lower limit(a) must be < Upper limit(b)')
        exit()
    # limits the maximum number of iterations to 1 million
    if (n > 1000000) :
        print('Input Error: No more than 1 million divisions are allowed!')
        exit()
    # calculate the step size or length of each sub-interval
    h = (b - a)/n
    step.append(h)
    N.append(n)
    # calculates the numerical integration using Right Hand Rule
    area = 0
    for i in range(1,n+1):
        x = a + float(i*h)
        area = area + f(x)*h
    # calculates error
    err = 1 - area
    rel_err = np.abs(err)*100
    abs_err.append(np.abs(err))
    print('---------------------------------------------------')
    print('NUMERICAL QUADRATURE RESULTS : RIGHT-ENDPOINT METHOD')
    print('---------------------------------------------------')
    print('Integrating from %8.2f    to %8.2f   in %5d steps' %(a,b,n))
    print('Area           = %10.4f units\u00b2'%(area))
    print('Error          = %10.4f'%err)
    print('Absolute Error = %10.4f '%(np.abs(err)))
    print('Relative Error = %10.4f'%rel_err)
    print('---------------------------------------------------')

def MpM(f,a,b,n):
    # Carries out the numerical integration using the Midpoint Rule
    # INPUT: f , a , b , n
    # f : function which is the integrand
    # a : lower limit of the interval
    # b : upper limit of the interval
    # n : number of sub-intervals

    # makes sure the input format is correct
    if (b < a) :
        print('Input Error: Lower limit(a) must be < Upper limit(b)')
        exit()
    # limits the maximum number of iterations to 1 million
    if (n > 1000000) :
        print('Input Error: No more than 1 million divisions are allowed!')
        exit()
    # calculate the step size or length of each sub-interval
    h = (b - a)/n
    step.append(h)
    N.append(n)
    # calculates the numerical integration using Midpoint Rule
    area = 0
    for i in range(n):
        x = a + float((i+0.5)*h)
        area = area + f(x)*h
    # calculates error
    err = 1 - area
    rel_err = np.abs(err)*100
    abs_err.append(np.abs(err))
    print('---------------------------------------------------')
    print('NUMERICAL QUADRATURE RESULTS : MIDPOINT METHOD')
    print('---------------------------------------------------')
    print('Integrating from %8.2f    to %8.2f   in %5d steps' %(a,b,n))
    print('Area           = %10.4f units\u00b2'%(area))
    print('Error          = %10.4f'%err)
    print('Absolute Error = %10.4f '%(np.abs(err)))
    print('Relative Error = %10.4f'%rel_err)
    print('---------------------------------------------------')

def TM(f,a,b,n):
    # Carries out the numerical integration using the Trapezoidal Rule
    # INPUT: f , a , b , n
    # f : function which is the integrand
    # a : lower limit of the interval
    # b : upper limit of the interval
    # n : number of sub-intervals

    # makes sure the input format is correct
    if (b < a) :
        print('Input Error: Lower limit(a) must be < Upper limit(b)')
        exit()
    # limits the maximum number of iterations to 1 million
    if (n > 1000000) :
        print('Input Error: No more than 1 million divisions are allowed!')
        exit()
    # calculate the step size or length of each sub-interval
    h = (b - a)/n
    step.append(h)
    N.append(n)
    # calculates the numerical integration using Trapezoidal Rule
    area = f(float(a))*h/2
    for i in range(1,n):
        x = a + float(i*h)
        area = area + f(x)*h
    area = area + f(float(b))*h/2
    # calculates error
    err = 1 - area
    rel_err = np.abs(err)*100
    abs_err.append(np.abs(err))
    print('---------------------------------------------------')
    print('NUMERICAL QUADRATURE RESULTS : TRAPEZOID METHOD')
    print('---------------------------------------------------')
    print('Integrating from %8.2f    to %8.2f   in %5d steps' %(a,b,n))
    print('Area           = %10.4f units\u00b2'%(area))
    print('Error          = %10.4f'%err)
    print('Absolute Error = %10.4f '%(np.abs(err)))
    print('Relative Error = %10.4f'%rel_err)
    print('---------------------------------------------------')


f = lambda x: np.sin(x)

step = []
abs_err = []
N = []
tic()
for n in range(10,100,10):
    LM(f,0,np.pi/2,n)
toc()
#plot(step,abs_err,'b','Left Endpoint')
linreg(N,abs_err,'Left Endpoint')
step = []
abs_err = []
N = []
tic()
for n in range(10,100,10):
    RM(f,0,np.pi/2,n)
toc()
#plot(step,abs_err,'b','Left Endpoint')
linreg(N,abs_err,'Right Endpoint')
step = []
abs_err = []
N = []
tic()
for n in range(10,100,10):
    MpM(f,0,np.pi/2,n)
toc()
#plot(step,abs_err,'b','Left Endpoint')
linreg(N,abs_err,'Midpoint')
step = []
abs_err = []
N = []
tic()
for n in range(10,100,10):
    TM(f,0,np.pi/2,n)
toc()
#plot(step,abs_err,'b','Left Endpoint')
linreg(N,abs_err,'Trapezoid')
plt.xlabel('N')
plt.ylabel('|E|')
plt.legend()
plt.title('|E| vs N')
plt.show()









# PLOTTING log(|E|) vs log(h):
step = []
abs_err = []
N = []
tic()
for n in range(10,1020,10):
    LM(f,0,np.pi/2,n)
toc()
#plot(step,abs_err,'b','Left Endpoint')
linreg(np.log(step),np.log(abs_err),'Left Endpoint')
step = []
abs_err = []
tic()
for n in range(10,1020,10):
    RM(f,0,np.pi/2,n)
toc()
#plot(step,abs_err,'r','Right Endpoint')
linreg(np.log(step),np.log(abs_err),'Right Endpoint')
step = []
abs_err = []
tic()
for n in range(10,1020,10):
    MpM(f,0,np.pi/2,n)
toc()
#plot(step,abs_err,'g','Midpoint')
linreg(np.log(step),np.log(abs_err),'Midpoint')
step = []
abs_err = []
tic()
for n in range(10,1020,10):
    TM(f,0,np.pi/2,n)
toc()
#plot(step,abs_err,'g','Midpoint')
linreg(np.log(step),np.log(abs_err),'Trapezoid')
plt.legend()
plt.ylabel('log(|E|)')
plt.xlabel('log(h)')
plt.title('log(|E|) vs log(h)')
plt.show()


# PLOTTING log(|E|) vs h:
step = []
abs_err = []
N = []
tic()
for n in range(10,1020,10):
    LM(f,0,np.pi/2,n)
toc()
#plot(step,abs_err,'b','Left Endpoint')
linreg(step,np.log(abs_err),'Left Endpoint')
step = []
abs_err = []
tic()
for n in range(10,1020,10):
    RM(f,0,np.pi/2,n)
toc()
#plot(step,abs_err,'r','Right Endpoint')
linreg(step,np.log(abs_err),'Right Endpoint')
step = []
abs_err = []
tic()
for n in range(10,1020,10):
    MpM(f,0,np.pi/2,n)
toc()
#plot(step,abs_err,'g','Midpoint')
linreg(step,np.log(abs_err),'Midpoint')
step = []
abs_err = []
tic()
for n in range(10,1020,10):
    TM(f,0,np.pi/2,n)
toc()
#plot(step,abs_err,'g','Midpoint')
linreg(step,np.log(abs_err),'Trapezoid')
plt.legend()
plt.ylabel('log(|E|)')
plt.xlabel('h')
plt.legend()
plt.title('log(|E|) vs h')
plt.show()



# PLOTTING |E| vs h:
step = []
abs_err = []
N = []
tic()
for n in range(10,1020,10):
    LM(f,0,np.pi/2,n)
toc()
#plot(step,abs_err,'b','Left Endpoint')
linreg(step,abs_err,'Left Endpoint')
step = []
abs_err = []
N =[]
tic()
for n in range(10,1020,10):
    RM(f,0,np.pi/2,n)
toc()
#plot(step,abs_err,'r','Right Endpoint')
linreg(step,abs_err,'Right Endpoint')
step = []
abs_err = []
N = []
tic()
for n in range(10,1020,10):
    MpM(f,0,np.pi/2,n)
toc()
#plot(step,abs_err,'g','Midpoint')
linreg(step,abs_err,'Midpoint')
step = []
abs_err = []
N = []
tic()
for n in range(10,1020,10):
    TM(f,0,np.pi/2,n)
toc()
#plot(step,abs_err,'g','Midpoint')
linreg(step,abs_err,'Trapezoid')
plt.legend()
plt.ylabel('|E|')
plt.xlabel('h')
plt.title('|E| vs h')
plt.show()



# PLOTTING |E| vs n:
step = []
N = []
abs_err = []
tic()
for n in range(10,1020,10):
    LM(f,0,np.pi/2,n)
toc()
#plot(step,abs_err,'b','Left Endpoint')
linreg(N,abs_err,'Left Endpoint')
step = []
abs_err = []
N = []
tic()
for n in range(10,1020,10):
    RM(f,0,np.pi/2,n)
toc()
#plot(step,abs_err,'r','Right Endpoint')
linreg(N,abs_err,'Right Endpoint')
step = []
abs_err = []
N = []
tic()
for n in range(10,1020,10):
    MpM(f,0,np.pi/2,n)
toc()
#plot(step,abs_err,'g','Midpoint')
linreg(N,abs_err,'Midpoint')
step = []
abs_err = []
N = []
tic()
for n in range(10,1020,10):
    TM(f,0,np.pi/2,n)
toc()
#plot(step,abs_err,'g','Midpoint')
linreg(N,abs_err,'Trapezoid Method')
plt.legend()
plt.title('|E| vs N')
plt.xlabel('N')
plt.ylabel('|E|')
plt.show()



# PLOTTING log(|E|) vs h:
step = []
abs_err = []
tic()
for n in range(10,1020,10):
    LM(f,0,np.pi/2,n)
toc()
#plot(step,abs_err,'b','Left Endpoint')
linreg(step,np.log(abs_err),'Left Endpoint')
step = []
abs_err = []
tic()
for n in range(10,1020,10):
    RM(f,0,np.pi/2,n)
toc()
#plot(step,abs_err,'r','Right Endpoint')
linreg(step,np.log(abs_err),'Right Endpoint')
step = []
abs_err = []
tic()
for n in range(10,1020,10):
    MpM(f,0,np.pi/2,n)
toc()
#plot(step,abs_err,'g','Midpoint')
linreg(step,np.log(abs_err),'Midpoint')
step = []
abs_err = []
tic()
for n in range(10,1020,10):
    TM(f,0,np.pi/2,n)
toc()
#plot(step,abs_err,'g','Midpoint')
linreg(step,np.log(abs_err),'Trapezoid')
plt.legend()
plt.ylabel('log(|E|)')
plt.xlabel('h')
plt.legend()
plt.title('log(|E|) vs h')
plt.show()



# PLOTTING log(|E|) vs log(h):
step = []
abs_err = []
tic()
for n in range(10,1020,10):
    LM(f,0,np.pi/2,n)
toc()
#plot(step,abs_err,'b','Left Endpoint')
linreg(np.log(step),np.log(abs_err),'Left Endpoint')
step = []
abs_err = []
tic()
for n in range(10,1020,10):
    RM(f,0,np.pi/2,n)
toc()
#plot(step,abs_err,'r','Right Endpoint')
linreg(np.log(step),np.log(abs_err),'Right Endpoint')
step = []
abs_err = []
tic()
for n in range(10,1020,10):
    MpM(f,0,np.pi/2,n)
toc()
#plot(step,abs_err,'g','Midpoint')
linreg(np.log(step),np.log(abs_err),'Midpoint')
step = []
abs_err = []
tic()
for n in range(10,1020,10):
    TM(f,0,np.pi/2,n)
toc()
#plot(step,abs_err,'g','Midpoint')
linreg(np.log(step),np.log(abs_err),'Trapezoid')
plt.legend()
plt.ylabel('log(|E|)')
plt.xlabel('log(h)')
plt.title('log(|E|) vs log(h)')
plt.show()



