from lucy_sfdc_cleanup.salesforce.setup.salesforce_setup import MySalesforce

class SalesForceTables():
    def __init__(self):
        self.accounts_df = MySalesforce.sfdc_query(
            """
                SELECT
                    Id,
                    Name,
                    Website,
                    Client_Status__c,
                    Customer_ID__c
                FROM
                    Account
                WHERE
                    Client_Status__c = 'Active' AND
                    Customer_ID__c = null
        """
        )

        self.contacts_df = MySalesforce.sfdc_query(
            """
                SELECT
                    Id,
                    Email,
                    Lucy_User_ID__C
                FROM
                    Contact
                WHERE
                    Account.Client_Status__c = 'Active' AND 
                    Lucy_User_ID__c = null
            """
        )