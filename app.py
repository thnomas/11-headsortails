import random
import os


coin = ['heads', 'tails']
correct_count = 0

while True:     
    result = random.choice(coin)
    answer = input('Heads or tails? ')

    while answer.lower() not in coin:
        print("please choose heads or tails") 
        answer = input('Heads or tails? ')

    if answer == result:
        correct_count += 1 
    else:
        print(f"The coin landed on {result.upper()}")
        print(f"Game over! your final score was: {correct_count}")
        break
    
    os.system('clear') 
    print(f"The coin landed on {result.upper()}")
    print(f"Correct guesses: {correct_count}")
    
    