

import requests
import json


url ="https://www.10bis.co.il/NextApi/GetRestaurantMenu?culture=en&uiCulture=en&restaurantId=19156&deliveryMethod=pickup "


def update_data():
    print('update')
    response = requests.get(url)
    all_data_json = response.json()
    menu_data = all_data_json['Data']
    menu_data_categories = menu_data['categoriesList']
    with open('data.json', 'w') as f:
        json.dump(menu_data_categories, f)

def read_file():
    with open('data.json') as f:
        data_file = json.load(f)
    print('finish to read')
    return data_file

