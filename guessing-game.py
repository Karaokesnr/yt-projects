print("A simple guessing game")
secret_no = 5
guess_no = 0
guess_lim = 3

while guess_no < guess_lim:
    guess = int(input("Make a guess: "))
    guess_no +=1
    if guess == secret_no:
        print("You won!")
        break
    elif guess_no < guess_lim:
        print ("Sorry, try again")
else:
    print("You snooze you loose!")
