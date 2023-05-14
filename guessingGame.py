from random import shuffle

def shuffle_list (mylist):
    shuffle(mylist)
    return (mylist)

def players_guess ():
    guess = ''
    
    while guess not in ['0','1','2','3','4']:
        guess = input("What is your guess? Pick a number from 0, 1, 2, 3 or 4:  ")
    return int(guess)

def check_guess(mylist,guess):
    if mylist[guess] == 'O':
        print ("Congratulations")
    else:
        print("WRONG")
        print(mylist)
        
mylist = ['','','O','','']

mixedup_list = shuffle_list(mylist)

guess = players_guess()

check_guess(mylist, guess)