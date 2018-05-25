def f(x):
    return x**6+101*x**5+425*x**4-425*x**2-101*x-1
 
def dif_f(x):
    return 6*x**5+5*101*x**4+4*425*x**3-2*425*x-101
 
if __name__ == '__main__':
    eps = 5*10**-6
    intervals = [[-97, -96], [-96, -95], [-1.5, -0.5], [-0.5, -0.1], [-0.1, 0.1], [0.8, 1.2]]
    for interval in intervals:
        x1 = interval[0]
        x2 = interval[1]
        while True:
            x1 = x1-f(x1)/dif_f(x1)
            x2 = x1-((x2-x1)*f(x1)/(f(x2)-f(x1)))
            if abs(x2-x1) < eps:
                break
        print('x = {0}'.format((x1+x2)/2))
