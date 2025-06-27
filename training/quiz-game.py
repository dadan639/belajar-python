print("Welcome To Game Quiz!!")

playing = input("Do you want to play? ").lower()

if playing != "yes":
    quit()
    
print("lets play the game")
score = 0

answer = input("What Does CPU stand for? ").lower()

if answer == "central processing unit":
    print("Correct!!")
    score += 1
else:
    print("Incorrect :)")

answer = input("What Does GPU stand for? ").lower()

if answer == "graphics processing unit":
    print("Correct!!")
    score += 1
else:
    print("Incorrect :)")

answer = input("What Does RAM stand for? ").lower()

if answer == "random access memory":
    print("Correct!!")
    score += 1
else:
    print("Incorrect :)")

answer = input("What Does PSU stand for? ").lower()

if answer == "power supply":
    print("Correct!!")
    score += 1
else:
    print("Incorrect :)")

answer = input("What Does SSD stand for? ").lower()

if answer == "solid state drive":
    print("Correct!!")
    score += 1
else:
    print("Incorrect :)")

print(f"You got {score} correct answer")
print(f"You got {(score/4) * 100} %")