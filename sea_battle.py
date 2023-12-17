from random import randint
from random import choice
import sys
class Exception:


    @classmethod
    def oneship(cls, x, y, shipss):                                        #перед тем как поставить корабль, данный метод проверяет:
        try:                                                               #1. стоит ли уже в той клетке корабль, если да, то не позволяет его там поставить
            if x > 8 or x < 1 or y > 8 or y < 1:                           #2. проверяет выходит ли голова корабля за границы поля, если да, то не позволяет это сделать
                raise ValueError("Вы поставили корабль за границу")
            for i in shipss:
                for b in i.lifes:
                    if x == b[0] and y == b[1]:
                        raise ValueError ("Вы туда уже ставили корабли")
                    else:
                        close = [[b[0] + 1, b[1] + 1], [b[0] + 1, b[1] - 1], [b[0] + 1, b[1]], [b[0] - 1, b[1]],
                                 [b[0] - 1, b[1] - 1], [b[0] - 1, b[1] + 1], [b[0], b[1] + 1], [b[0], b[1] - 1]]
                        for i in close:
                            if i[0] == x and i[1] == y:
                                raise ValueError("Корабль не может стать рядом в клетке,", x, y)
        except ValueError as e:
            print(e)
            return False
        else:
            return True

    @classmethod
    def oneshot(cls, x, y, shotss):                                    #данный метод не позволяет стрелять в одну и туже точку, а также за пределы карты
        try:
            for i in shotss:
                if x == i[0] and y == i[1]:
                    raise ValueError("Вы туда уже cтреляли")
            if x > 8 or x < 1 or y > 8 or y < 1:
                raise ValueError("Вы стрельнули за границу")
        except ValueError as e:
            print(e)
            return False
        else:
            return True

    @classmethod
    def closeship(cls, x, y, long, side, ships):                      # данный метод не позволяет устанавливать хвосты и головы корабля рядом с иными кораблями
        try:                                                          # также следит за тем, чтобы хвосты не выходили за пределы поля
            if side == 1:                                             #как это работает? перед тем как поставить корабль, данный метод моделирует ситуацию
                k = 1                                                 #при постановлении кораблей. Если нет конфликтов, то запускается сам метод по постановке корабля
                while k < long:
                    y += 1
                    k += 1
                    ship12 = Ship(x, y, side, long, [])
                    if x > 8 or x < 1 or y > 8 or y < 1:
                        raise ValueError ("Невозможно установить корабль за пределы карты,", x, y)
                    for i in ships:
                        for b in i.lifes:
                            if b[0] == ship12.x and b[1] == ship12.y:
                                raise ValueError ("Корабль упирается в клетку", x, y)
                            else:
                                close = [[b[0]+1, b[1]+1], [b[0]+1, b[1]-1], [b[0]+1, b[1]], [b[0]-1,b[1]], [b[0]-1, b[1]-1], [b[0]-1, b[1]+1], [b[0], b[1]+1], [b[0], b[1]-1]]
                                for i in close:
                                    if i[0]==ship12.x and i[1] == ship12.y:
                                        raise ValueError ("Корабль не может стать рядом в клетке,", x, y)


            if side == 2:
                k = 1
                while k < long:
                    x += 1
                    k += 1
                    ship12 = Ship(x, y, side, long, [])
                    if x > 8 or x < 1 or y > 8 or y < 1:
                        raise ValueError ("Невозможно установить корабль за пределы карты,", x, y)
                    for i in ships:
                        for b in i.lifes:
                            if b[0] == ship12.x and b[1] == ship12.y:
                                raise ValueError("Корабль упирается в клетку", x, y)
                            else:
                                close = [[b[0]+1, b[1]+1], [b[0]+1, b[1]-1], [b[0]+1, b[1]], [b[0]-1,b[1]], [b[0]-1, b[1]-1], [b[0]-1, b[1]+1], [b[0], b[1]+1], [b[0], b[1]-1]]
                                for i in close:
                                    if i[0]==ship12.x and i[1] == ship12.y:
                                        raise ValueError ("Корабль не может стать рядом в клетке,", x, y)

            if side == 3:
                k = 1
                while k < long:
                    y -= 1
                    k += 1
                    ship12 = Ship(x, y, side, long, [])
                    if x > 8 or x < 1 or y > 8 or y < 1:
                        raise ValueError ("Невозможно установить корабль за пределы карты,", x, y)
                    for i in ships:
                        for b in i.lifes:
                            if b[0] == ship12.x and b[1] == ship12.y:
                                raise ValueError("Корабль упирается в клетку", x, y)
                            else:
                                close = [[b[0]+1, b[1]+1], [b[0]+1, b[1]-1], [b[0]+1, b[1]], [b[0]-1,b[1]], [b[0]-1, b[1]-1], [b[0]-1, b[1]+1], [b[0], b[1]+1], [b[0], b[1]-1]]
                                for i in close:
                                    if i[0]==ship12.x and i[1] == ship12.y:
                                        raise ValueError ("Корабль не может стать рядом в клетке,", x, y)

            if side == 4:
                k = 1
                while k < long:
                    x -= 1
                    k += 1
                    ship12 = Ship(x, y, side, long, [])
                    if x > 8 or x < 1 or y > 8 or y < 1:
                        raise ValueError ("Невозможно установить корабль за пределы карты,", x, y)
                    for i in ships:
                        for b in i.lifes:
                            if b[0] == ship12.x and b[1] == ship12.y:
                                raise ValueError("Корабль упирается в клетку", x, y)
                            else:
                                close = [[b[0]+1, b[1]+1], [b[0]+1, b[1]-1], [b[0]+1, b[1]], [b[0]-1,b[1]], [b[0]-1, b[1]-1], [b[0]-1, b[1]+1], [b[0], b[1]+1], [b[0], b[1]-1]]
                                for i in close:
                                    if i[0]==ship12.x and i[1] == ship12.y:
                                        raise ValueError ("Корабль не может стать рядом в клетке,", x, y)

                        break
        except ValueError as t:
            print(t)
            return False
        else:
            return True

