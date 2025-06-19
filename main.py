import random

def generate_secret_number():
    while True:
        digits = [str(random.randint(0, 9)) for i in range(0, 4)]
        
        if len(set(digits)) == len(digits): # Check for duplicates
            return "".join(digits)
        
            
def get_user_guess(prompt):
    while True:
        guess = input(prompt)
        
        if not guess.isdigit():
            print("Invalid input: Please enter only digits.\n")
            continue
            
        if len(guess) != 4:
            print("Invalid input: The number must be 4 digits long.\n")
            continue

        if has_duplicate_digits(guess):
            print("Invalid input: The number must have 4 different digits.\n")
            continue
            
        return guess
            
def has_duplicate_digits(number_str):
    return len(set(number_str)) != len(number_str)

def calculate_cows_bulls(secret_number, guess):
    cows = 0
    bulls = 0
    
    for i in range(0, 4):
        if guess[i] == secret_number[i]:
            cows += 1
        elif guess[i] in secret_number:
            bulls += 1
            
    return cows, bulls 

def play_game():
    print("Welcome to Cows and Bulls!\n")

    while True:
        secret_number = generate_secret_number()
        num_guesses = 0


        while True:
            guess = get_user_guess("Guess a 4-digit number: ")
            num_guesses += 1
            
            cows, bulls = calculate_cows_bulls(secret_number, guess)
            
            if cows == 4:
                print(f"\nCongratulations! You guessed the number {secret_number} in {num_guesses} guesses!\n")
                break
            else:
                print(f"Wrong! Cows: {cows}, Bulls: {bulls}\n")
        
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing! Goodbye.")
            break

if __name__ == "__main__":
    play_game()
