import sys
sys.path.append("..")
from escavador import escavador
import getpass


def main(argv):
    username = input('Username: ')
    password = getpass.getpass('Password: ')
    id = input('Institution Id: ')

    if id is None:
        print("Institution Id is required!")
        return 1

    person = escavador.authenticate(username, password).institution.find(id)
    print(person)

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
