from FoodItemClass import FoodItem

class Order :
  def __init__(self, date): 
    self.date = date
    self.foodItems = []
  def addFoodItems(self, foodItem):
    self.foodItems += [foodItem]
 