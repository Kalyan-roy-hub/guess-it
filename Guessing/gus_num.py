import random,time


num = random.randint(1,20)
from Guessing import Game1
print('Hello, I am JARVIS..welcome to my number guessing game...')
time.sleep(2)
print('I have a number for you to guess..Are you up for the challenge?..say yes or no')
ans=input('say yes or no :')
if ans == 'yes' or ans == 'Yes':
    print('Hey there ...this is JARVIS')
    print('You opted to play my guessing game..')
    print('I chose a number in between 1 and 20 including them both..please guess the number')
    g= Game1.game(num)
    g.play()
    
else:
    print('thank you...have a nice day')
    
    
