#ADGROCKPAPERSCISSORS
#(1 = Rock)
#(2 = Paper)
#(3 = Scissors)

#Lib
import random
import time
from os import system, name 
#GameVar
arrGameObj = ['Rock','Paper','Scissors']
UserChoice = 0
bPass = False
Outcome = "You picked {} and computer picked {}"
#RandomVar
comp = random.randint(1, 3)

#clearscreen
def clear(): 
 # for windows 
 if name == 'nt': 
  _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
 else: 
  _ = system('clear') 

#art
def printborder():
 print('----------------------------------')
 
#Gameplay
def printChoices(human,compchoice):
 print(Outcome.format(arrGameObj[int(human-1)],arrGameObj[int(compchoice-1)]))

def Start(choice):
 if choice == comp:     
  printborder()
  print('Draw')
  printChoices(choice,comp)
 if choice == 1 and comp == 2:
  print('You Win')
  printChoices(choice,comp)
 if choice == 1 and comp == 3:
  print('You lose')
  printChoices(choice,comp) 
 if choice == 2 and comp == 1:
  print('You Win')
  printChoices(choice,comp) 
 if choice == 2 and comp == 3:
  print('You lose')
  printChoices(choice,comp) 
 if choice == 3 and comp == 1:
  print('You lose')
  printChoices(choice,comp) 
 if choice == 3 and comp == 2:
  print('You Win')
  printChoices(choice,comp) 
 time.sleep(3)
 print("\n")
 if __name__ == "__main__":
    main() 
 

#UserChoice
def Choose():
 print('(1 = Rock)')
 print('(2 = Paper)')
 print('(3 = Scissors)')
 UserChoice = int(input())   
 if UserChoice == int(1) or UserChoice == int(2) or UserChoice == int(3):
   bPass = True
   Start(UserChoice)
 else:
  print('Invalid Choice')
  bPass = False
  if __name__ == "__main__":
    main() 

#EntryPoint
def main():
 clear()
 print('Welcome to ADG Rock Paper Scissors')
 time.sleep(3)
 print("\n")
 print('Make a choice?')
 Choose()

if __name__ == "__main__":
    main() 