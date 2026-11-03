# fibonacci series

def fibo(n):
    fibo(1)==0
    fibo(2)==1

    fibo(n)=(fibo(n-1)+fibo(n-2))
    return fibo(n)

print(fibo(5))