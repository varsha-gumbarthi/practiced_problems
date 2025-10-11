def max_two(n,list1):
    list1.sort()
    sum=0
    i,j=0,len(list1)-1
    while i<j:
        sum+=abs(list1[j]-list1[i])
        i+=1
        j-=1
    return sum
n=int(input())
list1=list(map(int,input().split()))
print(max_two(n,list1))