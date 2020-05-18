'''Write a program which will include a function flip(), that simulates a single flip of a coin: It randomly prints either Heads or Tails.
Accomplish this by choosing 0 or 1 arbitrarily with random.randrange(2), and use an if-else statement to print Heads when the result is 0, and Tails otherwise.
In your main program have a simple repeat loop that calls flip() 10 times to test it, so you generate a random sequence of 10 Heads and Tails.
'''
import random # random module will be imported
def heads_tails(flips):
    no_of_heads=0
    no_of_tails=0
    for i in range(flips):  # for loop is like for i to iterate through range
        number=random.randrange(2)
        if number== 0: #if 0 then heads
            no_of_heads +=1 # for counting number of heads
            print (no_of_heads,'Head')
        else:
            no_of_tails +=1
            print(no_of_tails,'tail')
    print('no_of_heads', no_of_heads)
    print('tails', no_of_tails)
    return;
heads_tails(3)


