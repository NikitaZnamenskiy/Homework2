with open('recipes.txt', encoding= 'utf-8') as file:
    cook_book = {}
    for line in file:
        dish_name = line.strip()
        products_count = int(file.readline())
        products = []
        for i in range(products_count):
            prod = file.readline()
            ingidient_name, count, unit = prod.strip().split(' | ')
            product = {
                'ingridient_name': ingidient_name,
                'count': count,
                'unit': unit
            }
            products.append(product)
        file.readline()
        cook_book[dish_name] = products
    print(cook_book)

def create_shop_list(dishes, person_count):
    result = {}
    for dish in dishes:
        recipe = cook_book[dish]
        for ingidient in recipe:
            key = ingidient['ingridient_name']
            if key not in result:
                new_dict = {
                    'measure': ingidient['measure'],
                    'quantiny': int(ingidient['quantiny']) * person_count
                }
                result[key] = new_dict
            else:
                result[key]['quantity'] += int(ingidient['quantity']) * person_count

    print(result)

    create_shop_list(['Запеченный картофель', 'Омлет', 'Фахитос'], 2)


#Task3
import os

current = os.getcwd()
folder = 'Task3'
file_name_1 = '1.txt'
file_name_2 = '2.txt'
file_name_3 = '3.txt'
file_name_4 = 'new.txt'

with open(os.path.join(current, folder, file_name_1)) as file1, open(os.path.join(current, folder, file_name_2)) as file2, open(os.path.join(current, folder, file_name_3)) as file3, open(os.path.join(current, folder, file_name_4), 'w') as new_file:
    dict_file = {
        file1: [len(file1.readlines()), file_name_1],
        file2: [len(file2.readlines()), file_name_2],
        file3: [len(file3.readlines()), file_name_3]
    }

    dict_file_sort = dict(sorted(dict_file.items(), key=lambda item : item[1][0]))
    # pprint(dict_file_sort, sort_dicts=False)
    file1.seek(0)
    file2.seek(0)
    file3.seek(0)

    for keys, values in dict_file_sort.items():
        new_file.writelines(f'{values[1]}\n')
        new_file.writelines(f'{values[0]}\n')
        for line in keys.readlines():
            new_file.writelines(f'{line}')
        new_file.writelines('\n')