class Dot:
    def __init__(self, x, y, c = "0"):
        self.x = x
        self.y = y
        self.c = c

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __str__(self):
        return f"{self.x, self.y}"
    def get_shot(self):
        return [self.x, self.y]

    def set_dot1(self):
        self.c = "♢"
    def set_dot2(self):
        self.c = "T"
    def set_dot3(self):
        self.c = "X"

k11, k12, k13, k14, k15, k16, k17, k18 = Dot(1,1), Dot(1,2), Dot(1,3), Dot(1,4), Dot(1,5), Dot(1,6), Dot(1,7), Dot(1,8)
k21, k22, k23, k24, k25, k26, k27, k28 = Dot(2,1), Dot(2,2), Dot(2,3), Dot(2,4), Dot(2,5), Dot(2,6), Dot(2,7), Dot(2,8)
k31, k32, k33, k34, k35, k36, k37, k38 = Dot(3,1), Dot(3,2), Dot(3,3), Dot(3,4), Dot(3,5), Dot(3,6), Dot(3,7), Dot(3,8)
k41, k42, k43, k44, k45, k46, k47, k48 = Dot(4,1), Dot(4,2), Dot(4,3), Dot(4,4), Dot(4,5), Dot(4,6), Dot(4,7), Dot(4,8)
k51, k52, k53, k54, k55, k56, k57, k58 = Dot(5,1), Dot(5,2), Dot(5,3), Dot(5,4), Dot(5,5), Dot(5,6), Dot(5,7), Dot(5,8)
k61, k62, k63, k64, k65, k66, k67, k68 = Dot(6,1), Dot(6,2), Dot(6,3), Dot(6,4), Dot(6,5), Dot(6,6), Dot(6,7), Dot(6,8)
k71, k72, k73, k74, k75, k76, k77, k78 = Dot(7,1), Dot(7,2), Dot(7,3), Dot(7,4), Dot(7,5), Dot(7,6), Dot(7,7), Dot(7,8)
k81, k82, k83, k84, k85, k86, k87, k88 = Dot(8,1), Dot(8,2), Dot(8,3), Dot(8,4), Dot(8,5), Dot(8,6), Dot(8,7), Dot(8,8)

