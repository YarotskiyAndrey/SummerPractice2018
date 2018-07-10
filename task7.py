import random

analitSolution = (1 / 3) - (1 / 36)
analitSolution = round(analitSolution, 3)

attempts = 0
numOfSixes = 0

chance = 0

while chance != analitSolution:
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    if (dice1 == 6 or dice2 == 6):
        numOfSixes += 1
    attempts += 1
    if numOfSixes != 0:
        chance = numOfSixes / attempts
        chance = round(chance, 3)
print("Chance of getting six:", chance)
print("Number of attempts:", attempts)
