def read_cookbook():
    with open("cookbook.txt") as f:
        cook_book = {}
        for line in f:
            dish = line.strip()
            num_ingridients = f.readline()
            ingridient_list = []
            for num in range(0,int(num_ingridients)):
                ingridient_dictionary = {}
                ingridient = f.readline()
                ingridient = ingridient.split(' | ')
                ingridient_dictionary['ingridient_name'] = ingridient[0].strip()
                ingridient_dictionary['quantity'] = int(ingridient[1])
                ingridient_dictionary['measure'] = ingridient[2].strip()
                ingridient_list.append(ingridient_dictionary)
            cook_book[dish] = ingridient_list
    return cook_book

def get_shop_list_by_dishes(dishes, person_count):
    cook_book = read_cookbook()
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