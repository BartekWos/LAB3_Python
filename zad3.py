import timeit
from functools import lru_cache

def fibo(n):
   if n <= 1:
       return n
   else:
       return(fibo(n-1) + fibo(n-2))

@lru_cache #pamięć podręczna 
def fibo2(n):
   if n <= 1:
       return n
   else:
       return(fibo2(n-1) + fibo2(n-2))

if __name__ == '__main__':

    imports_and_vars=globals()
    imports_and_vars.update(locals())

    fibo_nb = 30

    # print(fibo(fibo_nb))

    time = timeit.timeit('fibo(fibo_nb)', number=20, globals=imports_and_vars)
    print(time)

    time2 = timeit.timeit('fibo2(fibo_nb)', number=20, globals=imports_and_vars)
    print(time2)
