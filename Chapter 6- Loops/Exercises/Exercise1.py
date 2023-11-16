Toping_on_Pizza ="\nWhat kind of toping would you like on top of your pizza?"
Toping_on_Pizza +="\nEnter 'quit' when you are done: "

while True:
    Topping = input(Toping_on_Pizza)
    if Topping != 'quit':
        print(" I'll add " + Topping + " to your pizza." )
    else:
        break