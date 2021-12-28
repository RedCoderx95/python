from random import randint

point = 0

for i in range(5):
    num = int(input("Գուշակիր ինչ թիվ է։ "))
    x = randint(1, 10)
    if num == x:
        print("Գերազանց է")
        point += 1
    elif num == x + 2 or num == x - 2:
        print("Ոչինչ")
        point += 0.52
    else:
        print("Փորձիր կրկին")
print()
print("Դուք վաստակել եք։ ", point, " միավոր")
print("Դուք  գուշակել եք մաքսիմալ հնարավորի։ ", (point/5)*100, "%-ը")



