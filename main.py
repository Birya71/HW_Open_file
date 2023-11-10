import os
def read_file():
    cook_book = {}
    with open('C:/recepies/recept.txt', 'r', encoding='utf-8') as file:
        line = [row.strip() for row in file]
        index = 0
        while index < len(line):
            if line[index].isdigit():
                number_ing = 0
                massiv_ingridients = []
                while number_ing < int(line[index]):
                    ingridients = line[index + number_ing + 1].split('|')
                    data_ingridients = {
                            'ingredient_name': ingridients[0],
                            'quantity': int(ingridients[1].strip()),
                            'measure': ingridients[2].strip()
                        }
                    massiv_ingridients.append(data_ingridients)
                    number_ing += 1
                cook_book.update({line[index - 1]: massiv_ingridients})
            index += 1
    return cook_book

def get_shop_list_by_dishes(dishes, person_count, book):
    ingr_list = dict()
    for dish_name in dishes:
        if dish_name in book:
            for ings in book[dish_name]:
                meas_quan_list = dict()
                if ings['ingredient_name'] not in ingr_list:
                    meas_quan_list['measure'] = ings['measure']
                    meas_quan_list['quantity'] = ings['quantity'] * person_count
                    ingr_list[ings['ingredient_name']] = meas_quan_list
                else:
                    ingr_list[ings['ingredient_name']]['quantity'] = ingr_list[ings['ingredient_name']]['quantity'] + \
                                                                     ings['quantity'] * person_count
        else:
            print('Нет такого блюда')
    return ingr_list
# book = read_file()
# data = get_shop_list_by_dishes(['Омлет', 'Запеченный картофель'], 2, book)
# print(data)
def read_files_in_dir(path):
    # directory = os.listdir('C:\etology_hw')
    directory = os.listdir(path)
    data = {}
    for file in directory:
        # получаем путь к каждому файлу для открытия
        file_path = os.path.join(os.path.dirname(__file__), file)
        # print(file_path)
        with open(file_path, 'r', encoding='utf-8') as f:
            # Чтение содержимого файла
            content = f.read()
            data[file_path] = content
            sorted_data = dict(sorted(data.items(), key=lambda item: len(item[1]), reverse=False))
            # print(content)
    return sorted_data

def write_file(dict_data):
    direct = "C:\etology_hw"
    new_file = os.path.join(direct, 'data.txt')
    print(new_file)
    with open(new_file, 'w') as f:
        for key, value in data_homework.items():
            f.write(key + ' ' + str(len(value)) + '\n' + ' ' + value + '\n')

path = "C:\etology_hw"
data_homework = read_files_in_dir(path)
# print(data_homework)
write_file(data_homework)







