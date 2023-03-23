# YOUR IMPLEMENTATION OF simulate_game GOES HERE

import random

def simulate_game():
    total = 0
    # creates a for loop that runs 1000 times
    for x in range(1000):
        count6 = False
        count = 0
        list = []
        # creates a for loop that runs 100 times
        for i in range(100):
            # takes the random numbers and puts it into a list
            list.append(random.randint(1, 6))
            # checks if there is a 6 in the list
            if (list[i] == 6):
                # counts up by 1
                count += 1
            # count will turn 0 if there are no consecutive sixes
            else:
                count = 0
            # checks if count is greater than or equal to 3
            if (count >= 3):
                # turns count6 true
                count6 = True

        # when count6 is true it adds 1 to the total
        if (count6 == True):
            total += 1
            
    # returns the probabilty estimate
    return (total/1000)

# prints simulate_game()
print(simulate_game())

