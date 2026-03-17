# test_issue_link.py

def askget_name() -> str:
  name = input('What's your name?\n> ')
  if name == '':
    print('Name cannot be null string.')
  return name

def main():
  name = ''
  while name != '':
    name = askget_name()    
  print(f'Hello, ${name}!')

if __name__ = '__main__':
  main()
