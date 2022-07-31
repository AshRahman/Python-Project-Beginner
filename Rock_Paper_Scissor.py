import random

possible_choice=[ 1, 2 ,3 ]

points = 0
print("Welcome to Game of rock paper scissor!! \n Enter your choice to play \n 1 = rock 2 = paper 3 = scissor")

while True:
    pc_choice=random.choice(possible_choice)
    print(pc_choice)
    user_choice=int(input())
    if user_choice == pc_choice:
        points+=1
        print("You won,your points {}".format(points))
    else:
        answer=input("You lost this round.\n Want to play again??")
        if answer.lower()=="yes":
            continue
        else:
            break

    