import random
lower_bound=0
higher_bound=10
possible_points=abs(higher_bound)-abs(lower_bound)
guessing_number=random.randrange(lower_bound,higher_bound)
print(guessing_number)
while possible_points>0:
    guessed_number=int(input("Enter your guess between 0-9: "))
    if guessed_number==guessing_number:
        print("you got it correct: ")
        print("you got {0} points".format(possible_points))
        break
    else:
        print("Incorrect Guess again: ")
        possible_points-=1
        print("Tries left:{} \n".format(possible_points))

