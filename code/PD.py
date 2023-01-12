for test_case in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))
    cnt = 0
    for t in range(n):
        if t != 0:
            for j in arr[0:t]:
                if arr[t] >= j:
                    cnt += 1
    print(cnt)