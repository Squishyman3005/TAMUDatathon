import pandas as pd
from FoodItemClass import FoodItem
from orderClass import Order
def newOrderIndexes(df):
  firstRow = True
  listIndexes = []
  orderList = []
  for index, row in df.iterrows():
    if (index > 400):
        break
    if (firstRow):
      prev = row[0]
      date = row[1]
      listIndexes += [index]
      a = Order(date)
      orderList += [a]
      firstRow = False
    else:
      current = row[0]
      if (prev != current):
        prev = current
        date = row[1]
        listIndexes += [index]
        a = Order(date)
        orderList += [a]
  return orderList, listIndexes

# Read in the file, order number can be added after being sorted
# if reading in 
def getFoodIndexes(combined_df):
    indexes = []
    indexes.append(0)

    for index, row in combined_df.iterrows():
        # case for mac and cheese
        if (index > 400):
            break
        # if either the next row has noodles or isn't mac and cheese append that index
        if (index == (len(combined_df) - 2) ):
            break
        if row[4] == "Mac and Cheese":
            if (row[4] != combined_df.iloc[index + 1][4]) or (combined_df.iloc[index+1][3] == "Noods"):
                indexes.append(index + 1)
        if row[4] == "Grilled Cheese Sandwich":
            if (row[4] != combined_df.iloc[index+1][4]) or (combined_df.iloc[index+1][3] == "Choose Your Meats"):
                indexes.append(index + 1)
        if row[4] == "Sides/Desserts":
            indexes.append(index + 1)
        if row[4] == "Drinks":
            indexes.append(index+1)
        if row[4] == "Mac and Cheese Party Tray (Plus FREE Garlic Bread)":
            indexes.append(index+1)
    indexes += [len(combined_df) - 1]
    return indexes

# Various statistical tests
combined_df = pd.read_csv("combined_sheets_with_june.csv")
# orderslist = []
# for index, row in combined_df.iterrows():
#     ordernumber = row[0]
#     currentOrder_df = combined_df.iloc(index)
    
#     addOrder(orderslist, currentOrder_df)
foodsIndex = getFoodIndexes(combined_df)
orderList, listIndexes = newOrderIndexes(combined_df)
foods = []
firstRow = True
a = FoodItem("")
counter1 = 1 ; counter2 = 0
n = 1
s = 0
l = 1
for index, row in combined_df.iterrows():
    # Need to iterate through rows for order 0 until row index reaches listIndexes[1]
    # when it reaches listIndexes[1] increment to listIndexes[2] and start orderList[1]
    # need to iterate for individual food items until index = foodsIndex[1] then increment to foodsIndex[2]
    # only create a new food item when index == foodsIndex[n]
    if (index > 400):
        break
    
    if ((index == 0 or index == foodsIndex[n]) and n != len(foodsIndex) - 1):
        if (index != 0):
            print(s, index, listIndexes[l], a.output())
            orderList[s].addFoodItems(a)
            a = FoodItem(row[4])
        if (index == 0):
            a = FoodItem(row[4])
        if (index == foodsIndex[n]):
            n += 1
    a.addModifierGroup(row[3])
    a.addModifiers(row[2])
    if (index == listIndexes[l] and l != len(listIndexes)-1):            
        l += 1
        s +=1



