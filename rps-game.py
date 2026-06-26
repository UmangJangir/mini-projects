import random 
import pyttsx3
jarvis = pyttsx3.init()

choose=["stone", "paper", "scissor"]
while True:
     
     jarvis.say("Choose stone , paper or scissor")
     jarvis.runAndWait()
     user= input("choose one (stone/paper/scissor/quit):").strip().lower()
     jarvis.say(f"you choose {user}")
     jarvis.runAndWait()

     if user == "quit":
          print("Game over !")
          
          jarvis.say("Game over!")
          jarvis.runAndWait()
          break
     if user not in choose:
          print("Invalid choice")
          continue
     
     print("you choose:", user)
     pc=random.choice(choose)
     print("pc choose:", pc)
     jarvis.say(f"pc choose {pc}")
     jarvis.runAndWait()
     if user==pc:
          print("it's a draw")
          jarvis.say("it's a draw")
          jarvis.runAndWait()
     elif (user=="stone" and pc=="scissor")or\
          (user=="scissor" and pc=="paper")or\
          (user =="paper" and pc=="stone"):

          print("you won ! 🏆")

          jarvis.say("you won")
          jarvis.runAndWait()
     else:
          print("pc won !🏆")     
          jarvis.say("pc won")
          jarvis.runAndWait()
