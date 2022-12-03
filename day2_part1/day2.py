with open("ip.txt", "r") as f:
    rounds = []
    for line in f:
        rounds.append(line.strip().split(" "))
    
items_scores = {"A": 1, "B": 2, "C": 3}
items_mapping = {"A": "R", "B": "P", "C": "S"}
score = 0
for round in rounds:
    player1 = round[0]  #  player1 move
    player2 = chr(ord(round[1]) - (ord("X") - ord("A")))  # player2 move (converted from X, Y, Z to A, B, C)
    score  += items_scores[player2]

    if player1 == player2:  # draw
        score += 3
    else:
        # player1 wins
        if (
            items_mapping[player1] == "R" and items_mapping[player2] == "S" 
            or 
            items_mapping[player1] == "P" and items_mapping[player2] == "R" 
            or
            items_mapping[player1] == "S" and items_mapping[player2] == "P"
        ):
            score += 0

        # player2 wins
        else:
            score += 6

print(score)