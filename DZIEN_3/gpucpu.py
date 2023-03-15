from numba import jit,cuda
import numpy as np
from timeit import default_timer as timer

def noramlfunc(a):
    for i in range(10000000):
        a[i] += 1

@jit(target_backend='cuda')
def gpufunc(a):
    for i in range(10000000):
        a[i] += 1

if __name__ == '__main__':
    n = 10000000
    a = np.ones(n,dtype=np.float64)
    start =timer()
    noramlfunc(a)
    print(f"proces na CPU: {timer()-start} s")

    start = timer()
    gpufunc(a)
    print(f"proces na GPU: {timer() - start} s")
