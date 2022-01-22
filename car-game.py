command =""
started = False
while True :
    command  = (input(">")).lower()
    if command == "start":
        if started:
            print ("Car is already started")
        else :
            started = True
            print ("Car started successfully")
    elif command == "stop":
        if not started :
            print("Car is already stopped")
        else :
            started = False
            print("Car stopped succesfully")
    elif command == "help":
        print ("""
start -> start the car
stop ->stop the car
quit -> quit the game
        """)
    elif command =="quit":
        print ("you exited the game.")
        break
    else:
        print ("sorry, I do not understand you")