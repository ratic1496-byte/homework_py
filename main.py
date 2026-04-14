def get_cook_book(file_name):
    cook_book = {}
    with open(file_name, 'r', encoding='utf-8') as f:
        for line in f:
            dish_name = line.strip()
            count = int(f.readline())
            ingredients = []
            for _ in range(count):
                name, qty, unit = f.readline().strip().split(' | ')
                ingredients.append({
                    'ingredient_name': name,
                    'quantity': int(qty),
                    'measure': unit
                })
            f.readline()
            cook_book[dish_name] = ingredients
    return cook_book

my_cook_book = get_cook_book('recipes.txt')
print(my_cook_book)

def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    cook_book = get_cook_book('recipes.txt')

    for dish in dishes:
        if dish in cook_book:
            for ingredient in cook_book[dish]:
                name = ingredient['ingredient_name']
                total_qty = ingredient['quantity'] * person_count
                
                if name not in shop_list:
                    shop_list[name] = {
                        'measure': ingredient['measure'],
                        'quantity': total_qty
                    }
                else:
                    shop_list[name]['quantity'] += total_qty
        else:
            print(f"Блюда '{dish}' нет в книге!")
            
    return shop_list


result = get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)

# Красиво выводим результат
import pprint
pprint.pprint(result)