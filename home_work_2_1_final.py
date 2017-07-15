def split_on(lst, delimiter = ''):
    splitted = [[]]
    for item in lst:
        if item == delimiter:
            splitted.append([])
        else:
            splitted[-1].append(item)
    return splitted

with open('cookbook.txt') as f:
      array = [row.strip() for row in f]
      array = split_on(array)
      cook_book = {}
      for dish in array:
        name = dish[0]
        cook_book[name] = None
        num_ingridients = int(dish[1])
        ingridient_list = []
        cookbook_ingridients_list = []
        for ing in range(2,num_ingridients+2):
          ingridient = dish[ing]
          ingridient_list.append(ingridient)
        cookbook_ingridients_new_list = []
        for ingridient1 in ingridient_list:
          ingridient1 = ingridient1.split(' | ')
          cookbook_ingridients_new_list.append(ingridient1)
        cookbook_list = []
        for ingridient in cookbook_ingridients_new_list:
          ingridient_dictionary = {}
          ingridient_dictionary.update({'ingridient_name': ingridient[0]})
          ingridient_dictionary.update({'quantity': int(ingridient[1])})
          ingridient_dictionary.update({'measure': ingridient[2]})
          cookbook_list.append(ingridient_dictionary)
          cook_book[name] = cookbook_list


def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        for ingridient in cook_book[dish]:
            new_shop_list_item = dict(ingridient)
            new_shop_list_item['quantity'] *= person_count
            if new_shop_list_item['ingridient_name'] not in shop_list:
                shop_list[new_shop_list_item['ingridient_name']] = new_shop_list_item
            else:
                shop_list[new_shop_list_item['ingridient_name']]['quantity'] += new_shop_list_item['quantity']
    return shop_list

def print_shop_list(shop_list):
    for shop_list_item in shop_list.values():
        print('{ingridient_name} {quantity} {measure}'.format(**shop_list_item))

def create_shop_list():
    dishes = input('введите блюда через запятую:').lower().split(',')
    person_count = int(input('Введите количество человек:'))
    shop_list = get_shop_list_by_dishes(dishes, person_count)
    print_shop_list(shop_list)

create_shop_list()