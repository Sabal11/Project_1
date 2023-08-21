i = 1
while i <= 10:
    num = input("> ")
    if num.upper() == "HELP":
        print ("start - to start the car")
        print ("stop - to stop the car")
        print ("quit - to exit")
    elif num.upper() == "START":
        print ("Car started....... Ready to go!")
    elif num.upper() == "STOP":
        print ("Car Stopped ")
    elif num.upper() == "QUIT":
        break
    else:
        print ("I don't understand....")
        print ("Type help")
    i = i + 1
