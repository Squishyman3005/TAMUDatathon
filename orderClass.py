class Order :
  def __inti__(self, date, orderID): 
    self.date = date
    self.orderID = orderID
    self.foodItems = []
  def addFoodItems(self, foodItem):
    self.foodItems += [foodItem]
  