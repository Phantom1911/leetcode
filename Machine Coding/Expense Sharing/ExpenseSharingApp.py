from typing import List
from User import User

class ExpenseSharingApp:
    def __init__(self, users):
        self.users = users

if __name__=="__main__":
    print("Welcome to expense sharing app")
    users = [User("u"+str(i)) for i in range(4)]
    app = ExpenseSharingApp(users)
    while True:
        operation = int(input("press 1 for SHOW , 2 for ADD , 3 to exit the app\n"))
        if operation == 3:
            break
        if operation == 1:

