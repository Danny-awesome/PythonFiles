import random

def getWords() :
    words = ['photosynthesis','diabetes','calamity','grateful','attitude']

    return random.choice(words).upper()

def check(word, guesses_made, my_guess) :
    my_guess = my_guess.upper()
    flag_status = ''
    i = 0;
    match = 0 
    for letter in word:
        if letter in my_guess :
            flag_status += letter
        else :
            flag_status += ''

        if letter == my_guess :
            match += 1

    if match > 1 :
        print('Word contains{0} {1}s'.format(match, my_guess))
    elif match == 1 :
        print('Word contains {0}'.format(my_guess))
    else :
        print('Word does not contain {0}'.format(my_guess))

    return flag_status

def main() :
    word = getWords()
    guesses_made = []
    flag_guessed = False
    print('The word contains {0} letters'.format(len(word)))
    while not flag_guessed:
        my_guess = input('enter one letter or a {0} letter words: '.format(len(word)))
        my_guess = my_guess.upper()
        if my_guess in guesses_made:
            print("'{0}' already guessed by you.")
        elif len(my_guess) == len(word):
            guesses_made.append(my_guess)
            if my_guess == word:
                flag_guessed = True
            else:
                print('incorrect')
        elif len(my_guess) == 1:
            guesses_made.append(my_guess)
            result = check(word, guesses_made, my_guess)
            if result == word:
                flag_guessed = True
            else:
                print(result)
        else:
            print('entry is not valid')
    print('Congrats. Word completed : '+word)
    print('Number of tries = {0}'.format(len(guesses_made)))

if __name__ == "__main__":
    main()