l11, l12, l13, l14, l15, l16, l17, l18 = Dot(1,1), Dot(1,2), Dot(1,3), Dot(1,4), Dot(1,5), Dot(1,6),Dot(1,7), Dot(1,8)
l21, l22, l23, l24, l25, l26, l27, l28 = Dot(2,1), Dot(2,2), Dot(2,3), Dot(2,4), Dot(2,5), Dot(2,6), Dot(2,7), Dot(2,8)
l31, l32, l33, l34, l35, l36, l37, l38 = Dot(3,1), Dot(3,2), Dot(3,3), Dot(3,4), Dot(3,5), Dot(3,6), Dot(3,7), Dot(3,8)
l41, l42, l43, l44, l45, l46, l47, l48 = Dot(4,1), Dot(4,2), Dot(4,3), Dot(4,4), Dot(4,5), Dot(4,6), Dot(4,7), Dot(4,8)
l51, l52, l53, l54, l55, l56, l57, l58 = Dot(5,1), Dot(5,2), Dot(5,3), Dot(5,4), Dot(5,5), Dot(5,6), Dot(5,7), Dot(5,8)
l61, l62, l63, l64, l65, l66, l67, l68 = Dot(6,1), Dot(6,2), Dot(6,3), Dot(6,4), Dot(6,5), Dot(6,6), Dot(6,7), Dot(6,8)
l71, l72, l73, l74, l75, l76, l77, l78 = Dot(7,1), Dot(7,2), Dot(7,3), Dot(7,4), Dot(7,5), Dot(7,6), Dot(7,7), Dot(7,8)
l81, l82, l83, l84, l85, l86, l87, l88 = Dot(8,1), Dot(8,2), Dot(8,3), Dot(8,4), Dot(8,5), Dot(8,6), Dot(8,7), Dot(8,8)

Keki = [l11, l12, l13, l14, l15, l16, l17, l18, l21, l22, l23, l24, l25, l26, l27, l28, l31, l32, l33, l34, l35, l36, l37, l38, l41, l42, l43, l44, l45, l46, l47, l48, l51, l52, l53, l54, l55, l56, l57, l58, l61, l62, l63, l64, l65, l66, l67, l68, l71, l72, l73, l74, l75, l76, l77, l78, l81, l82, l83, l84, l85, l86, l87, l88]
kletki = [k11, k12, k13, k14, k15, k16, k17, k18, k21, k22, k23, k24, k25, k26, k27, k28, k31, k32, k33, k34, k35, k36, k37, k38, k41, k42, k43, k44, k45, k46, k47, k48, k51, k52, k53, k54, k55, k56, k57, k58, k61, k62, k63, k64, k65, k66, k67, k68, k71, k72, k73, k74, k75, k76, k77, k78, k81, k82, k83, k84, k85, k86, k87, k88 ]

class Ship:

    def __init__(self, x, y, side, long, lifes):
        self.x = x
        self.y = y
        self.side = side
        self.long = long
        self.lifes = lifes
    def Dots(self):
        return self.lifes

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    def __str__(self):
        return f"{self.x}, {self.y}"

ow = True

