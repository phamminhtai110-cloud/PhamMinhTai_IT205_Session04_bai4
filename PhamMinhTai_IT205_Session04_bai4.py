import random

print("--- VONG QUAY MAY MAN RIKKEI STORE ---")
print("Ban co 5 luot doan so may man (1-100)")

secret_number = random.randint(1, 100)
max_guesses = 5
guessed_correctly = False

for attempt in range(1, max_guesses + 1):
    guess = int(input(f"\nLuot doan {attempt} - Nhap so cua ban: "))
    
    if guess == secret_number:
        print(f"=> Chuc mung! Ban da doan chinh xac ma so may man!")
        guessed_correctly = True
        break
    elif guess < secret_number:
        print(f"=> Goi y: So cua ban nho hon ma so may man!")
    else:
        print(f"=> Goi y: So cua ban lon hon ma so may man!")

if guessed_correctly:
    print("\n*** CHUC MUNG! Ban da trung thuong qua dac biet! ***")
else:
    print(f"\n*** Rat tiec! Ban da het {max_guesses} luot doan. Ma so may man la {secret_number}. ***")
    print("*** Hen ban dip sau may man hon! ***")

print("--- TRO CHOI KET THUC ---")