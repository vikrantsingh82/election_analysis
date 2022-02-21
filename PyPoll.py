# Read the file
# Total # of votes cast
# List of candidates with votes > 0
# Total # of votes for each candidate
# Winner based in popular votes



# Import the datetime class from the datetime module.
import datetime as dt
import csv as csv_file
import os
dir(csv_file)

# Use the now() attribute on the datetime class to get the present time.
now = dt.datetime.now()
# Print the present time.
#print("The time right now is ", now.year)

#election_data = open(file_path,'r')

file_path = 'C:/Users/usvisin3/OneDrive - PG (1)/12 Personal/Data Analytics Learning/election_analysis/Resources/election_results.csv'
file_to_load = os.path.join("C:/Users/usvisin3/OneDrive - PG (1)/12 Personal/Data Analytics Learning/election_analysis/Resources","election_results.csv")




# Using the open() function with the "w" mode we will write data to the file.
# # Use the open statement to open the file as a text file.
# outfile = open(file_to_save, "w")
# # Write some data to the file.
# outfile.write("Hello World")

# with open(file_to_save,"w") as text_file:
#     text_file.write("My testing\n")
#     text_file.write("Arapahoe\n")
#     text_file.write("Denver\n")
#     text_file.write("Jefferson")

# To do: perform analysis.

# Reading the file
# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("C:/Users/usvisin3/OneDrive - PG (1)/12 Personal/Data Analytics Learning/election_analysis/Resources", "election_analysis.txt")

format_election_result = (
    f"Election Results \n"
    f"-------------------------")
    

# 1. Initialize a total vote counter.
total_votes =0

# Declare candidates list
candidate_options = []

# Dictionary to cout and add votes fir each candidate
candidate_votes = {}

#With statement to open the file and run though each record

with open(file_to_load) as election_data:
    file_reader = csv_file.reader(election_data)
    #Skipping the header
    header = next(file_reader)
    
    for record in file_reader:
        # Add to the total vote count.
        total_votes += 1        
        candidate_name = record[2]      
        if(candidate_name not in candidate_options):
            
            # 1. Adding candidate name to list
            candidate_options.append(candidate_name)
            # 2. Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 1
        else:
            # 3. If teh candidate exists in list, just increment the counter by 1
            candidate_votes[candidate_name] +=1
    # Print the candidate list.
    print(candidate_votes)

    format_election_result = (f"{format_election_result}\nTotal Votes: {total_votes:,}\n"
    f"-------------------------\n")

    #Declaring variables for winning candidates
    winning_candidate= ''
    winning_count = 0
    winning_percentgae = 0.00
    for candidate in candidate_votes:
        votes = candidate_votes[candidate]
        # % of total votes
        vote_percent = (float(votes)/float(total_votes))*100

        if(votes > winning_count) and (vote_percent > winning_percentgae):
            winning_candidate = candidate
            winning_count = votes
            winning_percentgae = vote_percent
        
        # 4. Adding the text to format string to be wtitten to the file.
        format_election_result = (f"{format_election_result}\n{candidate}: received {vote_percent:.2f}% of the vote. ({votes:,})\n")

    # 5. Print the winning candidate name and percentage of votes.
    #print(f"\nWinning candiate is : {winning_candidate} \nWining % :{winning_percentgae:.1f}%\nWinning # of votes : {winning_count:,}")
    winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentgae:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)   

# Close the file.
election_data.close()

#Formatting for text file, writing the results in desired format
format_election_result = (
    f"{format_election_result}\n"
    f"{winning_candidate_summary}")

with open(file_to_save,"w") as text_file:
    text_file.write(format_election_result)




#print(dir(os.path))