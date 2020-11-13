import random

def main():
  print('You rolled a die')
  
  min = 1
  max = 6
  
  dice1 = random.randint(min,max)
  dice2 = random.randint(min,max)
  
  roll_again = 'yes'
  
  while roll_again == "yes" or roll_again == "y":
    print('Rolling the dices...')
    print('Its a winner....')
    print(dice1)
    print(dice2)
  
  roll again = raw_input("Roll the dices again?")

if __name__== "__main__":
  main()
