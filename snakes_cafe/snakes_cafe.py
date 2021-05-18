longline = "**************************************"


midlines = "**"
intro_welcome = "    Welcome to the Snakes Cafe!   "
intro_menu = "    Please see our menu below.    "
intro_last_line = " To quit at any time, type 'quit' "

print(longline)
print(f"{midlines}{intro_welcome}{midlines}")
print(f"{midlines}{intro_menu}{midlines}")
print(f"{midlines}                                  {midlines}")
print(f"{midlines}{intro_last_line}{midlines}")
print(longline)

#Add everything to the same dict
apetizers = {
  "Wings":0,
  "Cookies":0,
  "Spring Rolls":0
}
print(f"\nApetizers\n--------- ")

for x in apetizers:
  print(x)

entrees = {
  "Salmon":0,
  "Steak":0,
  "Meat Tornado":0,
  "A Literal Garden":0
  }

print(f"\nEntrees\n---------- ")
for x in entrees:
  print(x)

desserts = {
  "Ice Cream":0,
  "Cake":0,
  "Pie":0
}
print(f"\nDesserts\n---------- ")

for x in desserts:
  print(x)

drinks = {
  "Coffee":0,
  "Tea":0,
  "Unicorn Tears":0
  }
print(f"\nDrinks\n---------- ")

for x in drinks:
  print(x)

menu = apetizers, entrees, desserts, drinks

continue_loop = True

while continue_loop:
  print(longline)
  print(f"{midlines}   What would you like to order?  {midlines}")
  print(longline)
  order = input("> ")
  if order == "quit":
    print(f"{menu} coming right out!")
    continue_loop = False

  elif order in apetizers:
    order_counter = apetizers[order] 
    apetizers[order] += 1
    print(f"{order_counter} order of {order} have been added to your meal")   
    
  elif order in entrees:
    order_counter = entrees[order]
    entrees[order] += 1
    print(f"{order_counter} order of {order} have been added to your meal")
  elif order in desserts:
    order_counter = desserts[order]
    desserts[order] += 1
    print(f"{order_counter} order of {order} have been added to your meal")
  elif order in drinks:
    order_counter = drinks[order]
    drinks[order] += 1
    print(f"{order_counter} order of {order} have been added to your meal")
  else:
    print(f"Sorry, can't order {order}!")


print(order_counter)