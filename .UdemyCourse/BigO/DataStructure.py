import timeit


def method1():
    l=[]
    for i in range(1000):
        l=l+[i]


def method2():
    l = []
    for i in range(1000):
        l.append(i)


def method3():
    l = [n for n in range(1000)]
def method4():
    l = list(range(1000))

'''
10000000 loops, best of 5: 13.9 nsec per loop
10000000 loops, best of 5: 12 nsec per loop
10000000 loops, best of 5: 11.3 nsec per loop
10000000 loops, best of 5: 11.5 nsec per loop
'''
if __name__ == '__main__':
    timeit.main(method1())
    timeit.main(method2())
    timeit.main(method3())
    timeit.main(method4())


