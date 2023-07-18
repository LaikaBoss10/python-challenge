# Module for creating file paths
import os
# Module for reading CSV files
import csv

#make path variable to direct the csv open
electiondata_csvpath = os.path.join("Resources", "election_data.csv")

#List of Dictionary to store data
VotingData = {}
candidateList=[]

#open the budget csv
with open(electiondata_csvpath) as election_csv:
    #read the budget csv
    csvreader = csv.reader(election_csv,delimiter=',')

    #skip csv header
    csv_header = next(csvreader)


    #for loop iterates through the rows of the election csv. The for loop overall fills the dictionary with Candidate keys, and corresponding lists of all the ballot ids under that candidate
    for row in csvreader:
        #checks if the candidate is not in the voting data dictionary, if its not in it adds the candidate as a key and fills the value with an empty list
        if row[2] not in VotingData:
            VotingData.update({row[2]:[]})
        #appends the Ballot ID to the list in the dictionary; corresponding to the key of the specific candidate in the csv row.
        VotingData[row[2]].append(row[0])
        
#makes a list of the candidates
candidateList = (list(VotingData.keys()))

#first makes a new variable called total votes and sets it equal to zero. Uses for loop and dictionary keys to find the length of the lists of ballots for each candidate and sum to get total ballots (total votes)
TotalVotes = 0
for candidate in candidateList:
    TotalVotes = TotalVotes + len(VotingData[candidate])
    


#set path and name of output txt file
output_path = os.path.join("analysis", "PyPoll_Output.txt")

#open output text file
with open(output_path, 'w') as txtfile:
    #Prints and writes Total Votes in desired format
    print(f'Election Results\n\n-------------------------\n\nTotal Votes: {TotalVotes}\n\n-------------------------\n')
    txtfile.write(f'Election Results\n\n-------------------------\n\nTotal Votes: {TotalVotes}\n\n-------------------------\n\n')

    #Sets new variable VoteMax equal to zero. This variable is used to find the candidate with the max number of votes
    VoteMax=0
    #loops through each candidate. Gets number of votes from length of ballot ids under each candidate. 
    # Calculates Percentage by dividing by total votes. Prints and writes output in Desired format.
    for candidate in candidateList:
        candidateVotes = len(VotingData[candidate])
        #if statement keeps updates when a candidates number of votes is greater than vote max. The statement will find the candidate with the greatest number of votes, and vote max will be equal to their number of votes.
        if candidateVotes > VoteMax:
            VoteMax = candidateVotes
            Winner = candidate
        candidatePercentage = 100*candidateVotes/TotalVotes
        print(f'{candidate}: {candidatePercentage:.3f}% ({candidateVotes})\n')
        txtfile.write(f'{candidate}: {candidatePercentage:.3f}% ({candidateVotes})\n\n')

    #prints and writes the winner of the election in the desired format
    print(f'-------------------------\n\nWinner: {Winner}\n\n-------------------------')
    txtfile.write(f'-------------------------\n\nWinner: {Winner}\n\n-------------------------')