def func(num_list, s, e, k):
    ordered_list = num_list[s-1:e]
    ordered_list.sort()
    answer = ordered_list[k-1]
    return answer


T = int(input())

for _ in range(T):
    N, s, e, k = map(int, input().split())
    num_list = list(map(int, input().split()))
    print(func(num_list, s, e, k))
