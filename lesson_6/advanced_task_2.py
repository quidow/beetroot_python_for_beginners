"""
2. пока человек не введет q или Q или Й или й играем с ним 
в камень ножницы бумага. сделайте множество или кортеж для набора вариантов. 
Рандомно выбирайте один из элементов листа (tandom.choice).

2.1 для игры допишите учет статистики в словарь
stats = {"K": 0, "N": 0, "B":0 }
stats["K"] увеличиваем если человек загадал камень и так далее.
подумайте и допишите если есть больше 10 игр учет статистики предпочтений 
в качестве веса для рандома. (не случайно выбирать ПОТОМ фигуру а с учетом 
статистики. Делать рандом с учетом веса это пока рано но можете попробовать. 
Пока циклы условия, списки, вхождение в кортеж, 
редактирование словарика статистики )
"""

import random

opts = {
    "rock": ("r", "R", "к", "К"),
    "scissors": ("s", "S", "н", "Н"),
    "paper": ("p", "P", "б", "Б"),
    "quit": ("q", "Q", "й", "Й")
}

stats = {
    "rock": 0, 
    "scissors": 0, 
    "paper": 0
}

combos = {
    "rock": {
        "scissors": True,
        "paper": False
    },
    "scissors": {
        "rock": False,
        "paper": True
    },
    "paper": {
        "rock": True,
        "scissors": False
    }
}

print("This is ""rock paper scissors"" game!")
print("Your options are:")
for key in opts:
    print(key, opts[key])
while True:
    x = input("your choice: ")
    for key, val in opts.items():
        if x in val:
            x = key
            break
    else:
        print("your print is invalid")
        continue
    if x == "quit":
        print("bye")
        print("your stats: " + str(stats))
        exit()
    else:
        if sum(stats.values()) > 10:
            y = random.choices(['rock', 'scissors', 'paper'],
                               weights=[stats['scissors'], 
                                        stats['paper'],
                                        stats['rock']])[0]
        else:
            y = random.choice(list(stats.keys()))
        print("my choice is " + y)
        if x == y:
            print("draw!")
        else:
            if combos[x][y]:
                print("you win!")
            else:
                print("you lose!")
        stats[x] += 1
