### --- --- --- Py's "Guess the number" --- --- --- ###

import random

def game():
  print('Hi! My name is Py! Let\'s play "Guess the number"!\n')
  b = True
  while b:
    n = random.randint(0, 100)
    print('Py: I think of a number between 0 and 100. What is it?')
    bGuessed = False
    while not bGuessed:
      ans = input('Me: ')
      bAns = False
      ansNum = None
      try:
        ansNum = int(ans)
        bAns = True
      except:
        bAns = False
      if not bAns:
        print('Py: Err, "{_a}" doesn\'t look like a number.'.format(_a = ans))
        continue
      ans = ansNum
      if ans == n:
        print('Py: Yes, it\'s {_n}! You guessed it!'.format(_n = n))
        bGuessed = True
      elif ans > n:
        print('Py: Too high!')
      elif ans < n:
        print('Py: Too low!')
    print('Py: Nice game! Would you like to play again? (N/Y)')
    ans = input('Me: ')
    if ans[0] not in ('Y', 'y', 't', '1'):
      b = False
  print('Py: Bye!')


def MAIN():
  game()

MAIN()












# EOF #
