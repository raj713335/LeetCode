# https://leetcode.com/problems/maximum-population-year/description/

class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:

        years = dict(zip(range(1950,2051),[0]*101))

        max_population = 0
        max_population_year = 0

        for i in range(0, len(logs)):
            for j in range(logs[i][0], logs[i][1]):
                years[j] += 1

        for year, people in years.items():
            if people > max_population:
                max_population = people
                max_population_year = year

        return max_population_year
        
