while True:
     import random 
     choose=["stone", "paper", "scissor"]
     user= input("choose one : stone paper scissor").lower()
     print("you choose:", user)
     pc=random.choice(choose)
     print("pc choose:", pc)
     if user==pc:
          print("it's a draw")
     elif (user=="stone" and pc=="scissor")or\
          (user=="scissor" and pc=="paper")or\
          (user =="paper" and pc=="stone"):

          print("you won ! 🏆")
     else:
          print("pc won !🏆")   