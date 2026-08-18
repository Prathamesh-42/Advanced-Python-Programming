memo = {}
def f(n):    
    if n <= 1:
        return n
    
    if n in memo:
        return memo[n]

    memo[n] = f(n - 1) + f(n - 2)
    return memo[n]

n = int(input("Enter the value of n: "))
print("The", n, "th Fibonacci number is:", f(n))
