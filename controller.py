import GetDb
import pandas as pd
import json

data = GetDb.read_file()


# The function get name of category relevant
# with pandas libary take only the column
# return data frame of the relevant column of the category
def list_category(name_category):
    for category in data:
        if category['categoryName'] == name_category:
            list_of_category = category['dishList']
    df = pd.DataFrame(list_of_category)

    df = df[['dishId','dishName', 'dishDescription','dishPrice']]
    # print(list_of_category)
    return list_of_category


# The function get all list of the category and id
# search the id in the category
# return the item
def list_by_id(all_list, iid):
    iid = int(iid)
    for i in all_list:
        if i['dishId'] == iid:
            return i
    return '-1'


# get data frame and return json after drop id column
def parse_get_all(df):
    df = pd.DataFrame(df)
    df = df[['dishName', 'dishDescription', 'dishPrice']]
    result = df.to_json(orient="values")
    parsed = json.loads(result)
    return parsed

# All drinks
def get_drinks():
    drink_list = list_category('Drinks')
    return parse_get_all(drink_list)


# All pizzas
def get_pizzas():
    pizzas_list = list_category('Pizzas')
    return parse_get_all(pizzas_list)


# All Deserts

def get_desserts():
    desserts_list = list_category('Desserts')
    return parse_get_all(desserts_list)


# Help Function for drop colum
def get_drop_list(l):
    if l != -1:
        return l['dishName'], l['dishDescription'], l['dishPrice']
    return 'not found'


# get drink with id
def get_drink(iid):
    drink_list = list_category('Drinks')
    list_drink = list_by_id(drink_list, iid)
    return get_drop_list(list_drink)


# get pizza with id
def get_pizza(iid):
    pizzas_list = list_category('Pizzas')
    list_pizza= list_by_id(pizzas_list, iid)
    return get_drop_list(list_pizza)


# get dessert with id
def get_desert(iid):
    desert_list = list_category('Desserts')
    list_desert = list_by_id(desert_list, iid)
    return get_drop_list(list_desert)


# The function get the json and the name of the category
# search the list of the category
# calculate the sum of each category and return it
def price_by_category(json_file,category_name):
    sum_price=0
    category = json_file[category_name]
    for iid in category:
        if category_name=='drinks':
            category_type = get_drink(iid)
        if category_name == 'pizzas':
            category_type = get_pizza(iid)
        if category_name == 'desserts':
            category_type = get_desert(iid)
        sum_price += int(category_type[2])
    return sum_price


def price(json_file):
    sum_price = 0
    sum_price+=price_by_category(json_file, 'drinks')
    sum_price += price_by_category(json_file, 'pizzas')
    sum_price += price_by_category(json_file, 'desserts')

    return sum_price

