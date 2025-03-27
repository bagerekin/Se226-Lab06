from math import pi
x=30
n=2

# task 1
def factorial(x):
    if x == 0 or x == 1:
        return 1
    else:
        return x * factorial(x - 1)
    
print('factorial for' , x , ':' , factorial(x))

# task 2

val = lambda x,n: (-1)**n * x**(2*n+1) / factorial(2*n+1)
def sine_x(x,n): 
    x_rad = x * pi / 180
    total = 0
    for i in range(n):
        total += val(x_rad,i)
        return total 
    return val(x,n)

print('sine for' , x , ':' ,sine_x(x,n))

# task 3

def harmonic(n):
    sum = 0
    if n== 1:
        sum += 1
    else:
        harmonic(n-1)
        sum += 1/n
    return sum
print('harmonic for' , n , ':' , harmonic(n))
