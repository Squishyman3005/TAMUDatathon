import pandas as pd

# Define the class to represent the food order
class FoodOrder:
    def __init__(self, order_id, sent_date):
        self.order_id = order_id
        self.sent_date = sent_date
        self.noods = []
        self.cheese = []
        self.meats = []
        self.toppings = []
        self.drizzles = []
        self.sides = []
        self.drinks = []

    def add_item(self, modifier, option_group_name):
        # Based on the Option Group Name, we classify the modifiers into attributes
        if option_group_name == "Noods":
            self.noods.append(modifier)
        elif option_group_name == "Choose Your Cheese":
            self.cheese.append(modifier)
        elif option_group_name == "Choose Your Meats":
            self.meats.append(modifier)
        elif option_group_name == "Choose Your Toppings":
            self.toppings.append(modifier)
        elif option_group_name == "Choose Your Drizzles":
            self.drizzles.append(modifier)
        elif option_group_name == "Choose Your Side":
            self.sides.append(modifier)
        elif option_group_name == "Choose Your Drink":
            self.drinks.append(modifier)

    def __repr__(self):
        return f"Order ID: {self.order_id}\nSent Date: {self.sent_date}\nNoods: {self.noods}\nCheese: {self.cheese}\nMeats: {self.meats}\nToppings: {self.toppings}\nDrizzles: {self.drizzles}\nSides: {self.sides}\nDrinks: {self.drinks}"

def process_orders(csv_file_path):
    # Read the CSV file using pandas
    df = pd.read_csv(csv_file_path)
    
    # Create a dictionary to store orders by order number
    orders = {}

    # Iterate over each row in the dataframe
    for _, row in df.iterrows():
        order_number = row['Order #']
        sent_date = row['Sent Date']
        modifier = row['Modifier']
        option_group_name = row['Option Group Name']
        
        # If the order does not exist, create a new FoodOrder instance
        if order_number not in orders:
            orders[order_number] = FoodOrder(order_number, sent_date)
        
        # Add the item to the respective order
        orders[order_number].add_item(modifier, option_group_name)

    # Return the list of all orders
    return list(orders.values())

# Example usage
orders = process_orders('test.csv')  # Replace with your file path

# Display the results
##for order in orders:
##    print(order)


print(orders[0])
print(orders[1])