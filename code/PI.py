for _ in range(int(input())):
    n,ans = int(input()),-500000
    num_list = list(map(int, input().split()))
    temp = num_list[0]
    for i in range(1, n):
        ans = max(ans, temp - num_list[i])
        if temp < num_list[i]:temp = num_list[i]
    print(ans)