cnt = 0
def factors(s:int):
    ans = []
    for i in range(1,s+1):
        if s%i==0:
            ans.append(i)
    return ans

while True:
    
    try:
        a = int(input())
        state = 0
        if a==0:break
        for t in range(1,a+1):
            if sum(factors(t))==a:
                state = 1
                break
        if state==1:
            print(f"Case {cnt+1}: {t}")
        else:
            print(f"Case {cnt+1}: -1")
        cnt+=1
    
    except EOFError:break

#如果會爆時間的話 可以先用本地端跑 1 ~ 1000 的結果 改成只要查表就好