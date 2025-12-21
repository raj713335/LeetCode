# https://leetcode.com/problems/bitwise-user-permissions-analysis/description/

import pandas as pd

def analyze_permissions(user_permissions: pd.DataFrame) -> pd.DataFrame:


    common_perms = user_permissions.iloc[0]['permissions']
    any_perms = 0

    for index, row in user_permissions.iterrows():
        common_perms = common_perms & row['permissions']
        any_perms = any_perms | row['permissions']

    return pd.DataFrame({
        "common_perms": [common_perms],
        "any_perms": [any_perms]
    })
