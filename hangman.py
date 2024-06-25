import random

def choose_word():
    words = ["apple", "banana", "cherry", "orange", "grape"]
    return random.choice(words)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

def display_hangman(tries):
    stages = [
        """
           _______
          |       |
          |       
          |       
          |       
          |       
        _|_
        """,
        """
           _______
          |       |
          |       O
          |       
          |       
          |       
        _|_
        """,
        """
           _______
          |       |
          |       O
          |       |
          |       
          |       
        _|_
        """,
        """
           _______
          |       |
          |       O
          |      /|
          |       
          |       
        _|_
        """,
        """
           _______
          |       |
          |       O
          |      /|\\
          |       
          |       
        _|_
        """,
        """
           _______
          |       |
          |       O
          |      /|\\
          |      / 
          |       
        _|_
        """,
        """
           _______
          |       |
          |       O
          |      /|\\
          |      / \\
          |       
        _|_
        """
    ]
    return stages[tries]

def hangman():
    word = choose_word()
    guessed_letters = []
    tries = 0
    max_tries = len(display_hangman(0)) - 1
    
    print("Welcome to Hangman!")
    print(display_hangman(tries))
    print(display_word(word, guessed_letters))

    while tries < max_tries:
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter!")
        elif guess in word:
            guessed_letters.append(guess)
            if display_word(word, guessed_letters) == word:
                print(f"Congratulations! You guessed the word '{word}'!")
                return
        else:
            tries += 1

        print(display_hangman(tries))
        print(display_word(word, guessed_letters))

    print("Sorry, you ran out of tries! The word was:", word)

hangman()