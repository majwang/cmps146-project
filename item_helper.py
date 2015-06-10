import sys
import json
import helper

game_item_list = []

with open('item.json') as f:
    Data = json.load(f)


def get_item_cost(item_id):
    return Data["data"][str(item_id)]["gold"]["total"]



def get_item_name(item_id):
    return Data["data"][str(item_id)]["name"]


class Item_Node(object):
    item_cost = 0
    item_id = None
    item_name = None

    def __init__(self, cost, id,name):
        self.item_cost = cost
        self.item_id = id
        self.item_name = name

    def get_item_cost1(self):
        return self.item_cost

    def get_item_name(self):
        return self.item_name
    # def add_item_to_list(self):
    #     for i in range(0, len(game_item_list)):
    #         if self.get_item_cost() > game_item_list[i].get_item_cost(self.item_id):
    #             game_item_list.insert(i+1, self)



def add_item_to_list(node):
    index = 0
    for i in range(0, len(game_item_list)):
        if node.get_item_cost1() > game_item_list[i].get_item_cost1():
            break
        index += 1
    game_item_list.insert(index,node)

for item in Data["data"]:
    if "maps" in Data["data"][item] and  "1" in  Data["data"][item]["maps"] and Data["data"][item]["maps"]["1"] == False:
        continue;
    else:
        new_item_node = Item_Node(Data["data"][item]["gold"]["total"], Data["data"][item]["id"], Data["data"][item]["name"])
        add_item_to_list(new_item_node)
