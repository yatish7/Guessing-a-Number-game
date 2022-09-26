#Guessing the Number Game by the User
import random
class validnumber(Exception):
    pass
class numbertoosmall(Exception):
    pass
class numbertoobig(Exception):
    pass
lower_bound=int(input("Enter the lower bound of the game: "))
upper_bound=int(input("Enter the upper bound of the game: "))
computer_number=random.randint(lower_bound,upper_bound)
attempts=[]
count=0
print("\n****START GUESSING****\n")
while(1):
    try:
        user_guess=int(input("Enter Number: "))
        count+=1
        print(f"Attempt no: {count}")
        attempts.append(user_guess)
        if lower_bound>user_guess or upper_bound<user_guess:
            raise validnumber("Please enter a Valid Number within the boundaries")
        elif user_guess>computer_number:
            raise numbertoobig("**Hint** Please enter a Small Number")
        elif user_guess<computer_number:
            raise numbertoosmall("**Hint** Please enter a Big Number")
        else:
            break
    except (validnumber,numbertoobig,numbertoosmall) as e:
        print(e)
print("\n")
print("Congratulations you have cracked it......")
print(f"The number is {computer_number}")
print(f"The total number of attempts you took to guess: {count}")
reply=input("Do you want to know all your attempts(s/no)?? ")
if reply=="s":
    print(f"Your attempts: {attempts}")
    print("\nCongratulations Once again,Please Come Back and Play again.\n")
else:
    print("\nNo Issues,Congratulations Once again,Please Come Back and Play again.\n")
        
