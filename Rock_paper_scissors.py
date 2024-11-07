import random
print('Winning rules of the game ROCK PAPER SCISSORS are \n'
 + "Rock vs Paper -> Paper wins \n " 
+ "Rock vs Scissors -> Rocks Wins \n"
+ " Paper vs Scissors -> Scissors wins \n")

while True:
    print("Enter your choice \n 1 - Rock\n 2 - paper\n 3- Scissors \n")
    choice = int(input("Enter Your choice: "))

    while choice > 3 or choice < 1:
        choice = int(input("Enter a valid choice please: "))
    if choice == 1:
        choice_name = 'Rock'
    elif choice == 2:
        choice_name = 'Paper'
    else:
        choice_name = 'Scissors'
    print('User choice is: ', choice_name)
    print("Now it's Computer Turn... ")
    comp_choice = random.randint(1, 3)


    if comp_choice ==  1:
        comp_choice_name = 'Rock'
    elif comp_choice == 2:
        comp_choice_name = 'Paper'
    else:
        comp_choice_name = 'Scissors'
    

    print("Computer choice is: ", comp_choice_name)
    print(choice_name, 'vs', comp_choice_name)

    if choice == comp_choice:
        result = 'DRAW'
    elif (choice ==1 and comp_choice == 2) or (comp_choice ==1 and choice==2):
        result  = 'Paper'
    elif (choice == 1 and comp_choice_name == 3) or (comp_choice == 1 and choice==3):
        result = 'Rock'
    elif (choice ==2 and comp_choice_name==3) or (comp_choice == 2 and choice ==3):
        result = 'Scissors'
    if result ==  'DRAW':
        print("<== it is a tie==>")
    elif result == choice_name:
        print("<== User Wins! ==> ")
    else:
        print("<==Computer wins!==>")
    

    print('Do you want to play again? Y/N')
    ans = input().lower()
    if ans == 'n':
        break
    print("Thanks for playing! ")