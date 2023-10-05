# Guido van Rossum <guido@python.org>
import random


def step1():
    print("Утка-маляр 🦆 решила выпить зайти в бар. " "Взять ей зонтик? ☂️")
    option = ""
    options = {"да": True, "нет": False}
    while option not in options:
        print("Выберите: {}/{}".format(*options))
        option = input()

    if options[option]:
        return step2_umbrella()
    return step2_no_umbrella()


def bear_dice(from_chick=False):
    gambling = {"угадай число": True, "четное/нечетное": False}
    budget = 100
    print("Утка-маляр 🦆 нашла между перьями 100 рублей.")
    while budget > 0:
        print(f"Сейчас у утки 🦆 {budget} рублей. ", "Утка выбирает ставку: ")
        bet = int(input("Ваша ставка: \n"))
        if bet < 0:
            print("Ставка не может быть отрицательной! ")
            continue
        elif bet == 0:
            print(
                "Медведь не хочет играть на интерес",
                "Назвался груздем - полезай в кузов!",
            )
            continue
        elif budget < bet:
            print("У утки 🦆 нет таких денег :( Выберете правильную ставку: ")
            continue
        budget -= bet
        game = ""
        while game not in gambling:
            print(
                "Выберете игру. "
                "При выигрыше в четном/нечетном 🦆 получит удвоенную ставку.\n"
                "При победе в угадай число 🦆 получит упятиренную ставку"
            )
            game = input("Утка выбрала: {} / {}\n".format(*gambling))

        if gambling[game]:
            print("Утка выбрала угадать число. Какое число выпало медведю? ")
            dice_predict = ""
            while not dice_predict.isdecimal():
                dice_predict = input("Введите, сколько выпало на кости: \n")

            dice = random.randint(1, 6)
            print(f"Медведю выпало {dice}")
            if dice == int(dice_predict):
                budget += 5 * bet
                print("Ура! Утка-маляр 🦆 выиграла! Утка продолжит игру?")
            else:
                print("Утка-маляр 🦆 проиграла! Утка продолжит игру?")
        else:
            print(
                "Утка выбрала поставить на четное/нечетное. "
                "Какое число выпало медведю?"
            )
            odd = {"четное": 0, "нечетное": 1}
            dice_predict = ""
            while dice_predict not in odd:
                print("Введите, что выпало на кости: {}/{}".format(*odd))
                dice_predict = input()

            dice = random.randint(1, 6)
            print(f"Медведю выпало {dice}")
            if dice % 2 == odd[dice_predict]:
                budget += 2 * bet
                print("Ура! Утка-маляр 🦆 выиграла! Утка продолжит игру?")
            else:
                print("Утка-маляр 🦆 проиграла! Утка продолжит игру?")
        option = ""
        options = {"да": True, "нет": False}
        while option not in options:
            print("Выберите: {}/{}".format(*options))
            option = input()
        if options[option]:
            continue
        else:
            break
    else:
        print("У утки закончились деньги и она недовольно покрякала домой...")
    if from_chick:
        if budget >= 150:
            print(f"Утка купила зонтик ☂️ и пошла в бар с {budget - 150} руб.")
        else:
            print(
                "Утке не удалось заработать на зонтик ☂️ и она пошла домой."
                f"Зато между перьев {budget} руб."
            )
    else:
        if 100 < budget:
            print(f"Утка выиграла {budget - 100} руб. и потопала в бар!")
        elif 0 < budget and budget <= 100:
            print(
                f"Утка проиграла {-budget + 100} руб.",
                "и недовольно потопала в бар",
            )
        elif option == "нет" and budget == 0:
            print(
                'Утка обиженно ушла домой'
            )


def step2_umbrella():
    print(
        "Утка-маляр 🦆 взяла зонтик и вышла на улицу. "
        "Ну и дождь тут!!! Определенно, зонтик был взят не зря (кря!) "
        "Как пойти утке 🦆 - длинным или коротким путем?"
    )
    way = ""
    ways = {"длинный": True, "короткий": False}
    while True:
        way = input("Выберете: {}/{}\n".format(*ways))
        if way in ways:
            break
    if ways[way]:
        print(
            "К 🦆 подошел странный медведь в шляпе. "
            "🦆 предлагается сыграть в кости."
        )
        decisions = {"Согласиться": True, "Отказаться": False}
        while True:
            decision = input("Что выберет 🦆: {}/{}\n".format(*decisions))
            if decision in decisions:
                break
        if decisions[decision]:
            return bear_dice()
        else:
            print("Медведь рассказал анекдот про нюанс. " "Утка  передумала?")
            while True:
                decision = input("Что выберет 🦆: {}/{}\n".format(*decisions))
                if decision in decisions:
                    break
            if decisions[decision]:
                return bear_dice()
            else:
                print(
                    "Утка 🦆 ушла от медведя и добралась до бара. "
                    "Пусть накрякается!!!"
                )
    else:
        print("Утка 🦆 добралась до бара. " "Пусть накрякается!!!")


def step2_no_umbrella():
    print(
        "Ну и дождь тут!!! Определенно, зонтик зря не взяла( (кря!) "
        "Утка немного прошла под дождем и началась гроза. "
        "Без зонтика тут совсем никак!!! "
        "Недалеко утка увидела петуха, продающего зонтики."
    )
    print(
        "Выяснилось, что зонтик стоит 150 рублей. У утки же всего 100.",
        "Петух посоветовал обратиться к медведю, которого можно найти\
            за углом и сыграть с ним в азартную игру.",
    )
    answers = {"да": True, "нет": False}
    ans = ""
    while ans not in answers:
        ans = input("Пойти к медведю? {} / {}\n".format(*answers))
    if answers[ans]:
        print("Утка пошла за угол.")
        print("К 🦆 подошел странный медведь в шляпе. ")
        return bear_dice(from_chick=True)
    else:
        print("Утка грустно пошла домой :(")


if __name__ == "__main__":
    step1()
