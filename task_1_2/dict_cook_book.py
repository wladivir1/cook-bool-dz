import os
from pprint import pprint


# Задание № 1
def dict_menu(file_menu):
    """ перебирает файл и записывает содержимое файла в словарь """   
    file_path = os.path.join(os.getcwd(), file_menu)
    with open(file_path, 'r', encoding='utf-8') as file:
        cook_book = {}       
        for key_book in file:
            key_name = key_book.strip()            
            count = int(file.readline())
            Ingredients_list = list()
            for item in range(count):
                Ingredients = {}
                ingr = file.readline().strip()
                Ingredients['ingredient_name'], Ingredients['quantity'], Ingredients['measure'] = ingr.split('|')
                Ingredients_list.append(Ingredients)
            file.readline()
            cook_book[key_name] = Ingredients_list
    return cook_book
                          
# Задание № 2
def get_shop_list_by_dishes(dishes, person_count=int):
    """ Считает количество продуктов для приготовления на указанное количечтво персон """
    menu = dict_menu('recipes.txt')    # можно передать имя файла непосредственно в функцию dict_menu
    dict_ingridients = {}   
    for value in dishes:       
        if value in menu:                
            for dict_value in menu[value]:
                dict_count = {}
                key = dict_value['ingredient_name']                                  
                count = int(dict_value['quantity']) * person_count
                weight =  dict_value['measure']
                dict_count['measure'], dict_count['quantity'] = weight, count  
                dict_ingridients[key] = dict_count               
    return dict_ingridients


if __name__ == '__main__':
    print(dict_menu('recipes.txt'))
    print()            
    pprint(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))

   
       
       