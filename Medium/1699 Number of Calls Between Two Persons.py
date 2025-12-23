# https://leetcode.com/problems/number-of-calls-between-two-persons/description/

import pandas as pd

def number_of_calls(calls: pd.DataFrame) -> pd.DataFrame:

    # Normalize pairs so that person1 < person2
    calls['person1'] = calls[['from_id', 'to_id']].min(axis=1)
    calls['person2'] = calls[['from_id', 'to_id']].max(axis=1)

    # Aggregate: call count and total duration
    result = (
        calls.groupby(['person1', 'person2'], as_index=False)
        .agg(
            call_count=('duration', 'count'),
            total_duration=('duration', 'sum')
        )
    )

    return result
