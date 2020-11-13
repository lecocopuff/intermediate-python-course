from random import randint

def main():
  roll = True
  
  while roll: 
    print('Rolling the dices...')
    print(randint(1,6))
    print(randint(1,6))
  
    roll = ('y' or 'yes') in input().lower()

if __name__== "__main__":
  main()
