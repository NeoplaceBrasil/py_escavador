import sys
sys.path.append("..")
from escavador import escavador
import getpass


def main(argv):
    username = input('Username: ')
    password = getpass.getpass('Password: ')

    token = escavador.authenticate(username, password).user.credits
    print(token)

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
