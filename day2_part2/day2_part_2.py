with open("ip.txt", "r") as f:
    rounds = []
    for line in f:
        rounds.append(line.strip().split(" "))
    
items_scores = {"A": 1, "B": 2, "C": 3}
items_mapping = {"A": "R", "B": "P", "C": "S"}
score = 0
for round in rounds:
    player1 = round[0]  #  player1's item
    round_result = round[1]

    # need to end round in a draw
    if round_result == "Y":  
        score += items_scores[player1] + 3  # score of same item as player1 plus score of draw

    # need to lose round
    elif round_result == "X":
        if player1 == "A":
            player2 = "C"
        elif player1 == "B":
            player2 = "A"
        else:
            player2 = "B"
        score += items_scores[player2] + 0  # score of player1 item plus score of loss

    # need to win round
    else:
        if player1 == "A":
            player2 = "B"
        elif player1 == "B":
            player2 = "C"
        else:
            player2 = "A"
        score += items_scores[player2] + 6  # score of player1 item plus score of loss


print(score)