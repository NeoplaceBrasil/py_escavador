import sys
sys.path.append("..")
import getpass
from escavador import escavador


def main(argv):
    username = input('Username: ')
    password = getpass.getpass('Password: ')

    token = escavador.user.get_token(username, password)
    print(token)

    save = input('Type [y/Y] to save: ')
    if save.lower() == 'y':
        escavador.user.save()

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
