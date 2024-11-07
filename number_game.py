def nearest_Mutiple(num):
    if num >4:
        near = num+ (4-(num%4))
    else:
        near = 4
    return near
def lose1():
    print("\n\n You Lose")
    print("Better luck next time")
    exit(0)
def check(xyz):
    i = 1
    while i<len(xyz):
        if (xyz[i]-xyz[i-1])!=1:
            return False
        i = i+1
        return True

def start1():
    xyz = []
    last =0
    while True:
        print("Enter 'F' to take the first chance")
        print("Enter 'S' to take the second chance")
        chance = input('>')

        if chance == 'F':
            while True:
                if last == 20:
                    lose1()
                else:
                    print("\n\n Your Turn")
                    print("\nHow many number do you wish to enter ")
                    inp = int(input('> '))

                    if inp > 0 and inp <= 3:
                        comp = 4 - inp
                    else:
                        print("Wrong input you are disqualified from the game. ")
                        lose1()
                    i, j = 1, 1
                    print("Now enter the values")
                    while i <=inp:
                        a = input('>')
                        a = int(a)
                        xyz.append(a)
                        i = i+1

                    last = xyz[-1]
                    if check(xyz) == True:
                        if last == 21:
                            lose1()
                        
                        else:
                            # computer turn
                            while j <= comp:
                                xyz.append(last+1)
                                j = j+1
                            print("Order of input after computer's turn is: ")
                            print(xyz)
                            last = xyz[-1]
                    else:
                        print("\n You did not input consecutive integers. ")
                        lose1()
        

        elif chance == "S":
            comp = 1
            last=0

            while last < 20:
                j=1
                while j <= comp:
                    xyz.append(last + j)
                    j =j + 1
                print("Order of inputs after computers turn is: ")
                print(xyz)
                if xyz[-1]==20:
                    lose1()
                else: 
                    print("\n Your turn.")
                    print("\n How many numbers do you wish to enter? ")
                    inp = int(input('>'))
                    i = 1
                    print("Enter Your Values")
                    while i <=inp:
                        xyz.append(int(input('>')))
                        i = i+1
                    last = xyz[-1]
                    if check(xyz) == True:
                        near = nearest_Mutiple(last)
                        comp = near - last
                        if comp == 4:
                            comp = 3
                        else:
                            comp = comp
                    else:
                        print("You did not input consecutive integers. ")

                        lose1()
            print("\nCONGRATULATIONS !!!")
            print("YOU WON! ")
            exit(0)
        else:
            print("Wrong choice")
game = True
while game == True:
    print("Player 2 is computer")
    print("Do you want to play the 21 number game? (Yes/No)")
    ans = input('> ')
    if ans == 'Yes':
        start1()
    else:
        print("Do you want quit the game? (yes/no)")
        nex = input('> ')
        if nex== 'yes':
            print("You are quitting the game...")
            exit(0)
        elif nex == 'no':
            print("continuing... ")
        else: 
            print("wrong choice")