import os
import csv

#set input and output path
input_path = r'C:\Users\kamrk\RutgersDataScience\RUTJER201809DATA3\03-Python\Homework\Instructions\PyPoll\Resources\election_data.csv'
output_path = ('Python-Challenge','PyPoll')

#Declare Variables
TotalVotes = 0
CandidateList = []
CandidateVote = {}
WinningCandidate = ""
WinningVotes = 0
Vote_Output = ""


#Open and Read CSV
with open(input_path, newline = '') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter = ',')

    #read header row
    csv_header = next(csvfile)

    #Loop through CSV
    for row in csv_reader:

        #Calculate Total Votes
        TotalVotes += 1

        #Create List of Candidates
        if row[2] not in CandidateList:
            CandidateList.append(row[2])

            #Begin Counting Votes For Candidate
            CandidateVote[row[2]] = 0

        #Add Votes To Candidate
        CandidateVote[row[2]] += 1

    #Determine Winner By Looping Through Votes
    for Candidate in CandidateVote:
        votes = CandidateVote.get(Candidate)

        #Get Vote Percentage
        Vote_Pct = (float(votes) / float(TotalVotes)) * 100

        #Get Winning Votes
        if votes >= WinningVotes:
            WinningVotes = votes
            WinningCandidate = Candidate


        #Output For Votes
        Vote_Output += f"{Candidate}: {Vote_Pct: .3f}% ({votes})\n"
        


    #Final Output
    output = (
    f"ELECTION RESULTS\n"
    f"-----------------------\n"
    f"Total Votes: {TotalVotes}\n" 
    f"------------------------\n"
    f"{Vote_Output}\n"
    f"--------------------------\n"
    f"Winning Candidate: {WinningCandidate}\n")

    print(output)


#Export To Txt File
with open('PyPollResults.txt','w') as txt_file:
    txt_file.write(output)







     

           

        



        


