# 4
# 13 3
# 1 2 3 4 5 6 7 0
# 8 9 4 10 13 0
# 11 2 12 9 6 7 0
from collections import Counter
for _ in range(int(input())):
    n,s = map(int,input().split())
    data = [list(map(int,input().split())) for _ in range(s)]
    #先找出重點車站
    c = Counter([i for j in data for i in j])
    c.pop(0)
    point_station = [i for i in c if c[i]>=2]
    point_station_rank = dict()
    print(point_station)
    for check_station in point_station:
        route = [[i[i.index(check_station)-1],i[i.index(check_station)+1]] for i in data if check_station in i]
        possible_point = list(map(sum,list(map(lambda x: [2 if jk in point_station else 1 for jk in x],route))))
        print(f"check_station:{check_station},route:{route},possible_point:{possible_point}")
        point_station_rank[check_station] = sum(possible_point)
    # print(point_station)
    # print(point_station_rank)