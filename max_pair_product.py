# Noah is given an integer array A of length N. He must perform the foliowing operations:

# Select any integer pair having sum equal to 18 from the array.

# Select the pair with maximum product such that the first element of the pair is greater than the second element of the pair.

# Your task is to help Noah find and return a pair in the form of an integer array, which satisfies the mentioned conditions.

# Input Specification:

# input1: An integer value N, representing the size of array A.

# Input2: An integer array A.

# Output Specification:

# Return  a pair in the form of an integer array, which satisfies the mentioned conditions.

# Sample Input:

# 8

# 11 12 2 8 10 11 9 8

# Sample Output:

# [10, 8]



def find_pair(N, A):
    best_pair = None
    max_product = float('-inf')
    
    # Check all pairs
    for i in range(N):
        for j in range(i+1, N):
            if A[i] + A[j] == 18:
                # Ensure first element > second element
                if A[i] > A[j]:
                    product = A[i] * A[j]
                    if product > max_product:
                        max_product = product
                        best_pair = [A[i], A[j]]
                elif A[j] > A[i]:
                    product = A[i] * A[j]
                    if product > max_product:
                        max_product = product
                        best_pair = [A[j], A[i]]
    
    return best_pair
N=int(input())
A=list(map(int,input().split()))
print(find_pair(N,A))
