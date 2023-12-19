# https://leetcode.com/problems/design-a-food-rating-system/


from sortedcontainers import SortedList

class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.ratings={}
        self.cuisine={}
        self.by_cuisine=collections.defaultdict(lambda:SortedList())
        for food,cuisine,rating in zip(foods,cuisines,ratings):
            self.cuisine[food]=cuisine
            self.ratings[food]=rating
            self.by_cuisine[self.cuisine[food]].add((-rating,food))


    def changeRating(self, food: str, newRating: int) -> None:
        prevRating=-self.ratings[food]
        self.ratings[food]=newRating
        self.by_cuisine[self.cuisine[food]].remove((prevRating,food))
        self.by_cuisine[self.cuisine[food]].add((-newRating,food))

    def highestRated(self, cuisine: str) -> str:
        return self.by_cuisine[cuisine][0][1]
        
        

        


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)

