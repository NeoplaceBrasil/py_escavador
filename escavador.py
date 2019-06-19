import requests
import models


class Escavador:
    @property
    def user(self):
        if not self._user:
            self._user = models.User(self._authenticated_token)
        return self._user

    @property
    def person(self):
        return models.Person(self.user.token)

    @property
    def institution(self):
        return models.Institution(self.user.token)

    @property
    def lawsuit(self):
        return models.Lawsuit(self.user.token)

    @property
    def search(self):
        pass

    @property
    def is_authenticate(self):
        return bool(self.user.token)

    def authenticate(self, username, password):
        if not username or not password:
            raise Exception("username and password are required.")

        self.user.get_token(username, password)
        return self

    def __init__(self, token=None):
        self._authenticated_token = token
        self._user = None


escavador = None
escavador = Escavador() if not escavador else escavador
