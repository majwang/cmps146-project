from __future__ import division
import item_heuristic
import item_helper


"""
def find_cost(src_box,dst_box,src_point):
    dst_point = find_point(src_point,dst_box)
    distance = euclidian(src_point, dst_point)
    return distance,dst_point

def a_star_search(start, goal, items):
    frontier = PriorityQueue()
    frontier.put(start, 0)
    came_from = {}
    cost_so_far = {}
    came_from[start] = None
    cost_so_far[start] = 0
    visited = []
    while not frontier.empty():
        current = frontier.get()

        if current == goal:
            break
        nextCells = items[current] #find all the adj boxes
        for next in nextCells:
            cost, temp_point = find_cost(current,next,detail_points[current][0]) #find the cost and point inside
            new_cost = cost_so_far[current] + cost
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                visited.append(next)
                cost_so_far[next] = new_cost
                priority = new_cost + euclidian(dst_point, temp_point)
                frontier.put(next, priority)
                came_from[next] = current


    if current != goal:
        print "No Path Found"
        return [],([],[]),visited
    current = goal
    path = [current]
    while current != start:
        current = came_from[current]
        path.append(current)
    return path,visited

class PriorityQueue:
    def __init__(self):
        self.elements = []

    def empty(self):
        return len(self.elements) == 0

    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))

    def get(self):
        return heapq.heappop(self.elements)[1]"""


def inc_money(start, end):
    return (end.total_gold - start.total_gold)


def custom(start, end, items, event, our_curr_gold):
    when = event["timestamp"] - start.event_time
    change_current_gold = (end.total_gold - start.total_gold)/60000 * when

    """start_gold = our_curr_gold

    if (start_gold + change_current_gold) < item_helper.get_item_cost(event["itemId"]):
        gold_at_purchase = item_helper.get_item_cost(event["itemId"])
    else:"""
    gold_at_purchase = our_curr_gold + change_current_gold

    for item in items:
        if gold_at_purchase < item.item_cost:
            continue
        if gold_at_purchase - item.item_cost < 0:
            continue
        print "At time: " + str(event["timestamp"]/60000) + ", we had: " + str(gold_at_purchase) + ", so we purchased: " + item.item_name + ": costs " + str(item.item_cost) + ", now we have: " + str(gold_at_purchase - item.item_cost)
        print "We actually purchased: " + item_helper.get_item_name(event["itemId"]) + "."
        return gold_at_purchase - item.item_cost

    pass#return items[index]