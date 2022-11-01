# sfdc_lucy_cleanup

# Objectives: 
* Inputs Data fro mthe Lucy Data Sheet and uses that to tie out and update any SFDC records missing their Customer ID or Lucy User Id for accounts and contacts respectively 
    * Future state - Use a google service account to pull the data vs. manually downloading a csv 
    
 ## Instructions
 1. Donwload the Lucy Data Sheets for Both Accounts and Users from [here](https://docs.google.com/spreadsheets/d/1uBSJ1HuW0cQdaw38aoLNCLbwmut2IaivLM_2z2lx_9g/edit#gid=404963854) as a CSV 
 2. Put both these files in the source data directory 
 3. run the script as a module ```python -m lucy_sfdc_cleanup.main``` 
