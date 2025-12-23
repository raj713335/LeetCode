# https://leetcode.com/problems/premier-league-table-ranking-iii/description/

import pandas as pd

def process_team_standings(season_stats: pd.DataFrame) -> pd.DataFrame:

    season_stats['points'] = 3*season_stats.wins + season_stats.draws
    season_stats['goal_difference'] = season_stats.goals_for - season_stats.goals_against

    # sort to determine ranks
    season_stats = season_stats.sort_values(by=['season_id', 'points', 'goal_difference', 'team_name'], 
                                ascending=[True, False, False, True])

    #  assign ranks
    season_stats['position'] = season_stats.groupby('season_id').cumcount() + 1

    # return the required columns from the dataframe
    return season_stats.iloc[:,[0,1,2,9,10,11]]
    
