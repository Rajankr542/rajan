print("Hey before the game begin if you are aware or not I would love to let you know the rules>\n1. Rock beats scissors\n2. Scissors beats paper\n3. Paper beats rock \n\nlet the game begins......")
print("choice 1 for 'rock'\n\t2 for paper\n\t3 for scissor")

player1 = input("\nEnter first player name:")
player2 = input("Enter second player name:")
if(player2==""):
    player2='player2'
if(player1==""):
    player1='player1'
elif (player1 == player2):
    player1=''.join((player1,'1'))
    player2 = ''.join((player2, '2'))



def choice1():
    choice1 = input("\nplease make your choice " + player1 + ":")
    if choice1 in [1,'rock','1']:
        choice1 = 1
    if choice1 in [2,'paper','2']:
        choice1 = 2
    if choice1 in [3,'scissor','3']:
        choice1 = 3
    if choice1 in [1, 2, 3, '1', '2', '3', 'rock', 'paper', 'scissor']:
        return choice1
    else:
        repc1()


def choice2():
    choice2 = input("please make your choice " + player2 + ":")
    if choice2 in [1, 'rock', '1']:
        choice2 = 1
    if choice2 in [2, 'paper', '2']:
        choice2 = 2
    if choice2 in [3, 'scissor', '3']:
        choice2 = 3

    if choice2 in [1,2,3,'1','2','3','rock','paper','scissor']:
        return choice2
    else:
        repc2()



def result(choice1,choice2):
    diff=choice1-choice2
    if diff in [-2,1]:
        print("\nHey "+player2+" you got defeted by "+player1+" you are a losser.\n"+player2+" you are a looser all the time hahhahahh.....\nGive it a try be a hero play again")

    if diff in [2,-1] :
        print("\nHey " + player1 + " you got defeted by " + player2 + " you are a losser.\n" + player1 + " you are a looser all the time hahhahahh.....\nGive it a try be a hero play again")
    else:
        print("\nhey you both have made same choice you guys are made for each other hahahhahahhahhah....")

def conex():
    if str(input("\nEner yes if you want to continue else press any key")) in ['yes','Yes']:
        choice1()
        choice2()
        result(x,y)
        conex()
    else:
        exit()
def repc1():
    print("enter a valid input or check spelling")
    choice1()
def repc2():
    print("enter a valid input or check spelling")
    choice2()


x=choice1()
y=choice2()
result(x,y)
conex()


