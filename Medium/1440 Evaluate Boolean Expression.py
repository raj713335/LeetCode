# https://leetcode.com/problems/evaluate-boolean-expression/description/

import pandas as pd
import numpy as np

def eval_expression(variables: pd.DataFrame, expressions: pd.DataFrame) -> pd.DataFrame:

    # Merge left_operand value
    df = pd.merge(
        expressions,
        variables.rename(columns={'name': 'left_operand', 'value': 'left_value'}),
        on='left_operand',
        how='left'
    )
    
    # Merge right_operand value
    df = pd.merge(
        df,
        variables.rename(columns={'name': 'right_operand', 'value': 'right_value'}),
        on='right_operand',
        how='left'
    )

    # Evaluate the boolean expression
    def eval_row(row):
        if row['operator'] == '<':
            return row['left_value'] < row['right_value']
        elif row['operator'] == '>':
            return row['left_value'] > row['right_value']
        elif row['operator'] == '=':
            return row['left_value'] == row['right_value']

    df['value'] = df.apply(eval_row, axis=1)

    # Convert boolean to 'true'/'false' string
    df['value'] = df['value'].map({True: 'true', False: 'false'})

    # Select required columns
    result = df[['left_operand', 'operator', 'right_operand', 'value']]

    return result
