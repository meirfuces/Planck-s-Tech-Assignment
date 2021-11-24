import GetDb
import pandas as pd
import json

data = GetDb.read_file()


def list_category(name_category):
    for category in data:
        if category['categoryName'] == name_category:
            list_of_category = category['dishList']
    df = pd.DataFrame(list_of_category)

    df = df[['dishId','dishName', 'dishDescription','dishPrice']]
    # print(list_of_category)
    return list_of_category


def list_by_id(all_list, iid):
    iid = int(iid)
    for i in all_list:
        if i['dishId'] == iid:
            return i
    return '-1'

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
    drink_list = list_category('Pizzas')
    list_drink = list_by_id(drink_list, iid)
    return get_drop_list(list_drink)


# get dessert with id
def get_desert(iid):
    desert_list = list_category('Desserts')
    list_desert = list_by_id(desert_list, iid)
    return get_drop_list(list_desert)
