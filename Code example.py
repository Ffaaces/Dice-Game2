#------------------------------------------------------------------------------------------------------------Dice game--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------





import random
import time

P1Name = input("Player 1 what is your name? ")
print (str("Hello " + P1Name))
time.sleep (1)
P2Name = input("Player 2 what is your name? ")
print (str("Hello " + P2Name))
time.sleep (1)
Password = input ("What is the password? ")

if Password == "ABC":
    print (str("Welcome " + P1Name + " and " + P2Name + " You have succssfully logged in well done enjoy the game"))
    time.sleep(1)
else:
    Password = False
while Password == False:
    password = input("Try re enter the password again ")
    if password == "ABC":
        print (str("Welcome " + P1Name + " and" + P2Name + " You have succssfully logged in well done enjoy the game"))
        Password = True
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------Username and password--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

P1Total = 0
P2Total = 0

for Round in range (1,2):
    P1Score = 0
    P2Score = 0
    P1Dice1 = random.randint (1,6)
    P1Dice2 = random.randint (1,6)
    P1Dice3 = random.randint (1,6)
    P2Dice1 = random.randint (1,6)
    P2Dice2 = random.randint (1,6)
    P2Dice3 = random.randint (1,6)
    P1Subtotal = (P1Dice1 + P1Dice2)
    P2Subtotal = (P2Dice1 + P2Dice2)
    print("Round " +str(Round) + " is now beging")
    time.sleep (1)
    Roll = input("\n" +str (P1Name) + " type roll to roll your 2 dice ")

    if Roll == "Roll" or Roll == "roll":
        print ("\nOn your first dice you rolled a ")
        time.sleep (2)
        print (P1Dice1)
        time.sleep (1)
        print ("On your second dice you rolled a ")
        time.sleep (2)
        print (P1Dice2)
        time.sleep (1)
    else:
        Roll = False
    while Roll == False:
        roll = input ("Please type only Roll to roll your dice ")
        if roll == "Roll" or roll == "roll":
            print ("\nOn your first dice you rolled a ")
            time.sleep (2)
            print (P1Dice1)
            time.sleep (1)
            print ("On your second dice you rolled a ")
            time.sleep (2)
            print (P1Dice2)
            time.sleep (1)
            Roll = True
            P1Subtotal = P1Dice2 + P1Dice1

    if P1Dice1 == P1Dice2:
        print ("You rolled a double you get one more dice")
        time.sleep (1)
        Roll3 = input("\n" +str (P1Name) + " type roll to roll your extra dice ")
        if Roll3 == "Roll" or Roll3 == "roll":
            print ("\nOn your extra dice you rolled a ")
            time.sleep (1)
            print (P1Dice3)
        else:
            Roll3 = False
        while Roll3 == False:
            roll3 = input ("Please type only Roll to roll your dice ")
            if roll3 == "Roll" or roll3 == "roll":
                print ("\nOn your extra dice you rolled a ")
                time.sleep (1)
                print (P1Dice3)
                Roll3 = True

    
    if P1Dice1 == P1Dice2:
        P1Subtotal = P1Dice3 + P1Dice2 + P1Dice1
    else:
        P1Subtotal = P1Dice2 + P1Dice1
            
        
    print ("Your sub total is")
    time.sleep (1)
    print (P1Subtotal)

    P1Total = P1Subtotal+P1Total

    if P1Subtotal % 2 == 0:
        P1Total = P1Total + 10
    else:
        P1Subtotal % 2 != 0
        P1Total = P1Total - 5

    if P1Subtotal % 2 != 0:
        print ("You lose 5 points for rolling a odd number")
        time.sleep (1)
    else:
        if P1Subtotal % 2 == 0:
            print ("You gain 10 points for rolling a even number")
            time.sleep (1)

    if P1Total < 0:
        P1Total = 0

    print ("so your total is " +str (P1Total))

    time.sleep(2)

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------Player one rolling dice and adding score--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


    Roll2 = input("\n" +str (P2Name) + " type roll to roll your 2 dice ")


    if Roll2 == "Roll" or Roll2 == "roll":
        print ("\nOn your first dice you rolled a ")
        time.sleep (2)
        print (P2Dice1)
        time.sleep (1)
        print ("On your second dice you rolled a ")
        time.sleep (2)
        print (P2Dice2)
        time.sleep (1)
    else:
        Roll2 = False
    while Roll2 == False:
        roll2 = input ("Please type only Roll to roll your dice ")
        if roll2 == "Roll" or roll2 == "roll":
            print ("\nOn your first dice you rolled a ")
            time.sleep (2)
            print (P2Dice1)
            time.sleep (1)
            print ("On your second dice you rolled a ")
            time.sleep (2)
            print (P2Dice2)
            time.sleep (1)
            Roll2 = True

    if P2Dice1 == P2Dice2:
        print ("You rolled a double you get one more dice")
        time.sleep (1)
        Rollextra = input("\n" +str (P2Name) + " type roll to roll your extra dice ")
        if Rollextra == "Roll" or Rollextra == "roll":
            print ("\nOn your extra dice you rolled a ")
            time.sleep (1)
            print (P2Dice3)
        else:
            Rollextra = False
        while Rollextra == False:
            roll4 = input ("Please type only Roll to roll your dice ")
            if roll4 == "Roll" or roll4 == "roll":
                print ("\nOn your extra dice you rolled a ")
                time.sleep (1)
                print (P2Dice3)
                Rollextra = True

    if P2Dice1 == P2Dice2:
        P2Subtotal = P2Dice3 + P2Dice2 + P2Dice1
    else:
        P2Subtotal = P2Dice2 + P2Dice1

    print ("Your sub total is")
    time.sleep (1)
    print (P2Subtotal)
    time.sleep (1)

    P2Total = P2Subtotal+P2Total

    if P2Subtotal % 2 == 0:
        P2Total = P2Total + 10
    else:
        P2Subtotal % 2 != 0
        P2Total = P2Total - 5

    if P2Subtotal % 2 != 0:
        print ("You lose 5 points for rolling a odd number")
        time.sleep (1)
    else:
        if P2Subtotal % 2 == 0:
            print ("You gain 10 points for rolling a even number")
            time.sleep (1)

    if P2Total < 0:
        P2Total = 0

    print ("so your total is " +str (P2Total))
    
