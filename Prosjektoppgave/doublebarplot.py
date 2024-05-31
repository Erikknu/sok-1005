from matplotlib import pyplot as plt
def python2bar(a,b,c,d,e,f,g,h,i):
    new_a = [x+0.3 for x in a]
    plt.clf()
    plt.bar(a,b,0.3)
    plt.bar(new_a,c,0.3)
    plt.title(d)
    plt.legend([e,f])
    plt.xlabel(g)
    plt.ylabel(h)
    plt.savefig(i)
    return plt.show()  