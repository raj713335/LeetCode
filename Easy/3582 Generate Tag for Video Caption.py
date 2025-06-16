# https://leetcode.com/problems/generate-tag-for-video-caption/description/

class Solution:
    def generateTag(self, caption: str) -> str:

        caption = caption.strip()

        caption = list(map(str, caption.split(" ")))

        res = "#"

        res += caption[0].lower()[:99]

        for i in range(1, len(caption)):
            res += caption[i].capitalize()[:99]

        return res[:100]
        
