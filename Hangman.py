import random


words = ["apple", "banana", "grape", "orange", "mango"]


word = random.choice(words)
guessed_letters = []
tries = 6

print("Welcome to Hangman!")
print("_ " * len(word))

while tries > 0:
    guess = input("Guess a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("Good guess!")
    else:
        print("Wrong guess.")
        tries -= 1


    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    print(display.strip())

    if all(letter in guessed_letters for letter in word):
        print("Congratulations! You guessed the word:", word)
        break
else:
    print("You lost! The word was:", word)
