import random

while True:
    number = int(input('How many dice do you want to roll? '))
    if number >= 1 and number <= 3:
        break
    print('You can only roll 1 to 3 dice.')

result = ''
for i in range(number):
    result += str(random.randint(1, 6))
    result += ', '
print(result[:-2])

