# for test_case in range(int(input())):
#     n = int(input())
#     arr = list(map(int,input().split()))
#     cnt = 0
#     for t in range(n):
#         if t != 0:
#             for j in arr[0:t]:
#                 if arr[t] >= j:
#                     cnt += 1
#     print(cnt)

# 2
# 5
# 38 111 102 111 177

#another solution

for _ in range(int(input())):
    n,arr = int(input()),list(map(int,input().split()))
    print(sum([arr[i] >= arr[j] for i in range(n) for j in range(i)]))
