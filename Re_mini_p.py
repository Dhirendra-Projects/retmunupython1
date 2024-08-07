#Define the menu with Price
menu = {
    "Pizza": 40,
    "Burger":50,
    "Pasta": 60,
    "Chicken tikka":100,
    "Sushi Rolls":80,
    "Coffee": 50,
}

#Greetings
print("Wecome to Our Python Restaurant")
print("Pizza: Rs-40\nBurger: Rs-50\nPasta: Rs-60\nChicken Tikka: Rs-100\nSushi Rools: Rs-80\nCoffee: Rs-50 ")

#Order from Guest 
order_total = 0
order_item = [ ]
item = input("Please enter your itme order name: =")
if item in menu:
    order_item.append(item)
    order_total+= menu[item] #To update order_total
    print(f"Your item {item} has been added to your order")

else:
    print(f" Sorry !! ordered item {item}is not available ")

another_order = input("Do you want to add another item? (Yes/No)")
if another_order == "Yes":
   item_2 =input("Please enter your itme: =")
   order_item.append(item_2)
   order_total+= menu[item_2]
   print(f"Item {item_2} has been added to order")
else:
    print(f"Sorry!! item { item_2} is not available now!")

print(f"The total amount of item {order_item}to pay is {order_total}")    







