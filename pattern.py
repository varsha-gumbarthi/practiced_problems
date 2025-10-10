N = int(input())

for i in range(N):
    for num in range(N, 0, -1):
        print((str(num) + " ") * (N - i), end="")
    print()
