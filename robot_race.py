def race(X,N,Y,M):
    t1=X
    t2=Y
    while t1!=t2:
        if t1<t2:
            t1+=N
        else:
            t2+=M
    return t1
X,N,Y,M=map(int,input().split())
print(race(X,N,Y,M))





















# Problem Statement:
# There is a robot race happening between two robots named Robotop and Robocop. Both the robots reach the starting point to begin the race on a Circular track

# Race starts at time T = 0 seconds. Robotop starts the race at T = Xth second and takes exactly N seconds to complete one lap. On the other hand. Robocop starts the race at T = Yth second and takes exactly M seconds to complete one lap.

#  Your task is to find and return an integer value, representing the least time T (in seconds) at which these two robots meet each other again at the starting point.

# Sample Input:

# 2 3 1 4

# Sample Output:

# 5

# Explanation:

# X=2, N=3, Y=1, N=4

# Robotop starts at T=2 and completes one lap every 3 seconds. Robocop starts at T=1 and completes one lap every 4 seconds. The smallest point where both meet at the starting point is 5 seconds.



