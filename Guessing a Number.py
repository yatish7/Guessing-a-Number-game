#Guessing the Number Game
import random
class validnumber(Exception):
    pass
class numbertoosmall(Exception):
    pass
class numbertoobig(Exception):
    pass
minimum=int(input("Enter the lower bound of the game: "))
maximum=int(input("Enter the upper bound of the game: "))
n=random.randint(minimum,maximum)
attempts=[]
c=0
print("\n****START GUESSING****\n")
while(1):
    try:
        number=int(input("Enter Number: "))
        c+=1
        print(f"Attempt no: {c}")
        attempts.append(number)
        if minimum>number or maximum<number:
            raise validnumber("Please enter a Valid Number within the boundaries")
        elif number>n:
            raise numbertoobig("**Hint** Please enter a Small Number")
        elif number<n:
            raise numbertoosmall("**Hint** Please enter a Big Number")
        else:
            break
    except (validnumber,numbertoobig,numbertoosmall) as e:
        print(e)
print("\n")
print("Congratulations you have cracked it......")
print(f"The number is {n}")
print(f"The total number of attempts you took to guess: {c}")
reply=input("Do you want to know all your attempts(YES/NO)?? ")
if reply=="YES":
    print(f"Your attempts: {attempts}")
    print("\nCongratulations Once again,Please Come Back and Play again.\n")
else:
    print("\nNo Issues,Congratulations Once again,Please Come Back and Play again.\n")
        
