def marks(m):
    match m:
        case 9:
            print("Outstanding")
        case 8:
            print("Excellent")
        case 7:
            print("A")
        case 6:
            print("B")
        case 5:
            print("C")
        case 4:
            print("D")
        case 3:
            print("fail")
        case _:
            print("Fail")

list = [42,33,54,12,90,78,88,65]

for index,item in enumerate(list):
    a = int (item/10)
    marks(a)
