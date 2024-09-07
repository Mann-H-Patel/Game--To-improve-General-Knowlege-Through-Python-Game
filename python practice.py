import random
from hangman_art import stages, logo
from name_list import marvel_heroes_with_hints, cricketers_with_hints, bollywood_heroes_with_hints, indian_cities_with_hints,indian_historical_places_with_hints, indian_cuisines_with_hints

print(logo)

choose_list = int(input("""From Which List Do You Like To Guess Name =>
                        input [0] to choose Marvel Hero List, 
                        input [1] For Criketer List, 
                        input [2] For Bollywood Hero List,
                        input [3] For Indian Cities List,
                        input [4] For Historical Places List,
                        input [5] For Indian Cusine List =>  """))

if choose_list == 0:
    random_hero_tuple = random.choice(marvel_heroes_with_hints)
elif choose_list == 1:
    random_hero_tuple = random.choice(cricketers_with_hints)
elif choose_list == 2:
    random_hero_tuple = random.choice(bollywood_heroes_with_hints)
elif choose_list == 3:
    random_hero_tuple = random.choice(indian_cities_with_hints)
elif choose_list == 4:
    random_hero_tuple = random.choice(indian_historical_places_with_hints)
elif choose_list == 5:
    random_hero_tuple = random.choice(indian_cuisines_with_hints)    
else:
    print("Enter Correct Letter Please => ")    
        
random_hero = random_hero_tuple[0]
hint = random_hero_tuple[1]

# Number of lives
lives = 6

# Placeholder for displaying the word with underscores
placeholder = ""
for _ in random_hero:
    placeholder += "_"

print(f"Hint: {hint}")  # Display the hint for the randomly selected hero
print(placeholder)  # Initial display of underscores

# Variable to track the game status
game_status = False
correct_letters = []  # List to store correctly guessed letters

while not game_status:
    display = ""
    guess = input("Guess A Letter: ").lower()

    if(guess == random_hero):
        print("You Win")
        game_status = True
    else:
        # If the letter has already been guessed
        if guess in correct_letters:
            print(f"You already chose the letter '{guess}'. Try again.")
        else:
            # Check if the guessed letter is in the word
            for letter in random_hero:
                if letter == guess:
                    display += guess
                    correct_letters.append(guess)
                elif letter in correct_letters:
                    display += letter  # Keep correctly guessed letters visible
                else:
                    display += "_"

            print()

            # If the guess was wrong, decrease lives
            if guess not in random_hero:
                lives -= 1
                print("You lost a life.")
                print(f"********[{lives}/6]********")
                print()
            else:
                print(f"********[{lives}/6]********")
                print()

            print(stages[lives])  # Show the current stage of the hangman
            print(display)  # Display the current state of the word
            print()
            # If no lives are left, the game is over
            if lives == 0:
                game_status = True
                print("Game over! You lost.")
                print(f"The correct hero was {random_hero}")

            # If there are no underscores left, the player has won
            if "_" not in display:
                game_status = True
                print("Congratulations! You guessed the hero correctly.")
