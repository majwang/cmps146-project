import item_helper


class Item_at_time_Node(object):
    item_id = None
    item_cost = None
    item_name = None
    event_type = None
    curr_gold = None


    def __init__(self,item_id,event_type):
        self.item_id = item_id
        self.event_type = event_type

        self.item_cost = item_helper.get_item_cost(item_id)
        self.item_name = item_helper.get_item_name(item_id)

    def getId(self):
        return self.item_id

    def getName(self):
        return self.item_name



class Node(object):
    p_id = None
    lane = None
    team = None
    championId = None
    item_event = []

    def __init__(self, id):
        self.p_id = id

    def getId(self):
        return self.p_id

    def getLane(self):
        return self.lane

    def addLane(self, lane):
        self.lane = lane

    def addTeam(self, team):
        self.team = team

    def addChampId(self, id):
        self.championId = id

    def add_item(self,node,id):
        if id == self.p_id:
            self.item_event.append(node)

    #def accept_item(self,item_id):




    def __str__(self):
        myreturn = str(self.p_id) + ", " + str(self.lane) + ", " + str(self.team) + ", " + str(self.championId)
        #myreturn = ''
        for item in self.item_event:
           myreturn += str(item.getName())
           myreturn += ' '

        print ""
        return myreturn

def create_participant_node(participantId):
    participant_node = Node(participantId)
    return participant_node


