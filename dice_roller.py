import random

def main():
  print('You rolled a die')
  
  min = 1
  max = 6
  
  dice1 = random.randint(min,max)
  dice2 = random.randint(min,max)
  
  roll = True
  
  while roll: 
    print('Rolling the dices...')
    print('Its a winner....')
    print(dice1)
    print(dice2)
  
    roll = ('y' or 'yes') in input().lower()

if __name__== "__main__":
  main()
