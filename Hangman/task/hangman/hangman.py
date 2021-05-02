# Write your code here
import random


def game():
    words = ['python', 'java', 'kotlin', 'javascript']
    word = words[random.randint(0, len(words) - 1)]

    attempt = 0
    hint = list('-' * len(word))
    guesses = []
    while attempt < 8:
        print()
        print("".join(hint))

        while True:
            letter = input(f"Input a letter:")

            if letter in guesses:
                print("You've already guessed this letter")
                print()
                print("".join(hint))
                continue

            if len(letter) != 1:
                print("You should input a single letter")
                print()
                print("".join(hint))
                continue

            if not letter.islower():
                print("Please enter a lowercase English letter")
                print()
                print("".join(hint))
                continue

            guesses.append(letter)
            break

        for idx, l in enumerate(list(word)):
            if letter == l:
                hint[idx] = l

        if '-' not in hint:
            break

        if letter not in word:
            print("That letter doesn't appear in the word")
            attempt += 1
            continue

    if "".join(hint) == word:
        print("You guessed the word!")
        print("You survived!")
        print()
    else:
        print("You lost!")
        print()


def main():
    print("H A N G M A N")

    while True:
        play = True if input('Type "play" to play the game, "exit" to quit:') == "play" else False

        if play:
            game()
        else:
            break


main()
