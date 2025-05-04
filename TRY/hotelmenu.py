menu = { 
    'pizza':40,
    'pasta':50,
    'maggie':30,
    'burger':60,
    'salad':70,
    'coffee': 80,
}
print("welcome to our pyRestorant")
print(" pizza : Rs 40\n pasta : Rs 50\n maggie : Rs 30\n burger : Rs 30\n salad : Rs 70\n coffee : Rs80")

order_total = 0

item1= input("Enter your order : ")
if item1 in menu:
    order_total += menu[item1]
    print("your item 1 has been added to your order !")
else : 
    print(f"Ordered item {item1} is not available\nplease order something that we can serve you ! ")

Another_order = input("Do you want to another item (yes/No)")
if Another_order =="yes":
    item2= input("Enter your second item : ")
    if  item2 in menu:
        order_total +=menu[item2]
        print(f"item {item2} has been added to your order !")

    else :
        print(f"Ordered item {item2} is not available !")
print(f"The total amount of your order is {order_total} !")
