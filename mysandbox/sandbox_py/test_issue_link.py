# test_issue_link.py

def askname():
  name = input('What's your name?\n> ')
  if name == '':
    print('Enter non-null string for name! Try again.')
  return name

def main():
  name = ''
  while name != '':
    name = askname()
  print(f'Hello, ${name}!')

if __name__ = '__main__':
  main()
