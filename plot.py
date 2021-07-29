import matplotlib.pyplot as plt
def plot(h,abs_err,color,name):
    plt.scatter(h,abs_err,color = color,label = name)
    plt.title("|E| vs x ")
    plt.xlabel('h')
    plt.ylabel('|E|')
    #plt.show()
def SLplot(h,abs_err,color,name):
    plt.scatter(np.log(h),abs_err,color = color,label = name)
    plt.title("log(|E|) vs x ")
    plt.xlabel('h')
    plt.ylabel('|E|')
    #plt.show()
def LLplot(h,abs_err,color,name):
    plt.scatter(np.log(h),np.log(abs_err),color = color,label = name)
    plt.title("log(|E|) vs log(x)")
    plt.xlabel('h')
    plt.ylabel('|E|')
    #plt.show()
    
