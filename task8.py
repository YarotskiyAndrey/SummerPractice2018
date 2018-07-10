import random

attempts = 0
lessThenNine = 0

chance = 0

while attempts <= 10000:
    attempts += 1
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    dice3 = random.randint(1, 6)
    dice4 = random.randint(1, 6)
    if (dice1 + dice2 + dice3 + dice4 < 9):
        lessThenNine += 1

chance = lessThenNine / attempts
chance = round(chance, 3)
print("Chance of getting sum less then nine:", chance)
if chance > 0.1:
    print("You should play this dice")
else:
    print("You shouldn't play this dice")
