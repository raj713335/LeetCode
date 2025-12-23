# https://leetcode.com/problems/calculate-product-final-price/description/

import pandas as pd

def calculate_final_prices(products: pd.DataFrame, discounts: pd.DataFrame) -> pd.DataFrame:
    
    df = pd.merge(products, discounts, on='category', how='left')
    
    df = df.fillna(0)

    df['final_price'] = df['price'] - (df['price'] * (df['discount']/100))

    return df[['product_id', 'final_price', 'category']]
