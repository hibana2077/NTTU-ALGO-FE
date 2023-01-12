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
    "0": "0"
}

#another way to do it
def sol2(in_str:str):return (sum(list(map(lambda x: x.isalpha(),in_str))),in_str.count("-"),"".join(list(map(lambda x: sorted(list(map(lambda y: mapping[y] if x in y else "",mapping)),reverse=True)[0],in_str))))

while True:
    try:
        out = sol2(input())
        print(f"{out[2]} {out[0]} {out[1]}")
    except EOFError:break