class Board:
    dots = kletki.copy()

    hid = True
    ship_life = None
    shot = []

    def __init__(self, boa, shots, ships):
        self.boa = boa
        self.shots = shots
        self.ships = ships
    def get_ships(self):
        return self.ships

    def add_ship(self, x, y, long, side):                       #Данный метод ставит на поле корабль, после того как пройдены все проверки
        ship11 = Ship(x, y, side, long, [])
        self.ships.append(ship11)
        ship11.lifes.append([x, y])
        for i in self.boa:
            if i == ship11:
                i.set_dot1()
                break
        if side == 1:
            k = 1
            while k < long:
                y += 1
                k += 1
                ship12 = Ship(x, y, side, long, [])
                ship11.lifes.append([x, y])
                for b in self.boa:
                    if b == ship12:
                        b.set_dot1()
                        break
        if side == 2:
            k = 1
            while k < long:
                x += 1
                k += 1
                ship12 = Ship(x, y, side, long, [])
                ship11.lifes.append([x, y])
                for b in self.boa:
                    if b == ship12:
                        b.set_dot1()
                        break
        if side == 3:
            k = 1
            while k < long:
                y -= 1
                k += 1
                ship12 = Ship(x, y, side, long, [])
                ship11.lifes.append([x, y])
                for b in self.boa:
                    if b == ship12:
                        b.set_dot1()
                        break
        if side == 4:
            k = 1
            while k < long:
                x -= 1
                k += 1
                ship12 = Ship(x, y, side, long, [])
                ship11.lifes.append([x, y])
                for b in self.boa:
                    if b == ship12:
                        b.set_dot1()
                        break



    def shot(self, x, y):                   # в данном методе реализован выстрел. Если игрок попал в корабль, то данный метод запускается заного
        global ow
        shot1 = Dot(x, y)
        self.shots.append([x, y])
        for i in self.ships:
            for g in i.lifes:
                if g == shot1.get_shot():
                    for c in self.boa:
                        if c == shot1:
                            c.set_dot3()
                            ow = True
                            break
                    i.lifes.remove(g)
                    if i.lifes == []:
                        self.ships.remove(i)
                    break
                else:
                    for c in self.boa:
                        if c == shot1:
                            if c.c == "X":
                                break
                            else:
                                c.set_dot2()
                                ow = False

        return ow





    def get_board(self):
        return self.boa
    def out(self):                                              # метод по выводу поля
        print(f"  1|2|3|4|5|6|7|8")
        print(f"1|{self.boa[0].c}|{self.boa[1].c}|{self.boa[2].c}|{self.boa[3].c}|{self.boa[4].c}|{self.boa[5].c}|{self.boa[6].c}|{self.boa[7].c}")
        print(f"2|{self.boa[8].c}|{self.boa[9].c}|{self.boa[10].c}|{self.boa[11].c}|{self.boa[12].c}|{self.boa[13].c}|{self.boa[14].c}|{self.boa[15].c}")
        print(f"3|{self.boa[16].c}|{self.boa[17].c}|{self.boa[18].c}|{self.boa[19].c}|{self.boa[20].c}|{self.boa[21].c}|{self.boa[22].c}|{self.boa[23].c}")
        print(f"4|{self.boa[24].c}|{self.boa[25].c}|{self.boa[26].c}|{self.boa[27].c}|{self.boa[28].c}|{self.boa[29].c}|{self.boa[30].c}|{self.boa[31].c}")
        print(f"5|{self.boa[32].c}|{self.boa[33].c}|{self.boa[34].c}|{self.boa[35].c}|{self.boa[36].c}|{self.boa[37].c}|{self.boa[38].c}|{self.boa[39].c}")
        print(f"6|{self.boa[40].c}|{self.boa[41].c}|{self.boa[42].c}|{self.boa[43].c}|{self.boa[44].c}|{self.boa[45].c}|{self.boa[46].c}|{self.boa[47].c}")
        print(f"7|{self.boa[48].c}|{self.boa[49].c}|{self.boa[50].c}|{self.boa[51].c}|{self.boa[52].c}|{self.boa[53].c}|{self.boa[54].c}|{self.boa[55].c}")
        print(f"8|{self.boa[56].c}|{self.boa[57].c}|{self.boa[58].c}|{self.boa[59].c}|{self.boa[60].c}|{self.boa[61].c}|{self.boa[62].c}|{self.boa[63].c}")


my_board = Board([], [],[])
en_bord = Board([], [], [])
my_board.boa = Keki
en_bord.boa = kletki





class User:
    @classmethod
    def shipAI(cls, long):                          #метод, который ставит корабли вместо пользователя
        x = randint(1, 8)
        y = randint(1, 8)
        side = randint(1, 4)
        if Exception.oneship(x, y, my_board.ships):
            if Exception.closeship(x, y, long, side, my_board.ships):
                my_board.add_ship(x, y, long, side)
            else:
                cls.shipAI(long)
        else:
            cls.shipAI(long)
    @classmethod
    def shipp(cls, long):                               #данный метод позволяет самостоятельно выставить корабли.
        print("________________")                       # перед постановкой кораблей, данный метод ссылается на класс исключений,
        print("Ваша доска")                             # где проходят все проверки на возможность постановление корабля,
        my_board.out()                                  # если все проверки пройдены, то запускается метод .add_ship
        try:                                            # Если какая-нибудь проверка не пройдена, то данный метод вызывается заново
            x = int(input("Введите x"))
            y = int(input("Введите y"))
            side = int(input("введите направление"))
            if side > 4 or side < 1:
                raise ValueError ("сторон всего 4")
        except ValueError as t:
            print ("значение не корректно,", t)
            cls.shipp(long)
        else:
            if Exception.oneship(x, y, my_board.ships):
                if Exception.closeship(x, y, long, side, my_board.ships):
                    my_board.add_ship(x, y, long, side)
                else:
                    cls.shipp(long)
            else:
                cls.shipp(long)

    @classmethod
    def ask(cls):
        print("________________")
        print("Доска противника")
        en_bord.out()
        try:
            x = int(input("Введите x"))
            y = int(input("Введите y"))
        except ValueError as t:
            print ("значение не корректно")
            cls.ask()
        else:
            if Exception.oneshot(x, y, en_bord.shots):
                qwe = en_bord.shot(x, y)
                while qwe:
                    print("есть пробитие")
                    if en_bord.ships == []:
                        print("________________")
                        print("Доска противника")
                        en_bord.out()
                        print("Вы победили")
                        exit()
                    print("________________")
                    print("Доска противника")
                    en_bord.out()
                    try:
                        x = int(input("Введите x"))
                        y = int(input("Введите y"))
                    except ValueError as t:
                        print("значение не корректно")
                        cls.ask()
                    else:
                        if Exception.oneshot(x, y, en_bord.shots):
                            qwe = en_bord.shot(x, y)
                        else:
                            qwe = False
                            cls.ask()
            else:
                cls.ask()

    @classmethod
    def move(cls):
        return cls.ask()

