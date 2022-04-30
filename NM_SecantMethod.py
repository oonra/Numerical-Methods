from tabulate import tabulate
from matplotlib import pyplot as plt
import numpy as np

def SecantMethod(func, a, b, mxi, tol):
    #Implementing the function:
    def f(x):
        f = eval(func)
        return f

    #Rules of Applying
    m = a - (f(a) * ( (a-b) / (f(a)-f(b)) ))

    iters = 0
    max_iters = mxi
    tolerance = tol

    #Applying the method:
    while (abs(f(m)) > tolerance and iters < max_iters and (a != b)):
        #Printing the table in each iteration:
        table= [["-   a   -", "-  f(a)  -", "-   b   -", "-  f(b)  -", " ", "-   m   -", "-  f(m)  -"], 
                [round(a,4), round(f(a),4), round(b,4), round(f(b),4), " ", round(m,4), round(f(m),4)]]
        print(tabulate(table, tablefmt="grid"))
        print()
        
        #Finding the m, the point in the x-axis which the secant line touches
        m = a - (f(a) * ( (a-b) / (f(a)-f(b)) ))

        #Advancing to next iteration
        a, b = b, m
        iters += 1
    
    #Final table at the end of the method
    table= [["-   a   -", "-  f(a)  -", "-   b   -", "-  f(b)  -", " ", "-   m   -", "-  f(m)  -"], 
            [round(a,4), round(f(a),4), round(b,4), round(f(b),4), " ", round(m,4), round(f(m),4)]]
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

SecantMethod(ff, aa, bb, mx, tl)
FuncPlot(ff)
