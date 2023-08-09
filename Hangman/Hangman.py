import random
import string
from words import words


# Function to get a valid word from the list of words
def get_valid_word(words):
    word = random.choice(words)  # randomly chooses something from the list
    while '_' in word or ' ' in word:
        word = random.choice(words)  # Keep choosing until a valid word is found
    return word.upper()


# Main Hangman game function
def hangman():
    # A set is an unordered collection of unique elements in Python.
    # The set() method is used to create a new set from a given iterable (like a list, tuple, or string).
    # It removes duplicate elements and returns a collection of unique elements.

    word = get_valid_word(words)  # Get a valid word to guess
    word_letters = set(word)  # Set of letters in the word
    alphabet = set(string.ascii_uppercase)  # Set of all uppercase letters in the alphabet
    used_letters = set()  # Set to store letters the user has guessed

    lives = len(word)  # Number of lives the player has

    # The join() method is a string method used to concatenate elements of an iterable (like a list) into a single
    # string using a specified separator. It is called on a separator string and takes an iterable as an argument. It
    # returns a new string where the elements of the iterable are joined together with the separator between them.

    # Getting user input and running the game loop
    while len(word_letters) > 0 and lives > 0:
        # Display the number of lives and used letters
        print("You have", lives, "lives left and you have used these letters:", " ".join(used_letters))

        # Display the current state of the word (with guessed letters revealed)
        word_list = [letter if letter in used_letters else "-" for letter in word]
        print("Current word:", " ".join(word_list))

        user_letter = input("Guess a letter: ").upper()

        if user_letter in alphabet - used_letters:
            # Add the guessed letter to the used_letters set
            used_letters.add(user_letter)

            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print(" ")

            else:
                lives = lives - 1
                print("\nYour letter,", user_letter, "is not in the word.")

        elif user_letter in used_letters:
            print('\nYou have already used that letter. Guess another letter.')

        else:
            print("\nThat is not a valid letter.")

    # Game outcome based on the final state
    if lives == 0:
        print("You died, Sorry. The word was", word)
    else:
        print("YAAAY! YOU GUESSED THE WORD!!!!")


hangman()
