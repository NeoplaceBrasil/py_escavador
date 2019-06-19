# -*- coding: utf-8 -*-
from enum import Enum, unique
import requests
import inspect
import helpers
import settings
import exceptions


class Request():
    def __init__(self, model, method, token=None):
        self._data = self.getEndPoint(model, method)
        self._url = settings.API_URL + settings.API_VERSION + '/' + self._data.get('base_url')
        self._method = self._data.get('method')
        self._authenticated = self._data.get('authenticated')
        self._headers = settings.DEFAULT_REQUEST_HEADER
        self._body_params = self._data.get('body_params') or dict()
        self._uri_params = self._data.get('uri_params') or dict()
        self._payload = dict()
        self._token = token

    def isAuthenticated(self):
        return self._authenticated

    def send(self, bodyParams=None, uriParams=None):
        #
        if bodyParams and len(bodyParams) and len(self._body_params):
            for arg in self._body_params:
                if bodyParams.get(arg.get('name')) is not None:
                    self._payload.update({arg.get('name'): bodyParams.get(arg.get('name'))})

        message = self._isValid()
        if message:
            return message

        if uriParams and len(self._uri_params):
            for param in self._uri_params:
                self._url = self._url.replace(param.get('id'), str(uriParams.get(param.get('name'))))

        return self._do_request()

    def getEndPoint(self, model, method):
        try:
            model_class = model.__class__.__name__
            data = helpers.laod_json(settings.END_POINTS_PATH)

            return data[model_class][method]
        except KeyError as e:
            raise KeyError("[{0}] EndPoint to {1}.{2} doesn\'t exists in {3}".format(str(e), model_class, method, settings.END_POINTS_PATH))

    def _isValid(self):
        if self._authenticated and not self._token:
            return "User not authenticated"

        for arg in self._body_params:
            arg_name = arg.get('name')
            arg_type = arg.get('type')
            arg_required = arg.get('required')
            param = self._payload.get(arg_name)

            if arg_required and param is None:
                return "Parameter {0} is required".format(arg_name)

            if not arg_required and param is not None:
                if param.__class__.__name__ != arg_type:
                    return "Parameter {0} should be {1}".format(arg_name, arg_type)

    def _do_request(self):
        if self._token:
            self._headers['Authorization'] = 'Bearer {0}'.format(self._token)

        response = requests.request(self._method, url=self._url,
                                    headers=self._headers, data=self._payload)
        response = response.json()

        if 'error' in response:
            raise Exception('Error: {0}. {1}.'.format(response.get('error'),
                                                      response.get('message')))
        elif response == "{'message': ''}":
            raise exceptions.BadRequest()

        return response


class User():
    def __init__(self, token=None):
        self._token = token
        self._token_data = None

    #@authtenticated
    def save(self):
        if not self._token:
            raise exceptions.TokenNotFound()

        helpers.write_json(settings.API_ACCESS_TOKEN, self._token_data)

    @property
    def token(self):
        if not self._token:
            self._token = self.get_token()
        return self._token

    @property
    def credits(self):
        if not self._token:
            raise exceptions.TokenNotFound()

        response = Request(self, inspect.stack()[0][3], self._token).send()
        if 'quantidade_creditos' in response:
            return int(response['quantidade_creditos'])

        return response

    def get_token(self, username=None, password=None):
        if not username and not password:
            self._token_data = helpers.laod_json(settings.API_ACCESS_TOKEN)
        else:
            self._token_data = Request(self, inspect.stack()[0][3]).send(bodyParams={'username': username, 'password': password})

        if not self._token_data:
            raise exceptions.TokenNotFound()
        if self._token_data and 'access_token' not in self._token_data:
            raise exceptions.InvalidTokenInformation()

        self._token = self._token_data.get('access_token')
        return self._token


class Person():
    def __init__(self, token=None):
        self._token = token

    #@authtenticated
    def find(self, key):
        if not self._token:
            raise exceptions.TokenNotFound()

        return Request(self, inspect.stack()[0][3], self._token).send(uriParams={"id": key})

    #@authtenticated
    def lawsuits(self, key=None):
        if not self._token:
            raise exceptions.TokenNotFound()

        return Request(self, inspect.stack()[0][3], self._token).send(uriParams={"id": key})


class Institution():
    def __init__(self, token=None):
        self._token = token

    #@authtenticated
    def find(self, id):
        if not self._token:
            raise exceptions.TokenNotFound()

        return Request(self, inspect.stack()[0][3], self._token).send(uriParams={"id": id})

    #@authtenticated
    def lawsuits(self, key=None):
        if not self._token:
            raise exceptions.TokenNotFound()

        return Request(self, inspect.stack()[0][3], self._token).send(uriParams={"id": key})


class Lawsuit():
    def __init__(self, token=None):
        self._token = token

    #@authtenticated
    def find(self, key):
        if not self._token:
            raise exceptions.TokenNotFound()

        return Request(self, inspect.stack()[0][3], self._token).send(uriParams={"id": key})

    #@authtenticated
    def events(self, key=None):
        if not self._token:
            raise exceptions.TokenNotFound()

        return Request(self, inspect.stack()[0][3], self._token).send(uriParams={"id": key})


@unique
class TipoEntidade(Enum):
    TODAS = 't'
    PESSOAS = 'p'
    INSTITUICOES = 'i'
    PATENTE = 'pa'
    DIARIOS_OFICIAIS = 'd'
    PARTES_ENVOLVIDAS = 'en'
    ARTIGOS = 'a'


class Termo():
    pass


# def buscarPessoa(self, termo, pagina):
#     self.buscar(termo=termo, tipo_entidade=TipoEntidade.PESSOAS)

# def buscarInstitucao(self, termo, pagina):
#     self.buscar(termo=termo, tipo_entidade=TipoEntidade.INSTITUICOES)

# def buscarInstitucao(self, termo, pagina):
#     self.buscar(termo=termo, tipo_entidade=TipoEntidade.PATENTE)

# def buscarDiarios(self, termo, pagina):
#     self.buscar(termo=termo, tipo_entidade=TipoEntidade.DIARIOS_OFICIAIS)

# def buscarPartesEnvolvidas(self, termo, pagina):
#     self.buscar(termo=termo, tipo_entidade=TipoEntidade.PARTES_ENVOLVIDAS)

# def buscarArtigos(self, termo, pagina):
#     self.buscar(termo=termo, tipo_entidade=TipoEntidade.ARTIGOS)


# def buscar(self, termo,  tipo_entidade=TipoEntidade.TODAS):
#     pass




class Instituicao():
    def __init__(self):
        pass


class Processo():
    #id
    #numero_antigo
    #numero_novo
    #tipo_envolvido
    #link_api

    def __init__(self):
        pass