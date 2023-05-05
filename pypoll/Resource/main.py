import csv
with open('election_data.csv','r') as csvfile:
    reader = csv.reader(csvfile)
    total_vote = 0
    charles_casper_stockham_vote = 0
    diana_degette_vote = 0
    raymon_anthony_vote = 0
    next(reader)
    for row in reader:
        total_vote = total_vote + 1
        if row[2]== "Charles Casper Stockham":
            charles_casper_stockham_vote = charles_casper_stockham_vote + 1
        elif row[2]== "Diana DeGette":
            diana_degette_vote = diana_degette_vote + 1
        elif row[2]== "Raymon Anthony Doane":
            raymon_anthony_vote = raymon_anthony_vote + 1
    percentage_votes_for_charles = charles_casper_stockham_vote/total_vote*100
    percentage_vote_for_diana_degette = diana_degette_vote/total_vote*100
    percentage_vote_for_raymon_anthony = raymon_anthony_vote/total_vote*100
    candidates = [charles_casper_stockham_vote, diana_degette_vote,raymon_anthony_vote]
    candidates = {
      "candidate1":
        {
            "name": "Charles Casper Stockham",
            "votes": charles_casper_stockham_vote,
        },
      "candidate2":
        {
            "name": "Diana DeGette",
            "votes": diana_degette_vote
          
        },
      "candidate3":
        {
            "name": "Raymon Anthony Doanne",
            "votes": raymon_anthony_vote

        }
    }
    winner = 0
    winner_name = ""
    for vote in candidates:
        if candidates[vote]["votes"] > winner:
            winner_name = (candidates[vote]["name"])
            winner = candidates[vote]["votes"]

print(f'Election Results')
print(f'------------------------------------')
print(f'Total votes: {total_vote}')
print(f'------------------------------------')
print(f'Charles Casper Stockham: {percentage_votes_for_charles:.3f}% ({charles_casper_stockham_vote})')
print(f'Diana Degette: {percentage_vote_for_diana_degette:.3f}% ({diana_degette_vote})')
print(f'Raymon Anthony: {percentage_vote_for_raymon_anthony:.3f}% ({raymon_anthony_vote})')
print(f'Winner: {winner_name}')
print(f'------------------------------------')

with open("election_data.txt", "w") as file:
    file.write(f'Election Results\n')
    file.write('-------------------------------------\n')
    file.write(f"Total votes: {total_vote}\n")
    file.write('-------------------------------------\n')
    file.write(f"Charles Casper Stockham: {percentage_votes_for_charles:.3f}% ({charles_casper_stockham_vote})\n")
    file.write(f"Diana Degette: {percentage_vote_for_diana_degette:.3f})% ({diana_degette_vote})\n")
    file.write(f'Raymon Anthony: {percentage_vote_for_raymon_anthony:.3f} ({raymon_anthony_vote})\n')
    file.write(f'Winner: {winner_name}\n')
    file.write(f'-------------------------------------\n')