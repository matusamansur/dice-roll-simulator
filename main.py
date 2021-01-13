import random

while True:
    opt = input("Press 1 to roll the dice, or 0 to end program: ")
    if (opt == '1'): 
        print("Dice roll: " + str(random.randint(1,6)))

    elif(opt == '0'):
        print("Exiting...")
        exit(0)

    else:
        print("Invalid Option")