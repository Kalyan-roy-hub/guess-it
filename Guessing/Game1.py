class game:
    
    def __init__(self,num):
        self.num= num
    def play(self):
        #n=int(input('Guess the number :'))
        while True:
            n=int(input('Guess the number :'))
            if n < self.num-8:
                print('Your guess is too low..go for a bigger number')
            elif n < self.num-5:
                print('You are close but still lower than the required')
            elif n < self.num:
                print('You can do it..your difference is just +-5')
            elif n == self.num:
                print('You have guessed {} and it is the right answer...CONGRATS'.format(n))
                break
            elif n < self.num+5:
                print('You can do it..your difference is just +-5')
            elif n < self.num+8:
                print('Your guess is too high..go for a smaller number ')
                
            elif n > 20:
                print('You are guessing out of the game range... guess under 20')

            
            
                
                
