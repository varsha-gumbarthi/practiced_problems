def alex(n):
    if n==0 or n==1:
        return 1
    f0, f1 = 1, 1
    for i in range (2,n+1):
        fn=(f1*f1+f0*f0)%47
        f0, f1=f1,fn
    return fn
n=int(input())
result=alex(n)
print(result)

# Alex is exploring a series and she came across a special series, in which

# f(N)=f(N-1)*f(N-1)+(N-2)*(N-2) mod 47

# where f(0) = 1. f(1)=1

# Your task is to help Alex find and return an integer value, representing the Nth  number in this special series.

# Input Specification:

# input1: An integer value N.

# Output Specification:

# Return an integer value, representing the Nth number in this special fibonacci series.

# Sample Input:

# 4

# Sample Output:

# 29

