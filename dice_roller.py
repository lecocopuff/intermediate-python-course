import random

def main():
  print('You rolled a die')
  
  min = 1
  max = 6
  
  roll_again = "yes"
  
  while roll_again == "yes" or roll_again == "y":
    print("Rolling the dices...")
    print("It's a winner....")
    print random.randint(min,max)
    print random.randint(min,max)
  
  roll again = raw_input("Roll the dices again?")

if __name__== "__main__":
  main()
