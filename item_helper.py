import sys
import json
import helper

with open('item.json') as f:
    Data = json.load(f)


def get_item_cost(item_id):
    return Data["data"][str(item_id)]["gold"]["total"]



def get_item_name(item_id):
    return Data["data"][str(item_id)]["name"]






