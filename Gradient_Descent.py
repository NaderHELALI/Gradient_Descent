

import os 
import matplotlib.pyplot as plt 
#Change the repo of work
os.getcwd()
os.chdir("C:/Users/Nader/Documents/Cours Esilv/SEMESTRE 2/Python/Machine Lernia/TD6")
os.getcwd()

#open and stock the data in 2 List
with open("IA_tp6_data.csv",'r') as f :
    lines=f.read().splitlines()
    
    X=[float(val.split(',')[0]) for val in lines]
    Y=[float(val.split(',')[1]) for val in lines]
print(X)
# MSE function   
def MSE(a,b,X,Y):
    res=0
    for i in range(len(X)):
        res+=(Y[i]-a*X[i]+b)**2
    return (1/len(X))*res

# Derivate function

# Gradient du paramètre m
def m_grad(m, b, X, Y):
    return sum(-2 * x * (Y[idx] - (m * x + b)) for idx, x in enumerate(X)) / float(len(X))

# Gradient du paramètre b
def b_grad(m, b, X, Y):
    return sum(-2 * (Y[idx] - (m * x + b)) for idx, x in enumerate(X)) / float(len(X))


def updateAB(a,b,X,Y,alpha):
    a_update=a-alpha*m_grad(a,b,X,Y)
    b_update=b-alpha*b_grad(a,b,X,Y)
    return a_update,b_update


def Gradient(X,Y,compt,alpha):
    a=0
    b=0
    
    for i in range(compt) :
        a=updateAB(a,b,X,Y,alpha)[0]
        
        b=updateAB(a,b,X,Y,alpha)[1]

        print(a)
    return a,b

a,b=(Gradient(X,Y,2000,0.0002))
print(a,b)


plt.scatter(X,Y)
App=[a*min(X)+b,a*max(X)+b]
plt.plot([min(X),max(X)],App,c='r')




