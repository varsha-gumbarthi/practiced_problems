a = int(input())
n=int(input())
digits = list(map(int, str(a))) 
for i in digits:
    sq = pow(i,n)
    print(sq)