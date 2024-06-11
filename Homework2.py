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