from matplotlib import pyplot as plt
import numpy as np

def stackedbar(a,b1,b2,b3,d,e1,e2,e3,g,h,i):
    bt2 = np.add(b1,b2)
    plt.clf()
    plt.bar(a,b1, color = "b")
    plt.bar(a,b2, bottom = b1, color = "r")
    plt.bar(a,b3, bottom = bt2, color = "g")
    plt.title(d)
    plt.legend([e1,e2,e3])
    plt.xlabel(g)
    plt.ylabel(h)
    plt.savefig(i)
    return plt.show()   

