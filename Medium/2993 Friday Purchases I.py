# https://leetcode.com/problems/friday-purchases-i/description/

import pandas as pd

def friday_purchases(purchases: pd.DataFrame) -> pd.DataFrame:
    
    # Ensure datetime type
    purchases['purchase_date'] = pd.to_datetime(purchases['purchase_date'])

    # Keep only Fridays (Monday=0, ..., Friday=4)
    friday_df = purchases[purchases['purchase_date'].dt.weekday == 4]

    # Compute week of month
    friday_df['week_of_month'] = (
        (friday_df['purchase_date'].dt.day - 1) // 7 + 1
    )

    # Aggregate total spending per Friday
    result = (
        friday_df
        .groupby(['week_of_month', 'purchase_date'], as_index=False)
        .agg(total_amount=('amount_spend', 'sum'))
        .sort_values('week_of_month')
    )

    return result
