import sys
sys.path.append("..")
from escavador import escavador
import getpass


def main(argv):
    username = input('Username: ')
    password = getpass.getpass('Password: ')
    ids = input('Type monitoring ids (separated by commas. e.g. 1,2,3): ')

    if ids and not ids.replace(',', '').isdigit():
        print("Enter only integers separated by commas!")
        return 1

    all_monitoring = escavador.authenticate(username, password).court.all_monitoring(ids)
    print(all_monitoring)

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
