import random
import hangman_logo
import hangman_words
import hangman_asciiart

print(hangman_logo.logo)
exit_game = False

while not exit_game:
    end = False
    stage = 0
    current_word = random.choice(hangman_words.words)
    size = len(current_word)
    char_remain = size - 2
    display = []
    ip = " "

    for i in range(size):
        if i == 0 or i == size - 1:
            display.append(current_word[i])
        else:
            display.append("_")
    
    print(display)
    while not end:
        choice = input("\nGuess a letter : ")
        
        # check whether the letter already entered
        if ip.count(choice) != 0:
            print(f"'{choice}' is already there.")
        
        else:
            ip += choice
            # wrong guess
            if current_word[1:size - 1].count(choice) == 0:
                print("Sorry! Letter is not in the word.")
                print("You lost one life")
                print(f"{6-stage} life ramaining")
                print(hangman_asciiart.hangmanpics[stage])
                stage += 1
            # correct guess
            else:
                print("Great! You guessed it correctly.")
                char_remain = char_remain - current_word[1:size-1].count(choice)
                for i in range(size):
                    if current_word[i] == choice:
                        display[i] = choice
            
        print(display)
        if stage>= 7:
            print(hangman_logo.lost)
            end = True
            print(f"The correct word is : {current_word}.")
        elif char_remain == 0:
            print(hangman_logo.won)
            end = True
    
    play = input("Do you want to play more (y, n) : ").lower()
    if play != "y":
        exit_game = True