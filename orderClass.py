from FoodItemClass import FoodItem

class Order :
  def __init__(self, date): 
    self.date = date
    self.foodItems = []
  def addFoodItems(self, foodItem):
    self.foodItems += [foodItem]
  def findCombination(self, Items):
    """
    Items: list of items
    Checks if all items are in modifiers 
    """
    combinationCount = 0
    for foodItem in self.foodItems:
      notFound = False
      for Item in Items:
        if Item not in foodItem.modifiers.keys():
          notFound = True
          break
      if notFound:
        continue
      combinationCount += 1
    return combinationCount
  def totalToppings(foodType):
    #Find Sum
    sum = 0
    for foodItem in self.foodItems:
      if (foodItem.name() == foodType):
        sum += foodItem.
   

a = FoodItem("Mac And Cheese")
a.addModifiers("parmesian")
a.addModifiers("chicken")
a.addModifiers("fortnite")

A = Order("8-30-2024")
A.addFoodItems(a)

combo = 0
combo = A.findCombination(["parmesian", "Goku", "chicken"])
print(combo)