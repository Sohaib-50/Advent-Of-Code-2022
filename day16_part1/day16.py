import random


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

minutes = 1
opened_valves = set()
pressure = 0
total_flow = 0
current_valve = "AA"
visited_valves = set()
while minutes < 30:
    print(f"Minute: {minutes}, opened_valves: {opened_valves}, currently at: {current_valve}, pressure: {pressure}")
    visited_valves.add(current_valve)

    # if valve isn't already opened and flow rate is not 0, open the valve
    if (current_valve not in opened_valves) and (flow_rates[current_valve] > 0):

        # open valve
        pressure += (30 - minutes) * flow_rates[current_valve]
        minutes += 1
        opened_valves.add(current_valve)
        continue


    # find out  the place where valve isn't opened and has maximum flow rate
    connected_valves = {v for v in valves_system[current_valve] if v not in opened_valves}
    max_valve = None
    max_connected_valve_flow = float('-inf')
    for connected_valve in connected_valves:

        if flow_rates[connected_valve] > max_connected_valve_flow:
            max_valve = connected_valve
            max_connected_valve_flow = flow_rates[connected_valve]


    # find connected valves which are not visited
    unvisited_connected_valves = {v for v in valves_system[current_valve] if v not in visited_valves}

    minutes += 1
    # if there are no unvisited connected valves and there is no valve with maximum flow rate, then go to any of the connected valves
    if not unvisited_connected_valves and not max_valve:
        current_valve = random.choice(list(connected_valves))
        continue
    
    # if there are no unvisited connected valves, then go to the valve with maximum flow rate
    if not unvisited_connected_valves:
        current_valve = max_valve
        continue

    # if there are unvisited connected valves, then go to one of them randomly
    current_valve = random.choice(list(unvisited_connected_valves))

    






   
    current_valve = max_valve
    minutes += 1

print(pressure)
print(valves_system)

    
