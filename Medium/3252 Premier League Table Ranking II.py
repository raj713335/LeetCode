# https://leetcode.com/problems/premier-league-table-ranking-ii/


import pandas as pd


def calculate_team_tiers(team_stats: pd.DataFrame) -> pd.DataFrame:

                    # Function used in 3) below
    def find_tier(percentile):
        if percentile <= ceil(team_stats.position.quantile(.33)):
            return 'Tier 1'
        if percentile <= ceil(team_stats.position.quantile(.66)): 
            return 'Tier 2'
        return 'Tier 3'

                    # 1) Determine team points 
    team_stats['points'] = 3 * team_stats.wins + team_stats.draws

                    # 2) Determine team position 
    team_stats['position'] = team_stats.points.rank( 
                        method = 'min', ascending = 0)

                    # 3) Determine tier using function above
    team_stats['Tier'] = team_stats.position.apply(find_tier)

                    # 4) Sort rows and reorder columns
    return team_stats.sort_values(['points', 'team_name'],
                        ascending = [0,1]).iloc[:,[1,6,7,8]]
    
    
    
