import random
random_num=random.randint(0,50)
print("Guess Number Program")
print("User Allowed Only 5 Times Guess")
chance=1
while True:
    if chance<5:
        print(f"Number Of Chance Left {6-chance}")
        print("Guess The Number:",end=" ")
        guess=int(input())
        if guess>random_num:
            print("Guessed High.")
        elif guess==random_num:
            print("Congratulations.Guessed Correct Number")
            break
        else:
            print("Guessed Low")
    elif chance==5:
        print("Its Your Last Chance")
        print("Guess The Number:",end=" ")
        guess=int(input())
        if guess>random_num:
            print("Guessed High.")
            print("Game Over!")
        elif guess==random_num:
            print("Congratulations.Guessed Correct Number")
        else:
            print("Guessed Low")
            print("Game Over!")
        break                           
    chance=chance+1
print(f"Random Number ={random_num}")   
print("Developed By Er Pratham Saxena")     
