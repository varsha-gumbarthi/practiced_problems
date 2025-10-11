def ls(key,l1):
    for i in range(len(l1)):
        if l1[i]==key:
            return i
    return -1
key=int(input())
l1=list(map(int,input().split()))
print(ls(key,l1))