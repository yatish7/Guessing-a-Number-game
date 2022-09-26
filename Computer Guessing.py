#Guessing a Number(computer is guessing here)
import random
class validnumber(Exception):
    pass
class numbertoosmall(Exception):
    pass
class numbertoobig(Exception):
    pass
lower_bound=int(input("Enter the lower bound of the game: "))
upper_bound=int(input("Enter the upper bound of the game: "))
attempts=[]
count=0
user_number=int(input("Enter the number which you want the computer to guess: "))
if user_number>upper_bound or user_number<lower_bound:
    print("Enter a valid number to guess within the boundaries.....")
else:
 print("\n******The Computer is starting to guess the number******\n")
 while(1):
    try:
      computer_guess=random.randint(lower_bound,upper_bound)
      count+=1
      print(f"Attempt no: {count}")
      print(f"The computer's guess is {computer_guess}")
      attempts.append(computer_guess)
      if computer_guess>user_number:
          upper_bound=computer_guess-1 # as both are inclusive in random
          raise numbertoosmall("Hint: Aim lower computer")
      elif computer_guess<user_number:
          lower_bound=computer_guess+1 #as both the arguments are inclusive in random
          raise numbertoobig("Hint: Aim higher computer")
    except numbertoosmall as e:
        print(e)
    except numbertoobig as e:
        print(e)
    if computer_guess==user_number:
        print("\nYou guessed it right computer,Great Job!...")
        print(f"\nThe number is {user_number}")
        break
 print("The total number of attempts taken: ",count)
 print("The guesses computer made in the process are: ",attempts)
 print("\nThanks for making me play the game 'YATISH', really had a great time...")
 print("--------Looking forward to playing with you again soon--------")
    
    
    
