# https://leetcode.com/problems/account-balance/description/

import pandas as pd

def account_balance(transactions: pd.DataFrame) -> pd.DataFrame:

    transactions = transactions.sort_values(['account_id','day'], ascending = [True,True])
    transactions['balance'] = 0 

    account_id = -1
    balance = 0
    for index, row in transactions.iterrows():
        if row['account_id'] != account_id:
            account_id = row['account_id']
            balance = 0

        if row['type'] == 'Deposit':
            balance += row['amount']

        elif row['type'] == 'Withdraw':
            balance -= row['amount']


        transactions.loc[index, 'balance'] = balance


    return transactions[['account_id', 'day', 'balance']]

    
