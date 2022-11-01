
import pandas as pd 

from lucy_sfdc_cleanup.salesforce.setup.salesforce_setup import MySalesforce

def update_records(accounts_dict, contacts_dict):
    '''
    Function that takes the accounts and contacts dictionaries with populated Customer and Lucy User Ids respectively and updates SFDC 

    Args: 
    accounts_dict: Dictionary of Accounts with Id and Customer_ID__c
    contacts_dict: Dictionary of Contacts with Id and Lucy_User_ID__c ]
    '''
    # update accounts and store results 
    accounts_res = MySalesforce.sf.bulk.Account.update(accounts_dict)
    # unpack results 
    res_df = pd.DataFrame.from_records(accounts_res)
    # show account results 
    if res_df.shape[0] > 0:
        print(
            'Account Results:\n',
            res_df.success.value_counts()
        ) 
        
    # update contacts and 
    contacts_res = MySalesforce.sf.bulk.Contact.update(contacts_dict)
    # upnakc results 
    res_df = pd.DataFrame.from_records(contacts_res)
    # show contact results 
    if res_df.shape[0] > 0:
        print(
            'Contact Results:\n',
            res_df.success.value_counts()
        )