def two_sum(list1,target):
    for i in range(len(list1)):
        for j in range(i+1,len(list1)):
            sum=list1[i]+list1[j]
            if sum==target:
                return [i,j]
list1=list(map(int,input().split()))
target=int(input())
print(two_sum(list1,target))