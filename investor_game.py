import random
b = 67
try:
    myfile = open('balance.txt', 'r', encoding='utf-8')
    my_balance = myfile.readline()
    myfile.close()
except FileNotFoundError:
    myfile = open('balance.txt', 'w', encoding='utf-8')
    myfile.close()
    my_balance = 500
print('Вас приветсвует симулятор инвестиций')
print('1.Сделать ставку\n2.Посмотреть бюджет\n3.Выход')
choose = int(input(': '))
def bet_stavka():
    print('Выберите ставку:\n1)Коэффицент:1.10, Процент:40%\n2)Коэффицент:1.30, Процент:20%\n3)Коэффицент:1.50, Процент:5%\n4)Коэффицент:1.005, Процент:80%')
    bet_choose = int(input(': '))
    myfile = open('balance.txt', 'r', encoding='utf-8')
    my_balance = myfile.readline()
    myfile.close()
    if bet_choose == 1:
        sum_bet = int(input('Выберите сумму которую хотите поставить: '))
        coef = 1.1
        my_chance = 0
        for i in range(0,10):
            chance = random.randint(1,9)
            if chance == 3:
                my_chance += 1
            elif chance == 4:
                my_chance += 1
        if  my_chance >= 4:
            print("Вам повезло")
            my_balance = int(my_balance)
            result = sum_bet * coef
            my_balance += result
            print(f'Ваш баланс стал составлять:{my_balance} рублей')
        else:
            print('Вам не повезло')
            my_balance = int(my_balance)
            my_balance -= sum_bet
            print(f'Ваш баланс стал составлять:{my_balance} рублей')

    if bet_choose == 2:
        sum_bet = int(input('Выберите сумму которую хотите поставить: '))
        coef = 1.3
        my_chance = 0
        for i in range(0, 10):
            chance = random.randint(1, 9)
            if chance == 3:
                my_chance += 1
            elif chance == 4:
                my_chance += 1
        if my_chance >= 3:
            print("Вам повезло")
            my_balance = int(my_balance)
            result = sum_bet * coef
            my_balance += result
            print(f'Ваш баланс стал составлять:{my_balance} рублей')
        else:
            print('Вам не повезло')
            my_balance = int(my_balance)
            my_balance -= sum_bet
            print(f'Ваш баланс стал составлять:{my_balance} рублей')


    if bet_choose == 3:
        sum_bet = int(input('Выберите сумму которую хотите поставить: '))
        coef = 1.5
        my_chance = 0
        for i in range(0, 10):
            chance = random.randint(1, 9)
            if chance == 3:
                my_chance += 1
            elif chance == 4:
                my_chance += 1
        if my_chance >= 2:
            print("Вам повезло")
            my_balance = int(my_balance)
            result = sum_bet * coef
            my_balance += result
            print(f'Ваш баланс стал составлять:{my_balance} рублей')
        else:
            print('Вам не повезло')
            my_balance = int(my_balance)
            my_balance -= sum_bet
            print(f'Ваш баланс стал составлять:{my_balance} рублей')


    if bet_choose == 4:
        sum_bet = int(input('Выберите сумму которую хотите поставить: '))
        coef = 1.005
        my_chance = 0
        for i in range(0, 10):
            chance = random.randint(1, 9)
            if chance == 3:
                my_chance += 1
            elif chance == 4:
                my_chance += 1
        if my_chance >= 1:
            print("Вам повезло")
            my_balance = int(my_balance)
            result = sum_bet * coef
            my_balance += result
            print(f'Ваш баланс стал составлять:{my_balance} рублей')
        else:
            print('Вам не повезло')
            my_balance = int(my_balance)
            my_balance -= sum_bet
            print(f'Ваш баланс стал составлять:{my_balance} рублей')
while b == 67:
    if choose == 1:
        bet_stavka()
    elif choose == 2:
        print(f'Ваш баланс составляет:{my_balance}')
    elif choose == 3:
        myfile = open('balance.txt', 'w', encoding='utf-8')
        myfile.writelines(my_balance)
        myfile.close()
