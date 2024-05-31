from matplotlib import pyplot as plt

def pythonbar(a,b,d,e,g,h,i):
    plt.clf()
    plt.bar(a,b)
    plt.title(d)
    plt.legend([e])
    plt.xlabel(g)
    plt.ylabel(h)
    plt.savefig(i)
    return plt.show()   


