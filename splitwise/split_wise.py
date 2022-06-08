from splitwise.User import User
import pandas as pd
import random

from splitwise.service import service

HELLO_STRING  = 'hello!'

if __name__=="__main__":
    n = int(input("enter num of users .. "))
    user_list = [User(str(i)) for i in range(n)]
    for u in user_list:
        print('user name is ' + u.name)
    print(random.randint(1,6))
    print(HELLO_STRING)
    print(f'{HELLO_STRING}')
    game = service(user_list)
    game.start_game()