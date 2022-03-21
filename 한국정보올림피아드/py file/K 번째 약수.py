def func(N, K):
    divider = [i for i in range(1, N+1) if N % i == 0]

    if len(divider) < K:
        return -1
    return divider[K-1]


N, K = map(int, input().split())

print(func(N, K))
