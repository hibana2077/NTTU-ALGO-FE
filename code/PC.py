mapping = {
    "ABC": "2",
    "DEF": "3",
    "GHI": "4",
    "JKL": "5",
    "MNO": "6",
    "PQRS": "7",
    "TUV": "8",
    "WXYZ": "9",
    "-": "-",
    "1": "1",
}

#another way to do it
def sol2(in_str:str):return (sum(list(map(lambda x: x.isalpha(),in_str))),in_str.count("-"),"".join(list(map(lambda x: sorted(list(map(lambda y: mapping[y] if x in y else "",mapping)),reverse=True)[0],in_str))))

while True:
    try:
        input_str = input()
        # alphabet_count = 0
        # dash_count = 0
        # for find in input_str:
        #     alphabet_count+=1 if find.isalpha() else 0
        #     dash_count+=1 if find=="-" else 0
        #     print(sorted(list(map(lambda x: mapping[x] if find in x else "",mapping)),reverse=True)[0],end="")

        # print(f" {alphabet_count} {dash_count}")
        #sol2
        out = sol2(input_str)
        print(f"{out[2]} {out[0]} {out[1]}")
    except EOFError:
        break