

print("Что надеть ?")
temp = int(input("Введите температуру: "))
rain = int(input("Есть ли осадки? (1/2) 1 - да 2 - нет: "))


if rain == 1 and 30 > temp > 20 :
    print("футболку, шорты, дождевик")

if rain == 2 and 30 > temp > 20 :
    print("футболку, шорты")
if 20 > temp > 0  :
    level_rain = int(input("Осадки сильные? (1/2) 1 - да 2 - нет: "))

    if 20 > temp > 0 and rain == 1 and level_rain == 1:
        print("пальто, резиновые сапоги, зонт")

    if 20 > temp > 0 and rain == 1 and level_rain == 2:
        print("пальто, дождевик")

if temp < 0:
    print("пуховик")

if 20 > temp > 0  and rain == 2 :
    print("пальто")

print("Хорошего дня :)")