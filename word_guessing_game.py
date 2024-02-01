import random
words = ['rainbow', 'computer', 'science', 'programming',
         'python', 'mathematics', 'player', 'condition',
         'reverse', 'water', 'board', 'geeks']

#####
def displayGame(word):
    for letter in word:
        print(letter)
#####

#####
def startGame():
    name = input('What is your name? ')
    print('Good luck!', name)

    cycle = 11
    random_word = random.choice(words)
    word = '-'*len(random_word)
    
    print('Guess the characters')
    displayGame(word)

    while cycle >= 0:
        if '-' not in word: # user wins the game
            print('You win!')
            print('The word is:', random_word)
            return 0

        res = input('guess a character: ') # get a character from user & check if it is a character
        if len(res) != 1:
            print('*'*11 + '\nWRONG INPUT\n' + '*'*11)
            continue

        if res in random_word: # if res is in random_word, then show all the letters that equals to res
            for i in range(len(random_word)):
                if random_word[i] == res:
                    word = word[:i] + res + word[i+1:]
            
            displayGame(word)

        else: # user entered a wrong input (a character that is not in random_word)
            print('Incorrect, You have', cycle, 'chances left')
            cycle -= 1
            displayGame(word)
            continue

    print('You lost!')
    print('The word is:', random_word)
#####

startGame()