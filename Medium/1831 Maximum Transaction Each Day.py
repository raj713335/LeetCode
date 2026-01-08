# https://leetcode.com/problems/maximum-transaction-each-day/description/

import pandas as pd

def find_maximum_transaction(transactions: pd.DataFrame) -> pd.DataFrame:

    # Extract date from datetime
    transactions["day_only"] = transactions["day"].dt.date

    # Find max amount per day
    max_per_day = transactions.groupby("day_only")["amount"].transform("max")

    # Keep rows where amount equals daily max
    result = transactions[transactions["amount"] == max_per_day]

    # Sort by transaction_id
    result = result.sort_values("transaction_id")

    return result[["transaction_id"]]
    
