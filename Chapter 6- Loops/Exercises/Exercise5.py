Sandwichs_orderd = [
    'pastrami', 'shawarma', 'grilled cheese', 'pastrami',
    'panini', 'roast beef', 'pastrami']
finished_sandwiches = []

print("I'm very sorry, we're entierly out of pastrami for today.")
while 'pastrami' in Sandwichs_orderd:
    Sandwichs_orderd.remove('pastrami')

print("\n")
while Sandwichs_orderd:
    current_sandwich = Sandwichs_orderd.pop()
    print("I am curently working on your " + current_sandwich + " sandwich.")
    finished_sandwiches.append(current_sandwich)

print("\n")
for sandwich in finished_sandwiches:
    print("I have made a " + sandwich + " sandwich.")