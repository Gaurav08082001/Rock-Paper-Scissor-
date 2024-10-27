import random
item_list = ['Rock', 'Paper', 'Scissor']

user_Input = input("Please enter your move- Rock, Paper or Scissor: ")
comp_Input = random.choice(item_list)

print(f"User input is {user_Input} and Computer input is {comp_Input}.")

if user_Input == comp_Input:
    print("Both choices are same. Match tie")

elif user_Input == "Rock":
    if comp_Input == "Paper":
        print("Computer wins because Paper covers Rock")
    else:
        print("User wins because Rock smashes Scissor")

elif user_Input == "Paper":
    if comp_Input == "Scissor":
        print("Computer wins because Scissor cuts Paper")
    else:
        print("User wins because Paper covers Rock")

elif user_Input == "Scissor":
    if comp_Input == "Rock":
        print("Computer wins because Rock smashes Scissor")
    else:
        print("User wins because Scissor cuts Paper")