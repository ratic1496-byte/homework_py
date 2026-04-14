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


file_names = ['1.txt', '2.txt', '3.txt'] 

all_data = []

def get_lines_count(file_info_list):
    return file_info_list[1]

for name in file_names:
    with open(name, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        all_data.append([name, len(lines), lines])

all_data.sort(key=get_lines_count)

with open('result.txt', 'w', encoding='utf-8') as out_f:
    for file_info in all_data:
        name, count, content = file_info
        out_f.write(f"{name}\n{count}\n") 
        out_f.writelines(content)
        out_f.write("\n")

print("Файлы в 'result.txt'")

