def two_parts(n,A):
   total=sum(A)
   prefix_sum=0
   result=[]
   for i in range(n):
       prefix_sum+=A[i]
       suffix_sum=total - prefix_sum
       result.append(abs(prefix_sum - suffix_sum))
   return result 
n=int(input())
A=list(map(int,input().split()))
print(two_parts(n,A))