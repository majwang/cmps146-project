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

class H_Node(object):
    current_gold = 0
    total_gold = 0
    event_time = 0

    def __init__(self, time, currentGold, totalGold):
        self.current_gold = currentGold
        self.total_gold = totalGold
        self.event_time = time

    def getCurrentGold(self):
        return self.current_gold

    def getTotalGold(self):
        return self.total_gold

    def getEventTime(self):
        return self.event_time


class Node(object):
    p_id = None
    lane = None
    team = None
    championId = None
    item_event = []
    role = None
    purchased_events = []

    def __init__(self, id,item_event = None, purchased_events = None):
        self.p_id = id
        if item_event is None:
            self.item_event = []
            self.purchased_events = []
        else:
            self.item_event = item_event
            self.purchased_events = purchased_events

    def getId(self):
        return self.p_id

    def getLane(self):
        return self.lane

    def addLane(self, lane):
        self.lane = lane

    def addTeam(self, team):
        self.team = team

    def addRole(self, role):
        self.role = role

    def getRole(self):
        return self.role

    def addChampId(self, id):
        self.championId = id

    def getChampId(self):
        return self.championId

    def add_item(self,node):
        #if id == self.p_id:
        self.item_event.append(node)

    def add_hitem(self, H_Node):
        self.purchased_events.append(H_Node)

    def getTeam(self):
        return self.team

    def getlist(self):
        return self.item_event

    def get_frame_list(self):
        return self.purchased_events

    #def accept_item(self,item_id):



    def __str__(self):
        myreturn = str(self.p_id) + ", " + str(self.lane) + ", " + str(self.team) + ", " + str(self.championId) + ", " #+ str(self.item_event)
        #myreturn = ''
        # for item in self.item_event:
        #    myreturn += str(item.getName())
        #    myreturn += ' '
        for item in self.purchased_events:
            myreturn += str(item.getTotalGold())
            myreturn += ' '
        print ""
        return myreturn

def create_participant_node(participantId):
    participant_node = Node(participantId)
    return participant_node


