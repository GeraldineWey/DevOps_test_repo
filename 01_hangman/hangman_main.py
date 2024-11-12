import random

# Mirrored ASCII art for the hangman stages with 8 stages total
HANGMAN_PICS = [
    '''
     +---+
     |    
     |    
     |    
    ===''', '''
     +---+
     |   O
     |    
     |    
    ===''', '''
     +---+
     |   O
     |   |
     |    
    ===''', '''
     +---+
     |   O
     |  /|
     |    
    ===''', '''
     +---+
     |   O
     |  /|\
     |    
    ===''', '''
     +---+
     |   O
     |  /|\
     |    \
    ===''', '''
     +---+
     |   O
     |  /|\
     |  / 
    ===''', '''
     +---+
     |   O
     |  /|\
     |  / \
    ==='''
]

# List of words
WORDS = [
    "Algorithm",
    "Bias",
    "Clustering",
    "Dataframe",
    "Exploration",
    "Feature",
    "Gradient",
    "Hypothesis",
    "Imputation",
    "Jupyter",
    "Kernel",
    "Linear",
    "Modeling",
    "Normalization",
    "Outlier",
    "Prediction",
    "Query",
    "Regression",
    "Sampling",
    "Tensor",
    "Unsupervised",
    "Visualization",
    "Workflow",
    "XGBoosting",
    "Yield",
    "Zscore"
]

def get_random_word(word_list):
    """Select a random word from the provided list."""
    return random.choice(word_list).upper()

def display_game_state(hangman_pics, missed_letters, correct_letters, secret_word):
    """Display the current state of the game, including ASCII art and guessed letters."""
    print(hangman_pics[len(missed_letters)])
    print("\nMissed letters:", " ".join(missed_letters))

    # Show the guessed word with unguessed letters as underscores
    display_word = [letter if letter in correct_letters else '_' for letter in secret_word]
    print("Word:", " ".join(display_word))

def play_hangman():
    print("Welcome to Hangman!")
    secret_word = get_random_word(WORDS)
    missed_letters = []
    correct_letters = []
    game_over = False

    while not game_over:
        display_game_state(HANGMAN_PICS, missed_letters, correct_letters, secret_word)

        guess = input("\nGuess a letter: ").upper()

        if guess in missed_letters + correct_letters:
            print("You've already guessed that letter. Try again.")
            continue

        if guess in secret_word:
            correct_letters.append(guess)

            # Check if the player has won
            found_all_letters = all(letter in correct_letters for letter in secret_word)
            if found_all_letters:
                display_game_state(HANGMAN_PICS, missed_letters, correct_letters, secret_word)
                print("\nCongratulations! You've guessed the word:", secret_word)
                game_over = True
        else:
            missed_letters.append(guess)

            # Check if the player has lost
            if len(missed_letters) == len(HANGMAN_PICS) - 1:
                display_game_state(HANGMAN_PICS, missed_letters, correct_letters, secret_word)
                print("\nGame Over! The word was:", secret_word)
                game_over = True

    # Ask if the player wants to play again
    if input("Play again? (Y/N): ").upper() == 'Y':
        play_hangman()

# Start the game
play_hangman()
