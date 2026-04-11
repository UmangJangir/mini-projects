import random
guess=["0","1","2","3","4","5","6","7","8","9"]
user=int(input("enter number from 0 to 9"))
pc=random.choice(guess)
print("you choose:",user)
print("pc choose:",pc)
if pc==user:
    print("correct guess")
else:
    print("Game over! number was:",pc)    