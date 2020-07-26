import random

numberWanted = int(input("How many times do you want the coin to flip: "))

side = ["Heads", "Tails"]


numberPicked = numberWanted
numberWanted = numberWanted - numberWanted

while numberWanted <= numberPicked:
  print("The coin flipped " + str(numberWanted) + " times and you got " + random.choice(side))
  numberWanted += 1


