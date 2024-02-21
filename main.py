print("\t\tПрограмма Кучук")
print("Угадайка\n")

import random

chislo = random.randint(1,100)
popitki = 0

lvl = int(input("1 - hard, 2 - medium, 3 - ez\n"))
if lvl > 3 or lvl < 1:
    print("Неправильный синтаксис")
ugadayka = int(input("Введите первое число\n"))

if lvl == 1:
    ogranichenie = 7
elif lvl == 2:
    ogranichenie = 5
elif lvl == 3:
    ogranichenie = 3

while chislo != ugadayka:
    ogranichenie += 1
    popitki += 1
    if ogranichenie > 10:
        print("Вы долбоеб")
        quit()
    if ugadayka > chislo:
        print("Попробуй взять число поменьше\n")
        ugadayka = int(input())
    elif ugadayka < chislo:
        print("Попробуй взять число побольше\n")
        ugadayka = int(input())
    if ugadayka == chislo:
        print("Поздравляем с победой")
        break

print('Вы угадали число за ', popitki, " (попытку/попыток)")
