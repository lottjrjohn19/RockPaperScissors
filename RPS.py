from random import randint

choice = input('rock (r), paper (p) or scissors (s)?')
print(choice, 'vs ', end='')

chosen = randint(1, 3)
# print(chosen)

if chosen == 1:
    computer = 'r'
elif chosen == 2:
    computer = 'p'
else:
    computer = 's'

print(computer)

if choice == computer:
    print('DRAW')
elif choice == 'r' and computer == 's':
    print('Player wins!')
elif choice == 'r' and computer == 'p':
    print('Computer wins!')
elif choice == 'p' and computer == 'r':
    print('Player wins!')
elif choice == 'p' and computer == 's':
    print('Computer wins!')
elif choice == 's' and computer == 'p':
    print('Player wins!')
elif choice == 's' and computer == 'r':
    print('Computer wins!')
