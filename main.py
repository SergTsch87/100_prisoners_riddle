#!/usr/bin/env python
# -*- coding: utf-8 -*-

# які tdd-тести порадиш написати для такого завдання:
# 1. Генеруємо 100 чисел від 1 до 100.
# 2. Перемішуємо їх у випадковому порядку.
# 3. Виводимо їх на екран.


# Умова:
#   Щойно знаходимо ланцюг len > 50: Припиняємо пошук (генерацію) ланцюгів

def generate_100_numbers() -> list:
    return list(range(1, 101))


def sort_randomly(numbers: list) -> list:
    import random
    random.shuffle(numbers)
    return numbers


def create_dict(shuffled_list: list) -> dict:
    return {i + 1: num for i, num in enumerate(shuffled_list)}


def chain_gen(some_dict: dict) -> dict:
    curr_key = next(iter(some_dict)) # отримуємо перший ключ словника
    list_keys = [] # тут зберігатимемо список ключів ланцюга chain_dict

    while curr_key in some_dict:
        curr_value = some_dict[curr_key]

        # print(f'{curr_key} -> {curr_value}')
    
        list_keys.append(curr_key)
        
        if curr_value == '' or curr_value not in some_dict or curr_value == next(iter(some_dict)):
            break
        
        # Ключ наступної ітерації буде поточним значенням, яке ми отримали з словника за поточним ключем
        curr_key = curr_value

    # if len(list_keys) > 50:
    #     return None

    # Словник із потрібними ключами:
    extracted_dict = {k: some_dict[k] for k in list_keys if k in some_dict}

    # Словник із рештою ключів:
    remaining_dict = {k: v for k, v in some_dict.items() if k not in list_keys}

    # extracted_dict - це словник, який містить лише ті пари ключ-значення з some_dict,
    # які не потрапили до chain_dicts
    return extracted_dict, remaining_dict


def gen_list_dicts(result_dict) -> bool:
    chain_dict = result_dict
    list_dicts = []

    while 1 <= len(result_dict) <= 100:
        chain_dict, remaining_dict = chain_gen(result_dict)
        # print(f'Словник з ланцюгом: {chain_dict}')
        # print(f'Довжина ланцюга: {len(chain_dict)}')
        
        if len(chain_dict) > 50: # Ланцюг > 50 - Це поразка у грі
            return False # Lose!
        
        result_dict = remaining_dict
        # print(f'Оновлений словник: {result_dict}')
        # print('---' * 10)
    
        list_dicts.append(chain_dict)

    # return list_dicts
    return True # Win!


def main() -> None:
    for row in range(1, 11):
        for col in range(1, 11):
            new_list = generate_100_numbers()
            # print(f'Генеруємо 100 чисел від 1 до 100: {new_list}')
            shuffled_list = sort_randomly(new_list)
            # print(f'Перемішуємо їх у випадковому порядку: {shuffled_list}')
            result_dict = create_dict(shuffled_list)
            # print(f'Створюємо словник: {result_dict}')
            
            # Win or Lose
            if gen_list_dicts(result_dict):
                print(1, end="")
            else:
                print(0, end="")

        print()


if __name__ == '__main__':
    main()