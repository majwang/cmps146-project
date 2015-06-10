import sys
import json
import helper
import item_helper
import item_heuristic


with open('data.json') as f:
    Data = json.load(f)


summonerName = {} #dict with summoner name for keys and participantId for values
game_participants = {} #dict of node objects using partcipantID for keys



for participantIdentity in Data["participantIdentities"]:
    summonerName[participantIdentity["player"]["summonerName"]] = participantIdentity["participantId"]
    node = helper.create_participant_node(participantIdentity["participantId"])
    game_participants[participantIdentity["participantId"]] = node

for participant in Data["participants"]:

    game_participants[participant["participantId"]].addLane(participant["timeline"]["lane"])
    game_participants[participant["participantId"]].addTeam(participant["teamId"])
    game_participants[participant["participantId"]].addChampId(participant["championId"])
    game_participants[participant["participantId"]].addRole(participant["timeline"]["role"])

#for pt in game_participants.items():
#    print pt



userid = None
while userid is None:
    filename = raw_input('Enter your summoner name: ')
    if summonerName.has_key(filename):
        userid = summonerName[filename]
        #print(str(userid))
    else:
        print("User Not Found")






for frame in range(0,Data["matchDuration"]/60):
    timestamp = Data["timeline"]["frames"][frame]["timestamp"]
    for pframe in Data["timeline"]["frames"][frame]["participantFrames"].values():
        if "participantId" in pframe and pframe["participantId"] != 0 :
            heuristic_node = helper.H_Node(timestamp, pframe["currentGold"], pframe["totalGold"] )
            game_participants[pframe["participantId"]].add_hitem(heuristic_node)



our_curr_gold = 0
our_curr_gold_flag = True


for frame in range(1,Data["matchDuration"]/60):
    start = None
    end = None
    frame_flag = False
    for event in Data["timeline"]["frames"][frame]["events"]:
        if "participantId" in event and event["participantId"] != 0 :
            if event["eventType"] != "SKILL_LEVEL_UP" and event["eventType"] != "ITEM_UNDO" and event["eventType"] != "ITEM_SOLD":
                item_node = helper.Item_at_time_Node(event["itemId"],event["eventType"])
                game_participants[event["participantId"]].add_item(item_node)
                start = game_participants[event["participantId"]].get_frame_list()[frame-1]
                end = game_participants[event["participantId"]].get_frame_list()[frame]

                if event["participantId"] == userid:
                    if not frame_flag:
                        frame_flag = True
                    if our_curr_gold_flag:
                        our_curr_gold = start.current_gold
                        our_curr_gold_flag = False
                    our_curr_gold = item_heuristic.custom(start, end, item_helper.game_item_list, event, our_curr_gold)
                    print " "

    if not frame_flag:
        our_curr_gold += item_heuristic.inc_money(start, end)
        frame_flag = False



#for pt in game_participants.items():
#    print pt[1]

userlane = game_participants[userid].getLane()
userteam = game_participants[userid].getTeam()
userrole = game_participants[userid].getRole()

if userlane == 'BOTTOM':
    userlane = userrole

print("Your Lane = " + userlane, "Your Team = " + str(userteam), "Your Role = " + str(userlane))

#loop to check enemy role's info
for pt in game_participants.items():
    #print(userlane, pt[1].getLane())
    if pt[1].getLane() == 'BOTTOM':
        enemylane = pt[1].getRole()
    else:
        enemylane = pt[1].getLane()
    if pt[1].getTeam() != userteam and enemylane == userlane:
        print(str(pt[1].getChampId()))


#print game_participants[9]