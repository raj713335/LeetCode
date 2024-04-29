# https://leetcode.com/problems/flip-game/description/

class Solution:
    def generatePossibleNextMoves(self, currentState: str) -> List[str]:

        ans = []

        if len(currentState) < 2:
            return ans

        currentState = list(currentState)

        for i in range(0, len(currentState)-1):
            if currentState[i:i+2] == ["+", "+"]:
                temp = currentState.copy()
                temp[i:i+2] = ["-", "-"]
                ans.append("".join(temp))

        return ans

        
