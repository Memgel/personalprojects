print("##############################")
print("#                            #")
print("#      | Fruit Machine |     #")
print("#       | By Jude.Y   |      #")
print("#                            #")
print("##############################")
print("")
num = 1
credit = float(1) #amount of credit to start
def roll(credit, reel1, reel2, reel3):# defines the subrutine that makes it roll
    credit = credit - 0.20
    new_credit = round(credit,2)
    print("-20p")
    print (("Your credit is now £" + str(new_credit)+"0"))
    print("")
    print ("------Rolling------")
    print("")
    print (reel1 + "-" + reel2 + "-" + reel3)
    if reel1 == reel2 or reel1 == reel3 or reel2 == reel3:
        credit = credit + 0.50
        print("££ You won 50p ££")
        print (("Your credit is now £" + str(new_credit)+"0"))
    elif reel1 == reel2 == reel3:
        credit = credit + 1
        print("££ You won £1 ££")
        print (("Your credit is now £" + str(new_credit)))
    elif reel1 == "Skull" == reel2 =="Skull" or reel2 == "Skull" == reel3 =="Skull" or reel1 == "Skull" == reel3 =="Skull":
        credit = credit - 1
        print("££ You lost £1 ££")
        print (("Your credit is now £" + str(new_credit)+"0"))
    elif reel1 == "Bell" == reel2 == "Bell" == reel3 == "Bell":
        credit = credit + 5
        print("££ You won £5 ££")
        print (("Your credit is now £" + str(new_credit)+"0"))
    else:
        print("Sorry you didnt win anyting")
        print (("Your credit is now £" + str(new_credit)+"0"))

    start(num, credit)
        
def start(num, credit):
    while num == 1:
        import random
        wheel = ['Cherry','Lemon','Bell','Star','Skull']
        reel1 = random.choice(wheel)
        reel2 = random.choice(wheel)
        reel3 = random.choice(wheel)
        play = input("Would you like to roll or quit? ")
        if play == "quit":
            print(new_credit)
            num = 1 + 1
        if play == "roll":
            if credit <= 0:
                print("Sorry no credits were found")
            else:
                roll(credit, reel1, reel2, reel3)
    
start(num, credit)
    
