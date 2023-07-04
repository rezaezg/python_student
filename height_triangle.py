""" numerical triangle of height N-1 and 1 <= N <= 9
1
22
333
4444
55555 """

# with range
for i in range(1, int(input())):
    print(i * (10 ** i // 9))

# with range and lambda
for n in range(1,int(input())):
    print(sum(map(lambda i: n * 10**i, range(n))))
