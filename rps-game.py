import random 
import pyttsx3
jarvis = pyttsx3.init()
     
choose=["stone", "paper", "scissor"]
while True:
     
     jarvis.say("Choose stone , paper or scissor")
     jarvis.runAndWait()
     user= input("choose one (stone/paper/scissor/quit):").strip().lower()
     if user == "quit":
          print("Game over !")
          break
     if user not in choose:
          print("Invalid choice")
          continue
     
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
