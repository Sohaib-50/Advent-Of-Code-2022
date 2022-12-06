with open("ip.txt", "r") as f:
    data_stream = f.readline().strip()

start = 0
chars = list()
chars.append(data_stream[0])
for end in range(1, len(data_stream)):
    chars.append(data_stream[end])
    if ((end - start) + 1) == 4:  # 4 len window made
        if len(set(chars)) == len(chars):  # all in window unique
            print(end + 1)
            exit()
        start += 1
        chars.pop(0)
    