#to find sum of pyramid elements
def pyramid(n):
    total_sum=0
    for i in range(1,n+1):
        
        for j in range(i,0,-1):
            total_sum+=j
        for j in range(2,i+1): 
            total_sum+=j
    return total_sum
n=int(input())
print(pyramid(n))



#to print pyramid

# def pyramid(n):
#     for i in range(1,n+1):
#         print(" " * (n-i),end="")
#         for j in range(i,0,-1):
#             print(j,end="")    #prints 321
#         for j in range(2,i+1): #prints 23        did not used 2 to avoid duplicates
#             print(j,end="")
#         print()
# n=int(input())
# print(pyramid(n))