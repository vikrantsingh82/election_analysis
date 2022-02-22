# Election Analysis Using Python

## Overview of Election Audit
The election commission want to do additional audit of the local congressional election and determine the following 
  - voter turnout for each county
  - percentage of votes from each county out of the total count
  - county with the highest turnout

Election results data is available in CSV files that will be used to determine 
  - Total # of votes cast
  - List of all the candidates
  - Total # of votes and percentage of votes each candidate received
  - Winning Candidate 

## Resources
  - Data Source: election_results.csv
  - Software Used: Python 3.9.7, VS Code 1.64.1

## Election Audit Results
We leveraged our python learning to read the election_results.csv file and then iterate through all the records
in file and determine the results. Here's the audit results

![Overall Summary](https://user-images.githubusercontent.com/98173091/155036733-37ecf777-4200-45f5-be6f-aa48625359c5.png)

### Candidate Wise Results

 #### 1. Total # of votes cast in the election: 369,711  
 ![Total Votes](https://user-images.githubusercontent.com/98173091/155037249-90c452ad-ae99-4688-ba8e-c10c1859ad0f.png)
 
 #### 2. Number of votes and the percentage of the total votes each candidate received.      
 ![Candidate Wise Votes](https://user-images.githubusercontent.com/98173091/155036934-bc957b40-a5b0-4b29-a3d4-dc0f80ad41c8.png)

 #### 3.  Winning Candidate with total # of votes and percentage: Diana DeGette
 ![Winning Candidate](https://user-images.githubusercontent.com/98173091/155037042-b08cbc3a-0243-434b-b0eb-815bbaa2e967.png)

### County Wise Results

 #### 1. Total number and the percentage of total votes for each county in the precinct.
 ![County Votes](https://user-images.githubusercontent.com/98173091/155036574-770cc963-b817-404e-b657-cd3f5ce869ca.png)
  
 #### 2.  County with largest # of votes: Denver
 ![Largest Turnout County](https://user-images.githubusercontent.com/98173091/155036828-f847a3f3-757f-47c3-ad14-dde223fb4c27.png)

 
## Election Audit Summary

The python script we created provided the election results in fraction of seconds and in the desired format
election commission wanted. The current dataset had election data for only 3 counties and 3 candidates,
This script can be used to determine the any other election results for other counties or cities. 
We would need to make following changes to the code to make this script usable for other elections,

1. File paths to read the .CSV file and write the analysis text file should be changed to a central location 
instead of local drive of computer.
![filepath](https://user-images.githubusercontent.com/98173091/155043360-111f2c5c-36f9-4610-8f68-5c25be7d26fe.png)
    

  
2. Instead of using the column index to fetch the county and candidate name, we should be using "Column Name". In case the 
columns are rearranged getting row value using index will give incorrect output.
![Col Index](https://user-images.githubusercontent.com/98173091/155039451-2577c8b8-8d80-4355-900e-91989d0cd8a3.png)
