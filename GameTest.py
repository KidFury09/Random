from random import shuffle
import pandas as pd

scores = []
players = []
genders = []
cities = []
ages = []

n = int(input("Enter the number of players to be added: "))
print()
 
for z in range(1,n+1):
    
    names = input(f"Enter player {z} name : ")
    players.append(names)

    gender = input("Gender: ")
    genders.append(gender)

    city = input("City: ")
    cities.append(city)

    age = input("Age: ")
    ages.append(age)

    print()

print()
 
def riddle():
 
    global players, score, Id 
 
    words = {"egg": "What has to be broken before you can use it? ",
             "candle": "I'm tall when I'm young and I'm short when I'm old. Who am I? ",
             "darkness":"The more of this there is, the less you see. What is it? ",
             "alphabets":"Which word contains all 26 letters? ",
             "incorrectly":"Which word in the dictionary is spelled incorrectly? ",
             "orange":"Which colour can we eat? "}

 
    for i in words:
        print(words[i])
        guess = input("Enter your guess: ").lower()
 
        if guess == i:
            score += 10
            print("Correct answer")
            print()
 
        else:
            score -= 5
            print("Wrong answer")
            print()
 
        print("Would you like to continue?")
        cho = input("Enter C to continue or S to stop: ").lower() 
        print()
 
        if cho == "c":
            pass
        elif cho == "s":
            break
 
 
    print(players[Id],"scored:",score)
    print()

 
def jumble():
 
    global players, score, Id
 
    words = ["computer","laugh","confidence","documentary","entertainment","practice"]
 
    for i in words:
 
        word = (list(i))
        shuffle(word)
        x = ""
        for j in word: 
            x += j
 
        print("Solve:", x)
        guess = input("Enter your guess here: ").lower()
 
        if guess == i:        
            score += 10
            print("Correct")
            print()
 
 
        else:
            score -= 5
            print("Wrong")
            print()
 
        print("Would you like to continue?")
        cho = input("Enter C to continue or S to stop: ").lower() 
        print()
 
        if cho == "c":
            pass
        elif cho == "s":
            break
 
    print(players[Id],"scored:",score)
    print()
    
 
for Id in range(len(players)):
 
    print(f"{players[Id]}'s turn to play")
    print()
    score = 0
    
    while True:
        print("Choose an option")    
        print("1. Riddles")
        print("2. Jumbled Words")
        print("3. Next player")
        print()
        ch = int(input("Enter your choice: "))
        print()
 
        if ch == 1:
            riddle()
 
        elif ch == 2:
            jumble()
 
        elif ch == 3:
            print("Thank you for playing")
            print()
            scores.append(score)
            break
 
        else:
            print("Invalid option")
            print()
    

data = {"Name" : players, "Score" : scores, "Gender" : genders, "City" : cities, "Age" : ages}

df = pd.DataFrame(data)
df.to_excel(r"")
