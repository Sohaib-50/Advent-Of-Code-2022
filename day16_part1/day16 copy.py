import random

MAX_MINS = 30

valves_system = {}
flow_rates = {}
with open("ip.txt") as f:
    for line in f:
        valve = ((line[line.find("Valve") + len("Valve") + 1 : line.find("has")]).strip())
        connected_valves = (line[line.find("valve") + len("valve") + 1 : ].strip().split(","))
        connected_valves = {v.strip() for v in connected_valves}
        flow_rate = line[line.find("flow rate=") + len("flow rate="): line.find(";")]
        valves_system[valve] = connected_valves
        flow_rates[valve]  = int(flow_rate)

# def get_pressure_dfs(current_valve, opened_valves, minutes_passed, current_pressure):
#     if minutes_passed == 30:
#         return current_pressure
    
#     # open the current valve only if it is not opened and flow rate is not 0
#     if (current_valve not in opened_valves) and (flow_rates[current_valve] > 0):
#         current_pressure += (30 - minutes_passed) * flow_rates[current_valve]
#         minutes_passed += 1
#         opened_valves.add(current_valve)
    
#     # expand the current valve, visit all the connected valves
#     connected_valves = {v for v in valves_system[current_valve] if v not in opened_valves}
#     max_pressure = float('-inf')
#     for connected_valve in connected_valves:
#         max_pressure = max(max_pressure, get_pressure_dfs(connected_valve, opened_valves, minutes_passed + 1, current_pressure))

#     return max_pressure

def get_pressure_bfs(valves_system, flow_rates, start_valve):
    queue = [(start_valve, 0, set(), 0)]  # (valve, minutes_passed, opened_valves, current_pressure)
    max_pressure = float('-inf')
    memo = {}
    
    while queue:
        current_valve, minutes_passed, opened_valves, current_pressure = queue.pop(0)
        if (current_valve, minutes_passed) in memo:
            continue
        
        if minutes_passed == MAX_MINS:
            max_pressure = max(max_pressure, current_pressure)
            continue

        # prune the search space
        if current_pressure < max_pressure:
            continue
        # find if current pressure is less than any of the other pressures in the queue
        # if yes, then prune the search space
        for valve, mins, opened, pressure in queue:
            if current_pressure > pressure and mins > minutes_passed:
                queue.remove((valve, mins, opened, pressure))
            elif current_pressure < pressure and mins < minutes_passed:
                continue
        if minutes_passed == MAX_MINS/4 and current_pressure < 200:
            continue


        # open the current valve only if it is not opened and flow rate is not 0
        if (current_valve not in opened_valves) and (flow_rates[current_valve] > 0):
            current_pressure += (30 - minutes_passed) * flow_rates[current_valve]
            minutes_passed += 1
            opened_valves.add(current_valve)
        
        # expand the current valve, visit all the connected valves
        connected_valves = {v for v in valves_system[current_valve]}
        for connected_valve in connected_valves:
            queue.append((connected_valve, minutes_passed + 1, opened_valves, current_pressure))
        
        print(max_pressure, minutes_passed, current_valve, current_pressure)
    
    return max_pressure

    
def max_flow(valves, path, minutes_left):
    if minutes_left < 1:
        return 0
    current_node = path[-1]

    candidates = []
    for neighbour in valves_system[current_node]:
        if neighbour not in path:
            path.append(neighbour)
            # Case 2.1
            candidates.append(
                valves[flow_rates[current_node] * (minutes_left-1)    # The flow starts from next minute
                + max_flow(valve_list, path, minutes_left-2)  # We move after two minutes
            )
            # Case 2.2
            candidates.append(max_flow(valves, path, minutes_left - 1))
            path.pop()
    if not candidates:
        return 0
    return max(candidates)

minutes_passed = 1
opened_valves = set()
pressure = 0
total_flow = 0
current_valve = "AA"
visited_valves = set()
max_pressure = get_pressure_bfs(valves_system, flow_rates, current_valve)
print(max_pressure)