import random
import time

def displayIntro():
        print('''You are in a land full of dragons. In front of you,
you see two caves. In one cave, the dragon is friendly
and will share his treasure with you. The other dragon
is greedy and hungry, and will eat you on sight.''')
        print()

def chooseCave():
    cave = ''
    while cave != '1' and cave != '2':
        print('Which cave will you go into? (1 or 2)')
        cave = input()

        return cave

def checkCave(chosenCave):
    print('You approach the cave...')
    time.sleep(2)
    print('It is dark and spooky...')
    time.sleep(2)
    print('YOu aRe VerY SCarD...')
    time.sleep(2)
    print('A large dragon jumps out in front of you! He opens his jaws and...')
    print()
    time.sleep(2)

    friendlyCave = random.randint(1, 2)

    if chosenCave == str(friendlyCave):
        print('Gives you his treasure!')
        afterTreaser() 
    else:  print('Gobbles you down in one bite!')
 
 
    chosenEscape = random.randint(1, 2)
               

def chosenEscape():
         route = ''
         while route != '1' and route != '2':
                print('There are two escape routes, which one will you choose? (1 or 2)')
                route = input()

                return route
def escape():
        if chosenEscape == str(random.randint):
                print('You got away and you never saw those pirates agian... or did you??')
        else:
                print('The pirates caught up to you and stool your gold, and left you deserted on an island...')
        
def afterTreaser():
        
        print('There are pirates that followed you to the treasure and they want it too...')
        
        print('You run away from the gold snatching pirates!')
        
        print("The pirates have swords and they're not going to be friends with you!")
        
        print('You trip on a branch and fall down a hole!')
        
        chosenEscape()
        escape()
                
escape == random.randint(1, 2)

playAgain = 'yes'
while playAgain == 'yes' or playAgain =='y':
    displayIntro()
    caveNumber = chooseCave()
    checkCave(caveNumber)

    print('Do you want to play again? (yes or no)')
    playAgain = input()
            
