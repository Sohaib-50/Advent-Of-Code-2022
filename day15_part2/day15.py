LIMIT = 4000000

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

x = 0
y = 0
while (x <= LIMIT) and (y <= LIMIT):
    # print(y)
    current_point = (x, y)
    
    # find the closest sensor
    for sensor in sensors_beacons:
        current_pt_sensor_distance = manhattan_distance(current_point, sensor) 
        sensor_beacon_distance = manhattan_distance(sensor, sensors_beacons[sensor])
        
        if sensor_beacon_distance >= current_pt_sensor_distance:
            sensor_y = sensor[1]
            positions_covered_in_row = (sensor_beacon_distance - abs((y - sensor_y)))
            x = sensor[0] + positions_covered_in_row + 1
            break
    else:
        print(x, y, "FIN")
        print((x * 4000000) + y)
        exit()

    if x >= LIMIT:
        x = 0
        y += 1
    

print(x, y)
