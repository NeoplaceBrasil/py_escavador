import os


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

API_URL = "https://api.escavador.com/api/v1/"

API_ACCESS_TOKEN = ROOT_DIR + "/token.json"

API_DOC = "https://api.escavador.com/docs"

API_VERSION = "v1"

END_POINTS_PATH = ROOT_DIR + "/endpoints.json"

DEFAULT_REQUEST_HEADER = {
    'X-Requested-With': 'XMLHttpRequest'
}
