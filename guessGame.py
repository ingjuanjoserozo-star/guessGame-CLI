# welcome message
def welcome_message(): 
    print("""
Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.
          """)
welcome_message()


# generate random number
import random as r
def random_num():
    num= r.randint(1, 100)
    return num


# select the difficulty level
def difficulty_menu():
    while True:
        print("""
Please select the difficulty level:
1. Easy (10 chances)
2. Medium (5 chances)
3. Hard (3 chances)
          """)
        dif_level= int(input("Enter your choice: "))
        if dif_level==1:
            print("Great! You have selected the Easy difficulty level.")
            choices = 10
        elif dif_level==2:
            print("Great! You have selected the Medium difficulty level.")
            choices = 5
        elif dif_level==3:
            print("Great! You have selected the Hard difficulty level.")
            choices = 3
        else:
            print("Select a correct option in the Menu")
            continue
        print("Let's start the game!")
        return choices


# timer
import time
class Timer:
    def start_time(self):
        self.start= time.perf_counter() # start counter
    def end_time(self):
        self.end= time.perf_counter() # end counter
    def show_time(self):
        total_time = self.end - self.start
        print(f"Time = {total_time:.2f} seconds")
        return total_time

timer = Timer()


# let's guess
def guess(choices):
    i = 0
    timer.start_time()
    while i < choices:
        guessed= int(input("Enter your guess: "))
        i+=1
        if guessed>numero:
            print(f"Incorrect! The number is less than {guessed}")
        elif guessed<numero:
            print(f"Incorrect! The number is greater than {guessed}")
        else:
            print(f"Congratulations! You guessed the correct number in {i} attempts")
            timer.end_time()
            save_scores()
            break

        
# score
scores=[]
def save_scores():
    i = 1
    score= timer.show_time()
    scores.append(score)
    if score < scores [0]:
        print("Great! New Record!")
    if len(scores) > 3:
        if score > scores[2]:
            print("You are not in the Top 3...")
    scores.sort()
    print("Best Times:")
    for sc in scores[0:3]:
        print(f"{i}. {sc:.2f}")
        i+=1

# game
game = True
while game == True:
    numero = random_num()
    choices= difficulty_menu() # it calls the menu
    guess(choices)
    while True:
        round= input("Play again? (y/n)").strip().lower()
        if round=='y':
            break
        elif round=='n':
            print("Thanks for playing!")
            game=False
            break
        else:
            print("Enter a valid option...")
            continue

