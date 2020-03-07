def f(x):
    res = 0
    for n in range(x+1):
        res = res + (n**2)
    return res
    
n = int(input())
if n == 0:
    print()
else:
    print(f(n)) 



