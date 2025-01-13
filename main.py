import random


def select_word():
    with open('words.txt', 'r') as file:
        words = file.readlines()
    return random.choice(words).strip()


def display_word(word, guessed_letters):
    displayed = ''.join([letter if letter in guessed_letters else '_' for letter in word])
    return displayed


def get_user_guess(guessed_letters):
    while True:
        guess = input("შეიყვანეთ ასო: ").upper()
        if len(guess) != 1 or not guess.isalpha():
            print("შეიყვანეთ მხოლოდ ერთი ასო!")
        elif guess in guessed_letters:
            print(f"ასო '{guess}' უკვე გამოცნობილია. სცადეთ სხვა ასო.")
        else:
            return guess


def update_game_state(word, guessed_letters, guess):
    if guess in word:
        guessed_letters.append(guess)
    return guessed_letters


def check_win(word, guessed_letters):
    return all(letter in guessed_letters for letter in word)


def check_game_over(remaining_attempts):
    return remaining_attempts <= 0


def main():
    while True:
        word = select_word()
        guessed_letters = []
        remaining_attempts = 6

        print("თამაშის დაწყება!")

        while True:
            print("\nგამოცნობილი სიტყვა:", display_word(word, guessed_letters))
            print(f"მცდელობები დარჩა: {remaining_attempts}")

            guess = get_user_guess(guessed_letters)
            guessed_letters = update_game_state(word, guessed_letters, guess)

            if guess not in word:
                remaining_attempts -= 1
                print(f"არასწორი ასო! მცდელობები შემცირდა.")

            if check_win(word, guessed_letters):
                print(f"\nგილოცავთ! თქვენ გამოიცანით სიტყვა: {word}")
                break

            if check_game_over(remaining_attempts):
                print(f"\nთქვენი მცდელობები ამოწურულია. სიტყვა იყო: {word}")
                break

        restart = input("გინდა ისევ ითამაშო? (y/n): ").lower()
        if restart != 'y':
            print("გმადლობთ თამაშისთვის!")
            break


