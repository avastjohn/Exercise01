# greet player
    # get player name
    # choose random number between 1 and 100
    # while True:
        # get guess
        # if guess is incorrect:
            # give hint
        # else:
            # congratulate player





from random import randint

print "Greetings earthling! What's your name?"
name = raw_input()

print "What a pleasure to meet you, %s ! I have a game for you." % name
print "I'm thinking of a number between 1 and 100. Try to guess my number."
guess = int(raw_input())

number = randint (1,101)
while guess != number:
    if guess < number:
        print "Your number is too low, guess again."
    else:
        print "Your number is too high, guess again."
    guess = int(raw_input())
        
print "You win! Bravo!"