
class AuthenticationRequired(Exception):
    pass


class NotAuthorized(Exception):
    pass


class InvalidTokenInformation(Exception):
    pass


class TokenNotFound(Exception):
    pass


class BadRequest(Exception):
    pass
