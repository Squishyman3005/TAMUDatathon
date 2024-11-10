import pandas as pd
from FoodItemClass import FoodItem
from orderClass import Order

# Read in the file, order number can be added after being sorted
# if reading in 
def getFoodAndOrderIndexes(combined_df):
    indexes = []
    indexes.append(0)
    firstRow = True
    listIndexes = []
    orderList = []
    for index, row in combined_df.iterrows():
        if (firstRow):
            prev = row["Order #"]
            date = row["Sent Date"]
            listIndexes += [index]
            a = Order(date)
            orderList += [a]
            firstRow = False
        else:
            current = row["Order #"]
            if (prev != current):
                prev = current
                date = row["Sent Date"]
                listIndexes += [index]
                a = Order(date)
                orderList += [a]
        # case for mac and cheese
        # if either the next row has noodles or isn't mac and cheese append that index
        if (index == (len(combined_df) - 2) ):
            break
        if row["Parent Menu Selection"] == "Mac and Cheese":
            if (row["Parent Menu Selection"] != combined_df.iloc[index + 1]["Parent Menu Selection"]) or (combined_df.iloc[index+1]["Option Group Name"] == "Noods"):
                indexes.append(index + 1)
        if row["Parent Menu Selection"] == "Grilled Cheese Sandwich":
            if (row["Parent Menu Selection"] != combined_df.iloc[index+1]["Parent Menu Selection"]) or (combined_df.iloc[index+1]["Option Group Name"] == "Choose Your Meats"):
                indexes.append(index + 1)
        if row["Parent Menu Selection"] == "Sides/Desserts":
            indexes.append(index + 1)
        if row["Parent Menu Selection"] == "Drinks":
            indexes.append(index+1)
        if row["Parent Menu Selection"] == "Mac and Cheese Party Tray (Plus FREE Garlic Bread)":
            indexes.append(index+1)
    indexes += [len(combined_df) - 1]
    return indexes, orderList, listIndexes

# Various statistical tests
combined_df = pd.read_csv("combined_sheets_with_june.csv")
# orderslist = []
# for index, row in combined_df.iterrows():
#     ordernumber = row[0]
#     currentOrder_df = combined_df.iloc(index)
    
#     addOrder(orderslist, currentOrder_df)
foodsIndex, orderList, listIndexes = getFoodAndOrderIndexes(combined_df)
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
    
    if ((index == 0 or index == foodsIndex[n]) and n != len(foodsIndex) - 1):
        if (index != 0):
            orderList[s].addFoodItems(a)
            a = FoodItem(row["Parent Menu Selection"])
        if (index == 0):
            a = FoodItem(row["Parent Menu Selection"])
        if (index == foodsIndex[n]):
            n += 1
    a.addModifierGroup(row["Option Group Name"])
    a.addModifiers(row["Modifier"])
    if (index == listIndexes[l] and l != len(listIndexes)-1):            
        l += 1
        s +=1

print(len(orderList))

