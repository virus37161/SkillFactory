q, w, e, r, t, y, u, i, o = "-", "-", "-", "-", "-", "-", "-", "-", "-",
def field():
    x0 = "  1 2 3"
    x1 = "1 %s %s %s" %(q, w, e)
    x2 = "2 %s %s %s" %(r, t, y)
    x3 = "3 %s %s %s" %(u, i, o)
    return print(x0 + "\n" + x1 + "\n" + x2 + "\n" + x3 + "\n")
print("Чтобы указать место, куда необходимо поставить символ, введите цифровое значение (сначала цифру расположенную слева, затем цифру, расположенную вверху)")
field()

end = True
def value ():
    end1 = not any(
        [all([q == w == e, q != "-", w != "-", e != "-"]),
         all([r == t == y, r != "-", t != "-", y != "-"]),
         all([u == i == o, u != "-", i != "-", o != "-"]),
         all([q == r == u, u != "-", r != "-", q != "-"]),
         all([w == t == i, w != "-", t != "-", i != "-"]),
         all([e == y == o, e != "-", y != "-", o != "-"]),
         all([q == t == o, q != "-", t != "-", o != "-"]),
         all([u == t == e, u != "-", t != "-", e != "-"])]
    )
    return end1
p = 0
while end:
    z = int(input("Ходят крестики"))
    while z != 11 and z!= 12 and z!= 13 and z!= 21 and z!= 22 and z!= 23 and z!= 31 and z!= 32 and z!= 33:
        print ("вы ввели неверное значение, попробуйте снова")
        z = int(input("Укажите корректное значение"))
    q = "x" if z == 11 else q; w = "x" if z == 12 else w; e = "x" if z == 13 else e; r = "x" if z == 21 else r; t = "x" if z == 22 else t; y = "x" if z == 23 else y; u = "x" if z == 31 else u; i = "x" if z == 32 else i; o = "x" if z == 33 else o
    field()
    end = value()
    p +=1
    if not end:
        print("победу одержали крестики")
        break
    if p == 9:
        print("ничья")
        break
    z = int(input("Ходят нолики"))
    while z != 11 and z!= 12 and z!= 13 and z!= 21 and z!= 22 and z!= 23 and z!= 31 and z!= 32 and z!= 33:
        print ("вы ввели неверное значение, попробуйте снова")
        z = int(input("Укажите корректное значение"))
    q = "0" if z == 11 else q; w = "0" if z == 12 else w; e = "0" if z == 13 else e; r = "0" if z == 21 else r; t = "0" if z == 22 else t; y = "0" if z == 23 else y; u = "0" if z == 31 else u; i = "0" if z == 32 else i; o = "0" if z == 33 else o
    field()
    end = value()
    if not end:
        print("победу одержали нолики")
    p += 1


