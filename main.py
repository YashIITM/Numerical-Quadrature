from tictoc import *
import numpy as np
import matplotlib.pyplot as plt
import sys
from LinReg import *
from Numerical_Quadrature import *

f = lambda x: np.sin(x)

print('LEFT-ENDPOINT METHOD  |-> 1')
print('RIGHT-ENDPOINT METHOD |-> 2')
print('MIDPOINT METHOD       |-> 3')
print('TRAPEZOID METHOD      |-> 4')
print('|E| VS N              |-> 5')
print('|E| VS h              |-> 6')
print('log(|E|) VS h         |-> 7')
print('log(|E|) VS log(h)    |-> 8')
print("------------------------------------------------")

module = int(input("MODULE NUMBER  = "))
if module > 8:
    print('INCORRECT MODULE INITIATION CODE !')
    exit()
N = int(input('NO. OF ITERATIONS = '))
if N>100000:
    print('MAX NO OF ITERATIONS IS 100000 !')
    exit()
    
ITER_STEP = int(input('SIZE OF EACH ITERATION STEP = '))


if module == 1:
    print("------------------------------------------------")
    print('Left-Endpoint Method Iteration Values and Plots')
    print("------------------------------------------------")

    step = []
    AE = []
    tic()
    for n in range(1,(N+1)*ITER_STEP,ITER_STEP):
        h , abs_err = LM(f,0,np.pi/2,n)
        step.append(h)
        AE.append(abs_err)
    toc()
    # Plot 1: |E| vs h
    linreg_ind(step,AE)
    plt.xlabel('h')
    plt.ylabel('|E|')
    plt.title('|E| vs h : Left-Endpoint Method')
    plt.legend()
    plt.autoscale()
    plt.show()
    # Plot 2: log(|E|) vs h
    linreg_ind(step,np.log(AE))
    plt.xlabel('h')
    plt.ylabel('log(|E|)')
    plt.title('log(|E|) vs h : Left-Endpoint Method')
    plt.legend()
    plt.autoscale()
    plt.show()
    # Plot 3: log(|E|) vs log(h)
    linreg_ind(np.log(step),np.log(AE))
    plt.xlabel('log(h)')
    plt.ylabel('log(|E|)')
    plt.title('log(|E|) vs log(h) : Left-Endpoint Method')
    plt.legend()
    plt.autoscale()
    plt.show()

if module == 2:
    print("------------------------------------------------")
    print('Right-Endpoint Method Iteration Values and Plots')
    print("------------------------------------------------")

    step = []
    AE = []
    tic()
    for n in range(1,(N+1)*ITER_STEP,ITER_STEP):
        h , abs_err = RM(f,0,np.pi/2,n)
        step.append(h)
        AE.append(abs_err)
    toc()
    # Plot 1: |E| vs h
    linreg_ind(step,AE)
    plt.xlabel('h')
    plt.ylabel('|E|')
    plt.title('|E| vs h : Right-Endpoint Method')
    plt.legend()
    plt.autoscale()
    plt.show()
    # Plot 2: log(|E|) vs h
    linreg_ind(step,np.log(AE))
    plt.xlabel('h')
    plt.ylabel('log(|E|)')
    plt.title('log(|E|) vs h : Right-Endpoint Method')
    plt.legend()
    plt.autoscale()
    plt.show()
    # Plot 3: log(|E|) vs log(h)
    linreg_ind(np.log(step),np.log(AE))
    plt.xlabel('log(h)')
    plt.ylabel('log(|E|)')
    plt.title('log(|E|) vs log(h) : Right-Endpoint Method')
    plt.legend()
    plt.autoscale()
    plt.show()

if module == 3:
    print("------------------------------------------------")
    print('Midpoint Method Iteration Values and Plots')
    print("------------------------------------------------")

    step = []
    AE = []
    tic()
    for n in range(1,(N+1)*ITER_STEP,ITER_STEP):
        h , abs_err = MpM(f,0,np.pi/2,n)
        step.append(h)
        AE.append(abs_err)
    toc()
    # Plot 1: |E| vs h
    linreg_ind(step,AE)
    plt.xlabel('h')
    plt.ylabel('|E|')
    plt.title('|E| vs h : Midpoint Method')
    plt.legend()
    plt.autoscale()
    plt.show()
    # Plot 2: log(|E|) vs h
    linreg_ind(step,np.log(AE))
    plt.xlabel('h')
    plt.ylabel('log(|E|)')
    plt.title('log(|E|) vs h : Midpoint Method')
    plt.legend()
    plt.autoscale()
    plt.show()
    # Plot 3: log(|E|) vs log(h)
    linreg_ind(np.log(step),np.log(AE))
    plt.xlabel('log(h)')
    plt.ylabel('log(|E|)')
    plt.title('log(|E|) vs log(h) : Midpoint Method')
    plt.legend()
    plt.autoscale()
    plt.show()

if module == 4:
    print("------------------------------------------------")
    print('Trapezoid Method Iteration Values and Plots')
    print("------------------------------------------------")

    step = []
    AE = []
    tic()
    for n in range(1,(N+1)*ITER_STEP,ITER_STEP):
        h , abs_err = TM(f,0,np.pi/2,n)
        step.append(h)
        AE.append(abs_err)
    toc()
    # Plot 1: |E| vs h
    linreg_ind(step,AE)
    plt.xlabel('h')
    plt.ylabel('|E|')
    plt.title('|E| vs h : Trapezoid Method')
    plt.legend()
    plt.autoscale()
    plt.show()
    # Plot 2: log(|E|) vs h
    linreg_ind(step,np.log(AE))
    plt.xlabel('h')
    plt.ylabel('log(|E|)')
    plt.title('log(|E|) vs h : Trapezoid Method')
    plt.legend()
    plt.autoscale()
    plt.show()
    # Plot 3: log(|E|) vs log(h)
    linreg_ind(np.log(step),np.log(AE))
    plt.xlabel('log(h)')
    plt.ylabel('log(|E|)')
    plt.title('log(|E|) vs log(h) : Trapezoid Method')
    plt.legend()
    plt.autoscale()
    plt.show()


