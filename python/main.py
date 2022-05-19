num = int(input())
for i in range(1, num + 1):

    a = 0
    b = 0
    c = 0
    d = 0
    e = 0
    count = int(input())
    if count / 11 != 0:
        e = count / 11
        if e / 7 != 0:
            d = e / 7
            if d / 5 != 0:
                c = d / 5
                if c / 3 != 0:
                    b = c / 3
                    if b / 2 != 0:
                        a = b / 2
                    else:
                        a = 0
                else:
                    b = 0
            else:
                c = 0
        else:
            d = 0
    else:
        e = 0

    print(f"#{i} {int(a)} {b} {c} {d} {e}")
