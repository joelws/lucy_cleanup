import time

import requests as r
import pandas as pd

from lucy_sfdc_cleanup.salesforce.sfdc_import import SalesForceTables
from lucy_sfdc_cleanup.salesforce.sfdc_upload import update_records

def cleanup_ids():
    '''
    Functiona that imports in Lucy Data and SFDC and finds missing Customer and Lucy User Ids in Salesforce and uploads them 
    '''
    #### import lucy data ####
    clients_df = pd.read_csv('lucy_sfdc_cleanup/source_data/Lucy data - UPDATED EVERY FRIDAY ___DO NOT MAKE A COPY___ - Accounts.csv')
    users_df = pd.read_csv('lucy_sfdc_cleanup/source_data/Lucy data - UPDATED EVERY FRIDAY ___DO NOT MAKE A COPY___ - Users.csv')

    ## cleanup clients DataFrame 

    # drop NaNs and duplicates 
    clients_df = clients_df.dropna(subset=['customer'])
    clients_df = clients_df.drop_duplicates(subset=['customer','customer_id'])
    # format customer id 
    clients_df.customer_id = clients_df.customer_id.astype('str').str.replace(',','').astype('float').astype('int').astype('str')

    ## cleanup users DataFrame 

    # drop duplicates 
    users_df = users_df.drop_duplicates(subset=['email','user_id'])
    # format user id 
    users_df.user_id = users_df.user_id.astype('str').str.replace(',','').astype('int').astype('str')

    ## import SFDC Data ##
    sf_data = SalesForceTables()

    ## Match in Missing Ids ## 
    act_upload_df = sf_data.accounts_df.set_index('Name').join(clients_df.set_index('customer')['customer_id'])[['Id','customer_id']].dropna().drop_duplicates()
    ct_upload_df = sf_data.contacts_df.set_index('Email').join(users_df.set_index('email')['user_id'])[['Id','user_id']].dropna().drop_duplicates()

    ## Prep for Upload 

    # rename columns 
    act_upload_df = act_upload_df.rename({'customer_id':'Customer_ID__c'}, axis='columns')
    ct_upload_df = ct_upload_df.rename({'user_id':'Lucy_User_ID__c'}, axis='columns')
    act_upload = act_upload_df.to_dict(orient='records')
    contact_upload = ct_upload_df.to_dict(orient='records')

    # upload to SFDC 
    update_records(
        accounts_dict=act_upload,
        contacts_dict=contact_upload
    )


def main():
    while True:
        cleanup_ids()
        time.sleep(60 * 60 * 24)

if __name__=='__main__':
    main()