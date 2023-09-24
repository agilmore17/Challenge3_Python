#modules
import os
import csv

#setup read file path for data, must start in PyPoll folder
pypoll_csv = os.path.join('Resources', 'election_data.csv')

#setup arrays
ballot_id = []
county = []
candidate = []


#open the file & store it as a list
with open(pypoll_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ",")
    csv_header = next(csv_reader)
    for row in csv_reader:
        ballot_id.append(row[0])
        county.append(row[1])
        candidate.append(row[2])

#formatting
print("Election Results")
print("___________________________________________")
print("")


#find length

total_votes = str(len(ballot_id))

print("Total Votes: " + total_votes)

#formatting
print("___________________________________________")
print("")

#total votes Charles

int_votes = len(ballot_id)

charles_count = int((candidate.count(("Charles Casper Stockham"))))

charles_percent = (round(charles_count/int_votes * 100, 3))

print(f"Charles Casper Stockham:  {charles_percent}%  ({charles_count}) ")


#total votes Diana

diana_count = int(candidate.count("Diana DeGette"))

diana_percent = (round(diana_count/ int_votes * 100, 3))

print(f"Diana DeGette: {diana_percent}% ({diana_count})")

#total votes Anthony

raymon_count = candidate.count("Raymon Anthony Doane")

raymon_percent = (round(raymon_count/int_votes * 100, 3))

print(f"Raymon Anthony Doane: {raymon_percent}% ({raymon_count})")

#formatting
print("___________________________________________")
print("")

#winner based on popular vote
total_votes_list = [charles_count, diana_count, raymon_count]
mostvotes = max(total_votes_list)

if mostvotes == charles_count:
    winner = "Charles Casper Stockham"
elif mostvotes == diana_count:
    winner = "Diana DeGette"
elif mostvotes == raymon_count:
    winner = "Raymon Anthony Doane"

print("Winner: " + winner)


#write to text file in current library


with open ('PyPoll Solution', 'w') as txtfile:
   txtfile.write("Election Results")
   txtfile.write("\n___________________________________________\n")
   txtfile.write("\nTotal Votes: " + total_votes)
   txtfile.write("\n___________________________________________\n")
   txtfile.write(f"\nCharles Casper Stockham:  {charles_percent}%  ({charles_count}) ")
   txtfile.write(f"\nDiana DeGette: {diana_percent}% ({diana_count})")
   txtfile.write(f"\nRaymon Anthony Doane: {raymon_percent}% ({raymon_count})")
   txtfile.write("\n___________________________________________\n")
   txtfile.write("\nWinner: " + winner)
   txtfile.write("\n___________________________________________")

