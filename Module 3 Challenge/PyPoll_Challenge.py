# -*- coding: UTF-8 -*-
"""PyPoll Homework Challenge Solution."""

# Add our dependencies.
import csv as csv_file
import os

# Add a variable to load a file from a path.
file_to_load = os.path.join("C:/Users/usvisin3/OneDrive - PG (1)/12 Personal/Data Analytics Learning/election_analysis", "Resources", "election_results.csv")
# Add a variable to save the file to a path.
file_to_save = os.path.join("C:/Users/usvisin3/OneDrive - PG (1)/12 Personal/Data Analytics Learning/election_analysis/Module 3 Challenge", "election_analysis.txt")

# Initialize a total vote counter.
total_votes = 0

# Candidate Options and candidate votes.
candidate_options = []
candidate_votes = {}


# 1: Create a county list and county votes dictionary.
county_options = []
county_votes = {}



# Track the winning candidate, vote count and percentage
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# 2: Track the largest county and county voter turnout.

largest_county = ""
votes_for_largest_count = 0


# Read the csv and convert it into a list of dictionaries

# Using with statement to populate list and dictoinary created for county data
with open(file_to_load) as county_data:
    file_reader = csv_file.reader(county_data)
    
    #Read the header
    header = next(file_reader)
    
    #for each row in CSV file read the data using for loop.
    for record in file_reader:
        # Add to the total vote count.
        total_votes += 1  

        # Get the candidate name from each row.
        candidate_name = record[2]

         # 3: Extract the county name from each row.    
        county_name = record[1]            


        # If the candidate does not match any existing candidate add it to
        # the candidate list
        if candidate_name not in candidate_options:

            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)
            # And begin tracking that candidate's voter count.
            candidate_votes[candidate_name] = 1
        else:
            # Add a vote to that candidate's count
            candidate_votes[candidate_name] += 1

        # 4a: Write an if statement that checks that the
        # if the county does not exists in the county list, just add it to the list
        if(county_name not in county_options):            
            # 4b. Adding county name to list
            county_options.append(county_name)

            # 4c. At the same time begin tracking that county's vote count, and store that in the dictionary created using county name as key.
            county_votes[county_name] = 0
        
        # 5: Add a vote to that county's vote count. If the county exists in list, just increment the county vote counter by 1 in the dictionary
        county_votes[county_name] +=1
    
# Save the results to our text file.
with open(file_to_save, "w") as text_file:


# Print the final vote count (to terminal)
# I'll not use this formatting, i'll use the format_election_result variable that i'm using and aoppending the data as required 
    election_results = (
        f"Election Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n\n"
        f"County Votes:")
    print(election_results, end="")
    
    # 6a: Write a for loop to get the county from the county dictionary.
    for county in county_votes:
        # 6b: Retrieve the county vote count.        
        votes_per_county = county_votes[county]

        # 6c: Calculate the percentage of votes for the county.
        vote_percent_per_county = (float(votes_per_county)/float(total_votes))*100        
        
        # 6f: Write an if statement to determine the winning county and get its vote count.
        if(votes_per_county > votes_for_largest_count):
            largest_county = county
            votes_for_largest_count = votes_per_county
        # 6d: Print the vote % and total # of votes for each county to the terminal.
        print(f"{county}: {vote_percent_per_county:.1f}%. ({votes_per_county:,})\n", end="")
        # Adding the text to format string to be wtitten to the file.
        election_results = (f"{election_results}\n{county}: {vote_percent_per_county:.1f}% ({votes_per_county:,})")
   

    # 6e: Save the county votes to a text file.
    text_file.write(election_results)             

    # 7: Print the county with the largest turnout to the terminal.
    largest_county_text = (f"\n\n--------------------------------------------\n"
    f"Largest County Turnout: {largest_county} ({votes_for_largest_count:,})\n"
    f"----------------------------------------------\n\n")
    

    # 8: Print and Save the county with the largest turnout to a text file.
    print(largest_county_text, end="")
    text_file.write(largest_county_text) 

    # Print and Save the final candidate vote count to the text file.
    for candidate_name in candidate_votes:

        # Retrieve vote count and percentage
        votes = candidate_votes.get(candidate_name)
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # Print each candidate's voter count and percentage to the
        # terminal.
        print(candidate_results)
        #  Save the candidate results to our text file.
        text_file.write(candidate_results)

        # Determine winning vote count, winning percentage, and candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage

    # Print and Save the winning candidate (to terminal)
    winning_candidate_summary = (
        f"\n-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")

    print(winning_candidate_summary)
    # Save largest county name and the winning candidate's name to the text file
    text_file.write(winning_candidate_summary)
