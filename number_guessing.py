import random

random_number = None
score = 0
count = 0
chance = 0

#initiate generating a number
def generate(i=None):
    response = input("Press 'g' to generate a random number between 1 - 5 ('q' to quit) - ")
    if response.lower() == 'g':
        generate_a_number()
        return True
    elif i == 1 and response.lower() == 'q':
        quit()
    elif response.lower() == 'q':
        return False
    else:
        print("invalid response")
        if i == 1:
            generate(1)
        else:
            generate()

#generate number
def generate_a_number():
    global random_number
    random_number = random.randint(1, 5)

#start game
def play_game():
    response = input("Do you want to play the guessing game. Y/N? ")
    if response.lower() == 'y':
        generate(1)
    elif response.lower() == 'n':
        quit()
    else:
        print("Invalid response!")
        play_game()

#output remarks
def remark():
    if round((score/count)*100) in range(75, 101):
        return 'Excellent'
    elif round((score/count)*100) in range(60, 75):
        return 'Very good'
    elif round((score/count)*100) in range(50, 60):
        return 'Good'
    elif round((score/count)*100) in range(35, 50):
        return 'Fair'
    else:
        return 'Try better next time'

#generate random success message
def correct_answer():
    responses = ['Correct. Thumbs up👍', 'Correct. Nice one👍', 'Correct. keep it up👍', 'Guessed right. Nice one👌']
    random_response = random.choice(responses)
    return random_response

#generate random failure message
def wrong_answer():
    responses = ['Wrong. try again', 'Wrong guess. try again']
    random_response = random.choice(responses)
    return random_response

#verify game continuation
def to_continue():
    i = input("Do you want to continue. Y/N? ")
    if i.lower() == 'y':
        return True
    elif i.lower() == 'n':
        return False
    else:
        print("Invalid response!")
        to_continue()

#provide hints to user
def hint():
    if generate_a_number() % 2 == 0:
        yield "number is an even number"
    if generate_a_number() % 2 == 1:
        yield "number is an even number"
    if generate_a_number() % 3 == 0:
        yield "number is a multiple of 3"

def start_game():
    global count, score, chance
    play_game()
    while True:
        try:
            response = int(input("Guess the number-> "))
        except:
            print("Invalid input")
            continue
        count += 1
        if response == random_number:
            if chance == 1:
                count -= 1  #decrement count by 1 to resolve double count of same question(due to second chance)-right answer for second chance
            score += 1  #increment score by 1 for correct answer
            chance = 0  #returns chance to initial value '0' for a correct answer
            print(correct_answer())
            if to_continue():
                if not generate():
                    break
                continue
            else:
                break
        else:
            chance += 1  #increment chance by 1 for a wrong answer
            if chance == 2:  #2 chances to answer a guess correctly
                chance = 0   #after 2 chances, chance is returned to initial value
                count -= 1   #decrement count by 1 to resolve double count of same question(due to second chance)-wrong answer for both chances
                print("Wrong. move on")
                if not generate():
                    break
                continue
            print(wrong_answer())
            continue

    print("score:", score)
    print("remark:", remark())
    print("Total:", count)

if __name__ == "__main__":
    start_game()
