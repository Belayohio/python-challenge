import os
import csv

#  step 1:file path
poll_file =os.path.join("..","Resources","election_data.csv")
with open(poll_file) as file_election:
    csv_election=csv.reader(file_election)
    #skip the header
    header=next(csv_election)
    #let's set intial value of the vote before it counted.
    vote=0
    #intial list of the vote_casted and candidate.and non duplicated list of participant
    vote_casted=[]
    list_of_candidate=[]
   
    # step 2:  now lets separate the list of vote casted and candidate out of the csv_election list.
    for row in csv_election:
        vote_casted.append(row[0])
        list_of_candidate.append(row[2])
        
        # step 3: to find number of total vote count. we can count vote_casted .
    for i in vote_casted:
            vote+=1
            if i==len(vote_casted):
                break
    print(f"Total Vote: {vote}")

    #step 4: we need to create variable to hold the non duplicate of the candidate. let
    completed_list=[] # intial value for list of the participant(number of the participant)
    for i in list_of_candidate:
            
            if i not in completed_list:
                completed_list.append(i)
               
    print("list of participant: "+ str(completed_list)) # now we have our list of participant
    #once it print our candidate looks like below.Note:i manualy put it for vizualize to help in next step.
   # completed_list=['Charles Casper Stockham', 'Diana DeGette', 'Raymon Anthony Doane']
 #step 5: to get total count for each candidate.
    for c in range(len(list_of_candidate)):
              if c==completed_list[0]:
                    list_of_candidate.count(completed_list[0]) # to find the total count of the first participant in thhe list.
              if c==completed_list[1]:
                    list_of_candidate.count(completed_list[1])
              if c==completed_list[2]:
                    list_of_candidate.count(completed_list[2])
    # step 6: to find the percentage of the each candidate: count of each candidate-vote divided by total count times 100
    print(f"{completed_list[0]}:{round((list_of_candidate.count(completed_list[0]))/vote*100,3)}% ({list_of_candidate.count(completed_list[0])})")
    print(f"{completed_list[1]}:{round((list_of_candidate.count(completed_list[1]))/vote*100,3)}% ({list_of_candidate.count(completed_list[1])})")
    print(F"{completed_list[2]}:{round(list_of_candidate.count(completed_list[2])/vote*100,3)}% ({list_of_candidate.count(completed_list[2])})")

     #step 7:# to get the winner of the election.we need to create variable that can hold counted vote.intial value from complete_list.
    participant=[]
    for r in completed_list:
         participant.append(list_of_candidate.count(completed_list[0]))
         participant.append(list_of_candidate.count(completed_list[1]))
         participant.append(list_of_candidate.count(completed_list[2]))
         break
    print(participant)
   #step 8: to find the name of the winner.
    for w in range(len(participant)):
         max_vote_count = participant[0]
         if participant[w]> max_vote_count:
          max_vote_count=participant[w]
          winner=completed_list[w]
          print("winner: " + str(winner))

         
    #step 9:write text file of the report.let minimize it
election_output=(f"\nTotal Vote: {vote}\n" f"{completed_list[0]}:{round((list_of_candidate.count(completed_list[0]))/vote*100,3)}% ({list_of_candidate.count(completed_list[0])})\n"
                 f"{completed_list[1]}:{round((list_of_candidate.count(completed_list[1]))/vote*100,3)})% ({list_of_candidate.count(completed_list[1])})\n"
                   F"{completed_list[2]}:{round(list_of_candidate.count(completed_list[2])/vote*100,3)}% ({list_of_candidate.count(completed_list[2])})")
# automatical the text file will create since i am opening the file in write mode
file_to_output = os.path.join("..","analysis", "election_analysis.txt") 
with open(file_to_output,'w',newline='') as poll_text:
     poll_text.write("Election Results\n ---------------------------------")
     poll_text.write(election_output)
     poll_text.write("\n-------------------------------------------------------")
     poll_text.write(("\n winner: " + str(winner)))
     poll_text.write("\n------------------------------")

         
