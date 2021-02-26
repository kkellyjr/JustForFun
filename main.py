# Generate your questions & answers below:
#What will be difficult?
  #Looping through options for which hand to play
#How to randomize computer's hand? What to import?
  #from random import randrange, randrange (1,4)
#How to pull data as to who wins?
  #display both hands, assign variables to each possible hand
#How to take into account all of the different final hand combinations
  #write possibilities, then combine and condense code later
  #add comment

from random import randrange

#Ask user to select which item they want to play for this round
print("Select your hand for this round.")
user_input = int(input("Enter 1 for Rock, 2 for Paper, or 3 for Scissors to play as your hand for this round: "))
if user_input == 1:
  print("The user has chosen Rock")
elif user_input == 2:
  print("The user has chosen Paper")
else:
  print("The user has chosen Scissors")

#Generate computer's hand
computers_hand = randrange(1,4)

#Print computer's hand
if computers_hand == 1:
    print("The computer has chosen Rock")
elif computers_hand == 2:
    print("The computer has chosen Paper")
else:
    print("The computer has chosen Scissors")

#Decide who wins

if (user_input == computers_hand):
  print("This round is a tie")
elif user_input == 1 and computers_hand == 2:
  print("The computer has won")
elif (user_input == 3 and computers_hand == 2):
  print("The user has won")
elif (user_input == 1 and computers_hand == 3):
  print("The user has won")
elif (user_input == 2 and computers_hand == 1):
  print("The user has won")
elif (user_input == 2 and computers_hand == 3):
  print("The computer has won")
#elif (user_input == 3 and computers_hand == 1):
else:  
  print("The computer has won")