import random
import string
import sys


class Automator:
    def makeUsername(self):
        userList = open('list.txt', 'r').readlines()
        i =+ 1
        return (random.choice(userList))

    def makePass(self):
        keygen = (string.ascii_letters + string.digits)
        randomPass = [("".join(random.choice(keygen) for i in range(8)))]
        return ("".join(randomPass))
    
    def output(self):
        username = self.makeUsername()
        password = self.makePass()

        while True:
            print(f"\nUsername: {username}Password: {password}")
            break
        
auto = Automator()
auto.output()