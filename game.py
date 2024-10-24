
import random

# Инициализация глобальных переменных
inventory = []
levels = {
    1: "Масло для двери",
    2: "Pdiddy",
    3: "Загадка",
    4: "Выход из замка Pdiddy"
}
monster_defeated = False
completed_tasks = set()
keys_found = set()
monster_required_item = "Канье"
total_keys = 3

# Функция для отображения инвентаря
def show_inventory():
    print("Ваш карман:", inventory if inventory else "пуст.")

# Функция для получения бутылок
def collect_keys():
    global keys_found
    print("Вы ищете бутылки с маслом в комнате...")
    keys = {f"бутылка{num}" for num in range(1, total_keys + 1)}
    
    while keys:
        action = input("Что вы хотите сделать? (взять, проверить карман): ").lower()
        if action == "взять":
            key = random.choice(list(keys))
            keys.remove(key)
            keys_found.add(key)
            inventory.append(key)
            print(f"Вы нашли {key}. Осталось бутылок: {len(keys)}.")
        elif action == "проверить карман":
            show_inventory()
        else:
            print("Неверная команда, попробуйте снова.")
    print("Вы собрали все бутылки!")

# Функция для нахождения Канье
def find_sword():
    print("Вы ищете Канье, чтобы победить Pdiddy.")
    if "Канье" not in inventory:
        print("Вы нашли Канье!")
        inventory.append("Канье")

# Функция для уровня 1
def level_one():
    print("Вы находитесь в комнате где спрятаны бутылки с маслом. Найдите бутылки с маслом. На бутылках будет код для выхода из замка.")
    collect_keys()

    while True:
        action = input("Что хотите сделать? (убежать, карман): ").lower()
        if action == "убежать" and keys_found:
            print("Вы убежали с маслом за пазухой.")
            completed_tasks.add(levels[1])
            break
        elif action == "карман":
            show_inventory()
        else:
            print("Неверная команда, попробуйте снова.")

# Функция для уровня 2
def level_two():
    global monster_defeated
    print("Вы вошли в темный коридор и встретили Pdiddy!")
    find_sword()

    while True:
        action = input("Что вы хотите сделать? (победить, убежать, карман): ").lower()
        if action == "победить":
            if "Канье" in inventory:
                print("Вы победили Pdiddy с помощью Канье!")
                monster_defeated = True
                completed_tasks.add(levels[2])
                break
            else:
                print("Для победы над Pdiddy вам нужен Канье!")
                continue
        elif action == "убежать":
            print("Вы убежали от Pdiddy, но все еще находитесь на белой вечеринке.")
        elif action == "карман":
            show_inventory()
        else:
            print("Неверная команда, попробуйте снова.")

# Функция для уровня 3
def level_three():
    print("Вы оказались в комнате, где играет песня. Угадайте кто её поет чтобы выбраться.")
    puzzle_answer = "джастин бибер"

    while True:
        answer = input("Baby, baby, baby, oh like baby, baby, baby, no ").lower()
        if answer == puzzle_answer:
            print("Вы угадали кто поёт песню и выбрались из замка Pdiddy!")
            completed_tasks.add(levels[3])
            break
        else:
            print("Неправильный ответ. Попробуйте еще раз.")

# Функция для уровня 4
def level_four():
    print("Вы находитесь у выхода из замка, но дверь закрыта.")
    secret_code = "FREEPDIDDY"  # Код для выхода

    while True:
        code = input("Введите код для выхода: ")
        if code == secret_code:
            print("Вы успешно выбрались из замка! Поздравляем!")
            completed_tasks.add(levels[4])
            break
        else:
            print("Неверный код. Попробуйте ещё раз.")

# Главная функция игры
def game():
    print("Добро пожаловать в замок Pdiddy!")
    level_one()
    if levels[1] in completed_tasks:
        print("Вы прошли уровень 1.")
    level_two()
    if monster_defeated:
        print("Вы прошли уровень 2.")
    level_three()
    if levels[3] in completed_tasks:
        print("Вы прошли уровень 3.")
    level_four()
    if levels[4] in completed_tasks:
        print("Вы завершили игру. Поздравляем!")

# Начало игры
if __name__ == "__main__":
    game()
