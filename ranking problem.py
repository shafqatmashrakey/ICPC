#https://open.kattis.com/problems/rankproblem
teams= int(input("Enter the number of teams: "))
matches = int(input("Enter the number of matches: "))
print("This is the team list")
team_list = []
for i in range(teams):
    print("T" + str(i + 1))
    team_list.append(i + 1)

#print(team_list)
print("Now give the prediction")

prediction = []
for j in range(matches):
    winner = input("Enter the winner team number.ex(T1..):")
    loser = input("Enter the loser team number.ex(T4..): ")

    # Extract the team numbers from the strings
    winner_num = int(winner[1:])
    loser_num = int(loser[1:])

    prediction.append((winner_num, loser_num))

print("Predictions:", prediction)
# Initialize rank list with team numbers
rank = team_list.copy()

# Process predictions to update rank
for winner, loser in prediction:
    if winner in rank and loser in rank:
        winner_index = rank.index(winner)
        loser_index = rank.index(loser)
        
        if winner_index > loser_index:
            # Remove and reinsert loser next to winner
            rank.remove(loser)
            rank.insert(winner_index, loser)

print("Ranked Teams: ", ["T" + str(team) for team in rank])