ROW_TO_CHECK = 2000000

sensors_beacons = {}
with open("ip.txt") as f:
    for line in f:
        line = line.strip().split()
        sensor_x = int(line[2][2:].split(",")[0])
        sensor_y = int(line[3][2:].split(":")[0])
        beacon_x = int(line[-2][2:].split(",")[0])
        beacon_y = int(line[-1][2:])
        sensors_beacons[(sensor_x, sensor_y)] = (beacon_x, beacon_y)


manhattan_distance = lambda p1, p2: abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
beacons = set(sensors_beacons.values())

no_beacons_fo_sure = set()
for sensor in sensors_beacons:
    beacon = sensors_beacons[sensor]
    sensor_distance = manhattan_distance(sensor, beacon)
    sensor_y = sensor[1]

    if ((sensor_y + sensor_distance) >= ROW_TO_CHECK) or ((sensor_y - sensor_distance) <= ROW_TO_CHECK):
        count_positions_in_row_to_check = (sensor_distance - abs((ROW_TO_CHECK - sensor_y)))
        for x in range(sensor[0] - count_positions_in_row_to_check, sensor[0] + count_positions_in_row_to_check + 1):
            if (x, ROW_TO_CHECK) not in beacons:
                no_beacons_fo_sure.add((x, ROW_TO_CHECK))

print(len(no_beacons_fo_sure))

    
                
        