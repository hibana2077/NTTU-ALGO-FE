
for _ in range(int(input())):
    n_len = int(input())
    num_list = list(map(int, input().split()))
    num_list.sort(reverse=True)
    mup = 1
    ans_list = []
    for t in num_list:
        if (mup*t)%9 == 0:
            mup = mup*t
            ans_list.append(t)
    if mup == 1:
        print(-1)
    else:
        print(' '.join(map(str, ans_list)))
