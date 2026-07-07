# Software Name: BlackJack  
# Author: Mercent Simukonda 
# License: No license 

# Class for the users account to withdraw and deposit money 
# credit to @khushipillay for the bank account class and function from Medium: My First Python Project: Building a Simple Banking System 
class HouseAccount:
    def __init__(self, balance=0) :
        self.__balance = balance # private attribute so user can't change the balance 



# show user a random set of cards for the dealer but one card is censored and total number is hidden 
# show user a random set of cards and the total number they currently have 

# give the user the option to hit, stand or double down 
# if the users card is 21 do not give them the option -> show dealers card 

# if user hits another card is added. 
# if user stands -> show dealers card 
# if user doubles down -> the bet is doubleded and another card is added 
# If total is above 21 do not give them an option -> show dealers card

# show dealers card

# if the dealers card is less than 17 they keep hitting until its 17 or more 

# if dealers card > 21 and the users card is more than or equal to 17  but less than or equal to 21 the user wins and the bet is added to their total balance 
# if dealers card > 21 and the users card is less than 17 or more than 21 the dealer  wins and the bet is removed from the total balance 
# if dealers card = 21 and the users card is less than 21 or more than 21 the dealer wins and takes the bet 
# if the dealers card = 21 and the users card is 21 its a tie and the bet goes back to the balance
# if the dealers card is more than or equal to 17 but less than or equal to 21 and its the same with the user as well The highest card holder wins 
# if the dealers card is more than or equal to 17 but less than or equal to 21 and its the same with the user but they have the same score the bet is returned to the balance of the user

# give the option for the user to repeat the while loop again or they can exit 

# Class for the users account to withdraw and deposit money 
# credit to @khushipillay for the bank account class and function from Medium: My First Python Project: Building a Simple Banking System 



# Welcome message and instructions for the player 
def main_menu():
    print('''Hi welcome to the London House! Let me explain the rules.
          
    Rules:
        Try to get as close to 21 without going over.
        Kings, Queens, and Jacks are worth 10 points.
        Aces are worth 1 or 11 points.
        Cards 2 through 10 are worth their face value.
        (H)it to take another card.
        (S)tand to stop taking cards.
        On your first play, you can (D)ouble down to increase your bet
        but must hit exactly one more time before standing.
        In case of a tie, the bet is returned to the player.
        The dealer stops hitting at 17.''')

# Menu runs on a while loop
    while True:
        choice = input('How much do you want to bet? :\n Current balance is: 5000 \n 1-5,000 or (Q)uit ') # Ask the user how much they want to bet 
        choice = choice.lower() # users characters are converetd to lowercase when entered 

        if choice >= '5000': # subtract balance based off bet
            #
            break
        elif choice == '2':
            #
            break
        elif choice =='3':
            #
            break
        elif choice == 'q':
            print('Goodbye!')
            break  # menu will keep running until a number from 0 to 3 is entered  
        else:
            print('Invalid choice. Please try again.''')

if __name__ == '__main__': # name main idiom allows the main_menu() function to be executed when running the script 
    main_menu()
