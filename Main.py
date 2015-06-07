import sys
import json
import helper
import item_helper


with open('data.json') as f:
    Data = json.load(f)


summonerName = {} #dict with summoner name for keys and participantId for values
game_participants = {}
summonerLanes = {}

for participantIdentity in Data["participantIdentities"]:
    summonerName[participantIdentity["player"]["summonerName"]] = participantIdentity["participantId"]
    node = helper.create_participant_node(participantIdentity["participantId"])
    game_participants[participantIdentity["participantId"]] = node

for participant in Data["participants"]:
    summonerLanes[participant["participantId"]] = participant["timeline"]["lane"]
    game_participants[participant["participantId"]].addLane(participant["timeline"]["lane"])
    game_participants[participant["participantId"]].addTeam(participant["teamId"])
    game_participants[participant["participantId"]].addChampId(participant["championId"])


for participant in game_participants.items():
    for frame in range(1, Data["matchDuration"]/60):
        for event in Data["timeline"]["frames"][frame]["events"]:
            if "participantId" in event and \
                            event["eventType"] != "SKILL_LEVEL_UP" and \
                            event["eventType"] != "ITEM_UNDO" and \
                            event["participantId"] == participant[1].getId():
                #print event["participantId"]

                item_node = helper.Item_at_time_Node(event["itemId"],event["eventType"])
                #if event["participantId"] == game_participants.keys():
                print str(event["participantId"]) + str(participant[0])
                if event["participantId"] == participant[0]:
                    game_participants[event["participantId"]].add_item(item_node,participant[0])
                #print str(event["participantId"]) + " " + item_node.getName()



#print item_helper.get_item_name(1001)
for pt in game_participants.items():
    print pt
#print game_participants[9]