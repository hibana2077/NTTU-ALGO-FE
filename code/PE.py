# 2
# 3
# A2 56
# B8 75
# C1 56
# 4
# B1 15
# B2 35
# B3 15
# B4 35


for cnt in range(int(input())):
    if cnt != 0:
        print()
    data = [input().split() for _ in range(int(input()))]
    data = map(lambda x: (x[0], int(x[1])), data)
    data = sorted(data, key=lambda x: x[0] , reverse=False)
    data = sorted(data, key=lambda x: x[1] , reverse=True)
    label = list()
    label_state = 0
    hidden_state = 0
    label_cnt = 0
    for i in range(len(data)):
        if data[i][1] == label_state:
            label.append([label_cnt, data[i][0], data[i][1]])
            hidden_state += 1
        else:
            label_state = data[i][1]
            if hidden_state == 0:
                label_cnt += 1
            else:
                label_cnt += hidden_state+1
                hidden_state = 0
            label.append([label_cnt, data[i][0], data[i][1]])

    print("\n".join(map(lambda x: " ".join(map(str, x)), label)))
    
        