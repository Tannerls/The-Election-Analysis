# add our dependencies
import csv
import os

# Assign a variable to load a file from a path.
file_to_load = os.path.join("election_results.csv")

# Assign a Variable to save a file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Setting total votes equal to zeor
total_votes = 0

# Setting Canidate opetions equal to row count.
canidate_options = [] 
# Delaring an empty dictionary
canidate_votes = {}

# Winning Canidate and Winning Count Tracker
winnig_canidate = ""
winning_count = 0
winning_percentage = 0


# Open the election results and read the file.
with open(file_to_load) as election_data:
    
    # To do: read and analyze the data here.
    file_reader = csv.reader(election_data)
    
    #read header row.
    headers = next(file_reader)

# Print each row in the CSV file.
    for row in file_reader:
        # Print the total_votes from each row.
        total_votes += 1
        # print the candidate name from each row.
        canidate_name = row[2]

#if the canidate does not match any existing canidate...
        if canidate_name not in canidate_options:
            # Add it to the list
            canidate_options.append(canidate_name)

            # Tracking for canidate vote count
            canidate_votes[canidate_name] = 0

        canidate_votes[canidate_name] += 1


    # save results to text file
    with open(file_to_save, "w") as txt_file:
        canidate_votes[canidate_name] += 1

    # Print the final vote count to the terminal.
        election_results = (
            f"\nElection Results\n"
            f"-------------------------\n"
            f"Total Votes: {total_votes:,}\n"
            f"-------------------------\n")
        print(election_results, end="")
        # Save the final vote count to the text file.
        txt_file.write(election_results)

        # move through the caidate list
        for canidate_name in canidate_votes:
            #retrieve vote count
            votes = canidate_votes[canidate_name]

            #calculating percentage
            vote_percentage = float(votes) / float(total_votes) * 100

            canidate_results = (
            f"{canidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

             #print(f"{canidate_name}: {vote_percentage: .2f}% ({votes:,})\n ")
            print(canidate_results)
           
            #  Save the candidate results to our text file.
            txt_file.write(canidate_results)

            if (votes > winning_count) and (vote_percentage > winning_percentage):
                #if ture then set winning_count = votes and winning_percentage = to vote_percentage
                winning_count = votes
                winning_percentage = vote_percentage
                #and, set the wiining_candidate equal to the canidates name.
                winning_canidate = canidate_name


    #print(f"{winning_canidate}: received {winning_count} votes, and won with {winning_percentage: .2f} of the total votes. ")
            winning_canidate_summary = (
                f"-------------------------\n"
                f"Winner: {winning_canidate}\n"
                f"Winning Vote Count: {winning_count:,}\n"
                f"Winning Percentage: {winning_percentage:.1f}%\n"
                f"-------------------------\n")
    #print(winning_canidate_summary)
        print(winning_canidate_summary)
        # Save the winning candidate's results to the text file.
        txt_file.write(winning_canidate_summary)
            
            