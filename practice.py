import random

choice = 'y'

while choice == 'y':
 dice= random.randint(1,6)
 input(print("Enter to role your dice: "))
 print("You roled a: " ,dice)

 choice=input("Would you like to play again(y/n): ")