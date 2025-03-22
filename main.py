'''
1 for snake 
-1 for water
0 for gun
'''
import random


computer = random.choice([0, 1,-1])
youDict = {"snake":1, "water":-1,"gun":0 }
reverse_dict = {1 : "snake", -1:"water", 0:"gun"}

while True:
    youstr = input("Enter Your Choice (snake, water, gun): ").lower()
    if youstr in youDict:
        break  # Agar input valid hai to loop se bahar aa jao
    print("Invalid choice! Please enter 'snake', 'water', or 'gun'.")

you = youDict[youstr]

print(f"You choose {reverse_dict[you]}\ncomputer choose {reverse_dict[computer]}")

if(computer == you):
    print("It's a Draw")
else:
    if(computer == -1 and you == 1):
        print("You win")

    elif(computer == 1 and you ==0):
        print("You Win")

    elif(computer == 0 and you == -1):
        print("You Win")

    elif(computer == 1 and you ==-1):
        print("Computer Wins")

    elif(computer == 0 and you ==1):
        print("Computer Wins")

    elif(computer == -1 and you == 0):
        print("Computer Wins")

    else:
        print("Something went wrong")

# if((computer - you) == -1 or (computer - you) == 2):
#     print("You lose")
# else:
#     print("You win")