if module == 5:
    AE = []
    S = []
    tic()
    for n in range(1,(N+1)*ITER_STEP,ITER_STEP):
        h , abs_err = LM(f,0,np.pi/2,n)
        S.append(n)
        AE.append(abs_err)
    toc()
    linreg_all(S,AE,'Left-Endpoint')
    AE = []
    tic()
    for n in range(1,(N+1)*ITER_STEP,ITER_STEP):
        h , abs_err = RM(f,0,np.pi/2,n)
        AE.append(abs_err)
    toc()
    linreg_all(S,AE,'Right-Endpoint')
    AE = []
    tic()
    for n in range(1,(N+1)*ITER_STEP,ITER_STEP):
        h , abs_err = MpM(f,0,np.pi/2,n)
        AE.append(abs_err)
    toc()
    linreg_all(S,AE,'Midpoint')
    AE = []
    tic()
    for n in range(1,(N+1)*ITER_STEP,ITER_STEP):
        h , abs_err = TM(f,0,np.pi/2,n)
        AE.append(abs_err)
    toc()
    linreg_all(S,AE,'Trapezoid')
    plt.xlabel('N')
    plt.ylabel('|E|')
    plt.title('|E| vs N')
    plt.legend()
    plt.show()
    

if module == 6:
    AE = []
    step = []
    tic()
    for n in range(1,(N+1)*ITER_STEP,ITER_STEP):
        h , abs_err = LM(f,0,np.pi/2,n)
        step.append(h)
        AE.append(abs_err)
    toc()
    linreg_all(step,AE,'Left-Endpoint')
    AE = []
    tic()
    for n in range(1,(N+1)*ITER_STEP,ITER_STEP):
        h , abs_err = RM(f,0,np.pi/2,n)
        AE.append(abs_err)
    toc()
    linreg_all(step,AE,'Right-Endpoint')
    AE = []
    tic()
    for n in range(1,(N+1)*ITER_STEP,ITER_STEP):
        h , abs_err = MpM(f,0,np.pi/2,n)
        AE.append(abs_err)
    toc()
    linreg_all(step,AE,'Midpoint')
    AE = []
    tic()
    for n in range(1,(N+1)*ITER_STEP,ITER_STEP):
        h , abs_err = TM(f,0,np.pi/2,n)
        AE.append(abs_err)
    toc()
    linreg_all(step,AE,'Trapezoid')
    plt.xlabel('h')
    plt.ylabel('|E|')
    plt.title('|E| vs h')
    plt.legend()
    plt.show()

if module == 7:
    AE = []
    step = []
    tic()
    for n in range(1,(N+1)*ITER_STEP,ITER_STEP):
        h , abs_err = LM(f,0,np.pi/2,n)
        step.append(h)
        AE.append(abs_err)
    toc()
    linreg_all(step,np.log(AE),'Left-Endpoint')
    AE = []
    tic()
    for n in range(1,(N+1)*ITER_STEP,ITER_STEP):
        h , abs_err = RM(f,0,np.pi/2,n)
        AE.append(abs_err)
    toc()
    linreg_all(step,np.log(AE),'Right-Endpoint')
    AE = []
    tic()
    for n in range(1,(N+1)*ITER_STEP,ITER_STEP):
        h , abs_err = MpM(f,0,np.pi/2,n)
        AE.append(abs_err)
    toc()
    linreg_all(step,np.log(AE),'Midpoint')
    AE = []
    tic()
    for n in range(1,(N+1)*ITER_STEP,ITER_STEP):
        h , abs_err = TM(f,0,np.pi/2,n)
        AE.append(abs_err)
    toc()
    linreg_all(step,np.log(AE),'Trapezoid')
    plt.xlabel('h')
    plt.ylabel('log(|E|)')
    plt.title('log(|E|) vs h')
    plt.legend()
    plt.show()

if module == 8:
    AE = []
    step = []
    tic()
    for n in range(1,(N+1)*ITER_STEP,ITER_STEP):
        h , abs_err = LM(f,0,np.pi/2,n)
        step.append(h)
        AE.append(abs_err)
    toc()
    linreg_all(np.log(step),np.log(AE),'Left-Endpoint')
    AE = []
    tic()
    for n in range(1,(N+1)*ITER_STEP,ITER_STEP):
        h , abs_err = RM(f,0,np.pi/2,n)
        AE.append(abs_err)
    toc()
    linreg_all(np.log(step),np.log(AE),'Right-Endpoint')
    AE = []
    tic()
    for n in range(1,(N+1)*ITER_STEP,ITER_STEP):
        h , abs_err = MpM(f,0,np.pi/2,n)
        AE.append(abs_err)
    toc()
    linreg_all(np.log(step),np.log(AE),'Midpoint')
    AE = []
    tic()
    for n in range(1,(N+1)*ITER_STEP,ITER_STEP):
        h , abs_err = TM(f,0,np.pi/2,n)
        AE.append(abs_err)
    toc()
    linreg_all(np.log(step),np.log(AE),'Trapezoid')
    plt.xlabel('log(h)')
    plt.ylabel('log(|E|)')
    plt.title('log(|E|) vs log(h)')
    plt.legend()
    plt.show()



print('END OF PROGRAM : RERUN TO USE A DIFFERENT MODULE')









