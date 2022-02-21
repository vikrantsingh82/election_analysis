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



# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("C:/Users/usvisin3/OneDrive - PG (1)/12 Personal/Data Analytics Learning/election_analysis/Resources", "election_analysis.txt")
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

with open(file_to_load) as election_data:
    file_reader = csv_file.reader(election_data)
    header = next(file_reader)
    print(header)
    
    # for record in file_reader:
    #     print(record)




# Close the file.
election_data.close()


#print(dir(os.path))