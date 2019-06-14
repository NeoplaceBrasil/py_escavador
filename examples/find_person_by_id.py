import sys
sys.path.append("..")
from escavador import models
import getpass


def main(argv):
    username = input('Username: ')
    password = getpass.getpass('Password: ')
    id = input('Person Id: ')

    if id is None:
        print("Person Id is required!")
        return 1

    person = models.Person().authenticate(username=username, password=password).find(id=id)
    print(person)

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
