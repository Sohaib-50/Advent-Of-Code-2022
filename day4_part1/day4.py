with open("ip.txt", "r") as f:
    intervals = []
    for line in f:
        intervals.append(line.strip())

intervals = [x.split(",") for x in intervals]
ans = 0
for i in range(len(intervals)):
    interval1 = intervals[i][0].split("-")
    interval1 = [int(x) for x in interval1]
    interval2 = intervals[i][1].split("-")
    interval2 = [int(x) for x in interval2]

    if (interval1[0] <= interval2[0]) and (interval1[1] >= interval2[1]):
        ans += 1
    elif (interval2[0] <= interval1[0]) and (interval2[1] >= interval1[1]):
        ans += 1
    # if interval1[0] <= interval2[0]:  # interval1 starts before or same time as interval2
    #     if interval1[1] >= interval2[1]:
    #         print(interval1, interval2, "cond1")
    #         ans += 1 
    # elif interval2[0] <= interval1[0]:
    #      if interval2[1] >= interval1[1]:
    #         print(interval1, interval2, "cond2")
    #         ans += 1


print(ans)