class AI:                       #искусственный интелект


    @classmethod
    def shipp(cls, long):
        x = randint(1, 8)
        y = randint(1, 8)
        side = randint(1, 4)
        if Exception.oneship(x, y, en_bord.ships):
            if Exception.closeship(x, y, long, side, en_bord.ships):
                en_bord.add_ship(x, y, long, side)
            else:
                cls.shipp(long)
        else:
            cls.shipp(long)

    @classmethod
    def ask(cls):
        x = randint(1, 8)
        y = randint(1, 8)
        if Exception.oneshot(x, y, my_board.shots):
            qwe = my_board.shot(x, y)
            print("________________")
            print("Ваша доска")
            my_board.out()
            while qwe:
                print("есть пробитие")
                if my_board.ships == []:
                    print("________________")
                    print("Ваша доска")
                    my_board.out()
                    print("Вы проиграли")
                    exit()
                x = randint(1, 8)
                y = randint(1, 8)
                if Exception.oneshot(x, y, my_board.shots):
                    qwe = my_board.shot(x, y)
                else:
                    qwe = False
                    print("________________")
                    print("Ваша доска")
                    my_board.out()
                    cls.ask()
        else:
            cls.ask()
    @classmethod
    def move(cls):
        return cls.ask()

stop = 1
def game():
    AI.shipp(4)
    AI.shipp(3)
    AI.shipp(2)
    AI.shipp(2)
    AI.shipp(1)
    AI.shipp(1)
    AI.shipp(1)
    AI.shipp(1)
    for c in en_bord.boa:
        if c.c == "♢":
            c.c = "0"
    for i in range(1,15):
        print("_______________________________")
    print("Добро пожаловать в игру Морской бой")
    print("Цель игры - уничтожить все корабли противника")
    print("Чтобы поставить корабль укажите x - цифры слева, y - цифры сверху")
    print("Также необходимо указать направление side куда будут смотреть корабли")
    print("1 - вправо, 2 - вниз, 3 - влево, 4 - вверх")
    print("Корабли не могут находится рядом на расстоянии одной клетки")
    print("___________________________________________________________")
    print("НАЧНЕМ")
    print("___________________________________________________________")
    try:
        Question = input("Если вы хотели случайным образом расставить свои корабли, напишите - Да \nЖелаете ли вы, чтобы Вам помогли расставить корабли?")
    except ValueError as E:
        None
    if Question == "Да":
        User.shipAI(4)
        User.shipAI(3)
        User.shipAI(2)
        User.shipAI(2)
        User.shipAI(1)
        User.shipAI(1)
        User.shipAI(1)
        User.shipAI(1)
    else:
        print ("Поставьте корабль с 4 клетками")
        User.shipp(4)
        print("Поставьте корабль с 3 клетками")
        User.shipp(3)
        print("Поставьте корабль с 2 клетками")
        User.shipp(2)
        print("Поставьте корабль с 2 клетками")
        User.shipp(2)
        print("Поставьте корабль с 1 клетками")
        User.shipp(1)
        print("Поставьте корабль с 1 клетками")
        User.shipp(1)
        print("Поставьте корабль с 1 клетками")
        User.shipp(1)
        print("Поставьте корабль с 1 клетками")
        User.shipp(1)
    print("__________")
    print("Ваша доска")
    my_board.out()
    while stop == 1:
        print("Ваш ход")
        User.move()
        print("Ходит противник")
        AI.move()

game()
