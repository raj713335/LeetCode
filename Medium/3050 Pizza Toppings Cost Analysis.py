# https://leetcode.com/problems/pizza-toppings-cost-analysis/description/

import pandas as pd

def cost_analysis(toppings: pd.DataFrame) -> pd.DataFrame:
    
    # Cross join to get all combinations of 3 toppings
    df = toppings.merge(toppings, how='cross', suffixes=('_1', '_2'))
    df = df.merge(toppings, how='cross')

    # Rename columns from third join
    df = df.rename(columns={
        'topping_name': 'topping_name_3',
        'cost': 'cost_3'
    })

    # Ensure no repeated toppings and alphabetical order
    df = df[
        (df['topping_name_1'] < df['topping_name_2']) &
        (df['topping_name_2'] < df['topping_name_3'])
    ]

    # Create pizza combination string
    df['pizza'] = (
        df['topping_name_1'] + ',' +
        df['topping_name_2'] + ',' +
        df['topping_name_3']
    )

    # Calculate total cost and round to 2 decimals
    df['total_cost'] = (
        df['cost_1'] + df['cost_2'] + df['cost_3']
    ).round(2)

    # Select required columns
    result = df[['pizza', 'total_cost']]

    # Sort as required
    result = result.sort_values(
        by=['total_cost', 'pizza'],
        ascending=[False, True]
    )

    return result
