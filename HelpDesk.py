import time
Keywords1 = ["internet"]
Keywords2 = ["slow"]
Keywords3 = ["audio"]
Keywords4 = ["graphics"]
Keywords5 = ["password"]
KeywordsE = ["exit", "stop"]
while(True):
    name = input("Hello, I am an automated assistant, what is your name? ")
    time.sleep(1)
    answer = input(f"Hello {name}, what can I help you with? ")
    words = answer.lower().split()
    for word in words:
        if (word in Keywords1, Keywords2, Keywords3, Keywords4, Keywords5, KeywordsE):
            print("You are having problems with", word)
            if(word=="internet"):
                print("Ensure all cables are connected or, if using wireless, that the router is active")
            elif(word == "slow"):
                print("Check active programs and shut down any not in use, this can be done by opening task manager, done by pressing control (CRTL),shift (The arrow pointing up) and escape (ESC) at the same time")
            elif (word =="audio"):
                print("Ensure all wires are plugged in, ensure audio settings are changed to how you want them to be")
            elif(word =="graphics"):
                print("Ensure all drivers are fully updated and, if needed, replace them")
            elif(word =="password"):
                print("Ensure Caps lock is disabled (The top arrow an the left of the keyboard) or, if you can not remember it, use forgot password on the password page")
            elif(word =="exit", "stop"):
               print(f"Goodbye {name}")
            exit()
        else: print("I am sorry but I am unsure of how to help with that")

        exit()