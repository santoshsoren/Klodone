
import random

secret_number = random.randint(1,100)

chance = 0

while chance < 5:
     guess_number = int(input("Enter your number: "))

     if guess_number == secret_number:
         print("Congratulation you win..!")
         break
     elif guess_number > secret_number:
         print("your number is greater than secret number try again..!")
     else:
         print("your number is smaller than secret number try again..!")

     chance += 1

if not chance < 5:
    print("You used your all chancees!! Game Over...!!!")
    print("Secret number is: ",secret_number)
    
