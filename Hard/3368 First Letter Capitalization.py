# https://leetcode.com/problems/first-letter-capitalization/description/

import pandas as pd

def process_text(user_content: pd.DataFrame) -> pd.DataFrame:

    # change to title case with title() method
    user_content['converted_text'] = (
            user_content.content_text.apply(lambda x: x.title()))

    # rename column per problem request
    return user_content.rename(columns={'content_text': 'original_text'})
    
