# guessing game
'''
secret_num = 10
guess_start = 0
guess_limit = 3
while guess_start < guess_limit:
     guess = int(input('guess: '))
     guess_start += 1
     if guess == int(secret_num):
        print('you won')
        break
     else:
         print('you lost')
'''
# car game
'''
command =""
started = True
while True:
    command = input('enter command >: ').lower()
    if command == 'start':
          print('car started')
    elif command == 'stop':
       print('car stopped')
    elif command == 'help':
       print("""
start - to start 
stop - to stop
quit - to quit
       """)
    elif command == 'quit':
        break
    else:
       print('No such command')
'''
