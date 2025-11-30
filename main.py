#Jada Long
import random

def get_guess():
    #keeps asking until the guess is good
    while True:
        user_letter = input("Guess: ")

        #must be exactly 1 character
        if len(user_letter) != 1:
            print("Your guess must have exactly one character!")
            continue

        #must be lowercase letter
        if not user_letter.islower():
            print("Your guess must be a lowercase letter!")
            continue

        return user_letter


def update_dashes(secret_word, current_dashes, guess_letter):
    #builds a new string showing updated progress
    updated = ""

    for i in range(len(secret_word)):
        if secret_word[i] == guess_letter:
            updated += guess_letter
        else:
            updated += current_dashes[i]

    return updated


def main():
    #a small list of possible mystery words
    word_list = [
        "Jada", "college", "december", "tea", "christmas",
        "bowie", "cyber", "secure", "network", "hacking"
    ]

    #pick one at random to keep things interesting
    secret_word = random.choice(word_list)

    #start with all dashes
    dashes = "-" * len(secret_word)

    #number of wrong guesses allowed
    guesses_left = 5

    #keep going until word is solved OR guesses run out
    while dashes != secret_word and guesses_left > 0:
        print(dashes)
        print(guesses_left, "incorrect guesses left.")

        letter = get_guess()


        if letter in secret_word:
            print("That letter is in the word!")
            dashes = update_dashes(secret_word, dashes, letter)
            guesses_left -= 1
        else:
            print("That letter is not in the word.")
            guesses_left -= 1


    if dashes == secret_word:
        print("You win! The word was: " + secret_word)
    else:
        print("You lose! The word was: " + secret_word)


# run the game
if __name__ == "__main__":
    main()
