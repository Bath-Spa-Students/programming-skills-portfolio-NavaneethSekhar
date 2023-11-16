Sandwichs_Orderd = ['grilled cheese', 'shawarma', 'turkey', 'panini']
Completed_Sandwiches = []

while Sandwichs_Orderd:
    current_sandwich = Sandwichs_Orderd.pop()
    print("I'm curently working on your " + current_sandwich + " sandwich.")
    Completed_Sandwiches.append(current_sandwich)

print("\n")
for sandwich in Completed_Sandwiches:
    print("I have made a " + sandwich + " sandwich.")