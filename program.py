import gym
#objective - Write a program which simulates a gym-supply retailer

#constraints - Keep track of supply and costs for each item. Display current inventory to the user/customer. Save and load
#stock from a text document


#https://realpython.com/iterate-through-dictionary-python/

shop_stock = gym.get_shop_stock()
# for key in shop_stock:
#     print(key)

# for item in shop_stock.items():
#     print(item)

# for key,value in shop_stock.items():
#     print(key, "-",value)

#indent ctrl + ]
print("\n \n Hello, welcome to our gym \n")

print("Here is our inventory: \n")

for key,value in shop_stock.items():
    print(key + " --- $" + str(value.price) + " (" + str(value.stock) + " left)")


valid_item_selected = False

while(valid_item_selected == False):

    selected_item =  input("\n Type the name of the item you would like to purchase (case insensitive) \n \n")


    for key in shop_stock:
        if(selected_item == key):
            valid_item_selected = True

    if valid_item_selected == False:
            print(selected_item + " is not a valid choice!")


print("You want to buy " + selected_item + "? How many would you like? (" + str(shop_stock[selected_item].stock) + " available)")