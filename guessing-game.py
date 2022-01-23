print ("""
A  GUESSING GAME
Enter a single digit number to play
""")
secret_no = 9
guess_no = 0
guess_limit= 3
while guess_no<guess_limit:
    guess =int(input ('Make a guess: '))
    guess_no +=1
    if guess == secret_no:
        print ("You won!")
        break
else:
    print("Sorry you lost.")
