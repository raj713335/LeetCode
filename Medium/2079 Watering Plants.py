# https://leetcode.com/problems/watering-plants/


class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        
        steps = 0
        counter = 0
        full_capacity = capacity
        
        for i in range(0, len(plants)):
            
            if plants[i] <= full_capacity:
                full_capacity -= plants[i]
                counter += 1
                steps += 1
            else:
                steps += counter
                counter += 1
                steps += counter
                full_capacity = capacity
                full_capacity -= plants[i]
                
            print(steps)
                
        return steps
                
                
                
            
            
        
