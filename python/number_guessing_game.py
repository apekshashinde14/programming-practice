import random
print("=======NUMBER GUESSING GAME========")
play_again = True
while play_again:
    secret_number = random.randint(1,100)
    attempt=0
    while True:
        try:
            guess=int(input("Guess Your Number between 1 to 100: "))
            if guess < 1 or guess > 100 :
                print("Please enter a number between 1 and 100.")
                continue
            attempt+=1
        except ValueError:
            print("Please enter a valid number")
            continue
        if guess==secret_number:
            print("Congratulations!!!")
            print(f'Total Attempt : {attempt}')
            break
        elif attempt == 7 :
            print("Game Over!!")
            print(f"Secret Number is {secret_number} ")
            break
        elif guess > secret_number:
            print("Too High!!")
        elif guess < secret_number:
            print("Too Low!!")

    while True:
        choice = input("Do you want to play again ? (yes/no) : ").strip.lower()
        if choice == 'yes':
            break
        elif choice == 'no':
            print("Good Bye!! See you again..")
            play_again=False
            break
        else :
            print("Invalid Choice!!")
            continue