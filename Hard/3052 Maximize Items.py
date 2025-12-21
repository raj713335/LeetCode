# https://leetcode.com/problems/maximize-items/description/

import pandas as pd

def maximize_items(inventory: pd.DataFrame) -> pd.DataFrame:

    prime = inventory[inventory.item_type == 'prime_eligible']
    nt_pr = inventory[inventory.item_type == 'not_prime']

    p_sum, p_cnt = sum(prime.square_footage), len(prime)
    n_sum, n_cnt = sum(nt_pr.square_footage), len(nt_pr)

    dp, m = divmod(500_000, p_sum)
    dn = m//n_sum

    return pd.DataFrame({'item_type':['prime_eligible', 'not_prime'], 
                        'item_count':[dp * p_cnt, dn * n_cnt] })
    
