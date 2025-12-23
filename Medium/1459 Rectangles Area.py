# https://leetcode.com/problems/rectangles-area/description/

import pandas as pd

def rectangles_area(points: pd.DataFrame) -> pd.DataFrame:
    
    # Self join to generate all point pairs
    df = points.merge(points, how='cross', suffixes=('_1', '_2'))

    # Keep only pairs where id1 < id2 (avoid duplicates & self-pairs)
    df = df[df['id_1'] < df['id_2']]

    # Compute area
    df['area'] = (
        (df['x_value_1'] - df['x_value_2']).abs() *
        (df['y_value_1'] - df['y_value_2']).abs()
    )

    # Remove zero-area rectangles
    df = df[df['area'] > 0]

    # Select and rename columns
    result = df[['id_1', 'id_2', 'area']].rename(
        columns={'id_1': 'p1', 'id_2': 'p2'}
    )

    # Sort as required
    result = result.sort_values(
        by=['area', 'p1', 'p2'],
        ascending=[False, True, True]
    )

    return result