#----------------------------------------------------------------------------------------------------------Player two rolling dice and adding score------------------------------------------------------------------------------------------
    time.sleep(2)

    print ("After round " +str (Round) + " the scores are")
    time.sleep(1)
    print (str(P1Name + " your score after round " +str (Round) + " is " +str(P1Total) + "\n" +str (P2Name) + " your score after round " +str (Round) + " is " +str (P2Total)))
    time.sleep (1)
    
#----------------------------------------------------------------------------------------------------------Round score------------------------------------------------------------------------------------------

if P1Total > P2Total:
    print (str(P1Name) + " Well done you win!!")
else:
    P1Total < P2Total
    print (str(P2Name) + " Well done you win!!")

if P1Total > P2Total:
    winner = P1Name
    looser = P2Name
else:
    P1Total < P2Total
    winner = P2Name
    looser = P1Name

if P1Total > P2Total:
    score = P1Total
    lscore = P2Total
else:
    P1Total < P2Total
    score = P2Total
    lscore = P2Total

#----------------------------------------------------------------------------------------------------------Defining the winner------------------------------------------------------------------------------------------

db = open ("Winners Log.txt","a+")
db.write ("\n" + "Congrats " +str (winner) + ", you beat " +str (looser) + " With a score of " +str (score)+ " to " +str (lscore))
db.close()

#----------------------------------------------------------------------------------------------------------Scores logged in external file------------------------------------------------------------------------------------------
