import random

class Word_list:
    def __init__():
        words = ['lyrical', 'learned', 'bait', 'murky', 'left', 'imagine', 'five', 'rely', 'tight', 
            'entertaining', 'even', 'auspicious', 'broad', 'snails', 'decorous', 'feeble', 'doll', 
            'protect', 'fine', 'befitting', 'freezing', 'worry', 'lace', 'faint', 'interesting', 
            'scrape', 'uttermost', 'flagrant', 'lavish', 'enjoy', 'blot', 'cheer', 'fat', 'gun', 'machine', 
            'mellow', 'mark', 'flow', 'leather', 'whirl', 'cherries', 'tenuous', 'cracker', 'adhesive', 
            'hill', 'farm', 'dramatic', 'arch', 'birds', 'dam', 'wood', 'whisper', 'hug', 'bucket', 'pets', 
            'invincible', 'wiggly', 'thing', 'wide-eyed', 'corn', 'medical', 'preserve', 'behavior', 
            'steam', 'mute', 'can', 'fairies', 'icy', 'cross', 'field', 'humor', 'concern', 'political', 
            'protest', 'pale', 'nauseating', 'stranger', 'rule', 'wail', 'detail', 'conscious', 
            'mountainous', 'squeal', 'beginner', 'clumsy', 'majestic', 'town', 'stormy', 'adjoining', 
            'decisive', 'veil', 'reach', 'whimsical', 'tip', 'bridge', 'launch', 'insect', 'awake', 'mine', 
            'quiver']
        return words

class Parachute_list:
    def __init__():
        parachute = [
            '  ___  ',
            ' /___\ ',
            ' \   / ',
            '  \ /  ',
            '   o   ',
            '  /|\  ',
            '  / \  ',
            '       ',
            '^^^^^^^',
        ]
        return parachute

class Guess_lists:
    def __init__():
        word_letters = []
        word_spaces = []
        incorrect_guesses = []
        return word_letters, word_spaces, incorrect_guesses

words = Word_list.__init__()
parachute = Parachute_list.__init__()
word_letters, word_spaces, incorrect_guesses = Guess_lists.__init__()


the_word = random.choice(words)
for letter in the_word:
    word_letters.append(letter)
    word_spaces.append('_')


# runs game
game_over = False
fails = 0
while game_over == False:
    #print spaces for word
    print()
    for space in word_spaces:
        print(space, end=' ')

    #print parachute
    print()
    for line in parachute:
        print(line)

    #prints wrong guesses
    if fails > 0:
        print('Incorrect Guesses: ', end = '')
        for letter in incorrect_guesses:
            print(letter, end=' ')
    print() 

    #checks and replaces guessed letter  
    guessed_letter = input('Guess a letter: (a-z) ')
    guess_result = False
    for i in range(len(word_letters)):
        if guessed_letter == word_letters[i]:
            word_spaces[i] = guessed_letter
            guess_result = True

    # adds fail counter if necessary
    if guess_result == False:
        fails += 1
        parachute[0] = ' '
        incorrect_guesses.append(guessed_letter)
    
    #ends game
    if fails == 5:
        game_over = True
        print()
        print('You Lose')
        print()
    if word_letters == word_spaces:
        game_over = True
        class Win:
            def finish():
                print()
                print('You Win')
                print(f'The word was: {the_word}')
                print()
        Win.finish()

    

