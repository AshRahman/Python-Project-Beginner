print("Welcome to the Digital quiz")
incorrect="Incorrect"
point=0
playing=input("Do you want to play??:")

if(playing.lower()!="yes"):
    quit()

answer= input("What is YOLO?:")
if answer.lower() == "you only live once":
    print("correcto mundo")
    point+=1
else:
    print(incorrect)

answer= input("What is LOL?:")
if answer.lower() == "laugh out loud":
    print("correcto mundo")
    point+=1
else:
    print(incorrect)

answer= input("What is lmao?:")
if answer.lower() == "laughing my ass off":
    print("correcto mundo")
    point+=1
else:
    print(incorrect)

print("Quiz ended")
print("Your point is: {0}".format(point))