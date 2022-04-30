from tabulate import tabulate
from matplotlib import pyplot as plt
import numpy as np

"""
1. To apply the Bisection Method, firstly an interval of x=[a,b]
   where the function changes sign should be selected. 
2. Then, the output of the function at the point x=m, which is 
   in the middle of this interval, should be checked. 
3. Sign of whichever of a or b the sign of f(m) is the same, m 
   is going to replace that one to form the new [a,b] interval. 
4. This process should be repeated until either the f(m) reaches 
   below tolerance or the number of iterations reach maximum.
"""

def BisectionMethod(func, a, b, mxi, tol):
    #Implementing the function:
    def f(x):
        f = eval(func)
        return f
    
    #Rules of applying:
    m = (a+b)/2
    
    iters = 0
    max_iters = mxi
    tolerance = tol
    conditions = True #Checks if the range is chosen appropriately.
    
    #Applying the method:
    while (abs(f(m)) > tolerance and iters < max_iters):
        #Printing the table in each iteration:
        table= [["-   a   -", "-  f(a)  -", "-   b   -", "-  f(b)  -", " ", "-   m   -", "-  f(m)  -"], 
                [round(a,5), round(f(a),5), round(b,5), round(f(b),5), " ", round(m,5), round(f(m),5)]]
        print(tabulate(table, tablefmt="grid"))
        print()

        #Determining the new interval:
        if ((f(m)>0 and f(a)>0 and f(b)>0) or (f(m)<0 and f(a)<0 and f(b)<0)):
            print("Range limits are not chosen appropriately.", end="\n")
            conditions = False
            break
        elif (f(m)*f(a) < 0):
            a, b = a, m
        elif (f(m)*f(b) < 0):
            a, b = m, b
        else:
            print("Range limits are not chosen appropriately.", end="\n")
            conditions = False
            break
        
        m = (a+b) / 2
        iters +=1

    if conditions == True:
        #Final table at the end of the method
        table= [["-   a   -", "-  f(a)  -", "-   b   -", "-  f(b)  -", " ", "-   m   -", "-  f(m)  -"], 
                [round(a,5), round(f(a),5), round(b,5), round(f(b),5), " ", round(m,5), round(f(m),5)]]
        print(tabulate(table, tablefmt="grid"))
        print()
        
        #Results
        print("Program has found an appropriate root value.")
        print("Number of iterations:", iters)
        print("Approximate root:", m)
        print("f(root):", f(m))
        print()


def FuncPlot(func):
    #Implementing the function
    def f(x):
        f = eval(func)
        return f

    #Boundaries of the plot
    x_min = int(input("Minimum x value of the graph: "))
    x_max = int(input("Maximum x value of the graph: "))
    x = np.linspace(x_min, x_max, 200)

    #Drawing the plot
    plt.figure(figsize=(14,8))
    plt.rcParams.update({"font.size": 22})
    plt.plot(x, f(x), color="red")

    #Title and labels
    plt.title("Initial Function Graph", fontsize=30, fontweight="bold")
    plt.xlabel("x", fontsize=24, fontweight="bold")
    plt.ylabel("f(x)", fontsize=24, fontweight="bold")

    #Gridlines
    plt.grid(True, which="both", axis="both")
    plt.axhline(color="#333333")
    plt.axvline(color="#333333")

    plt.show()


#Execution
ff = str(input("Function: "))
aa = int(input("Lower limit of interval: "))
bb = int(input("Upper limit of interval: "))
mx = int(input("Max iterations: "))
tl = float(input("Tolerance: "))
print()

BisectionMethod(ff, aa, bb, mx, tl)
FuncPlot(ff)
