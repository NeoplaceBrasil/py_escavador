import sys
sys.path.append("..")
from escavador import models
import getpass


def main(argv):
    username = input('Username: ')
    password = getpass.getpass('Password: ')

    token = models.User().token(username, password)
    print(token)

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
