Question = "How old are you exactly?"
Question += "\nEnter 'quit' when you're done. "

while True:
    Age = input(Question)
    if Age == 'quit':
        break
    Age = int(Age)

    if Age < 3:   
        print(" you are allowed in for free")
    elif Age < 13:
        print(" Your ticket will be $10.")
    else:
        print(" Your ticket will be $15.")
