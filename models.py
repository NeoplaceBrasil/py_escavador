# -*- coding: utf-8 -*-
from enum import Enum, unique
import helpers
import settings
import requests
import inspect


class Request():
    def __init__(self, model, token=None):
        self._data = self.getEndPoint(model, inspect.stack()[1][3])
        self._url = settings.API_URL + self._data.get('base_url')
        self._method = self._data.get('method')
        self._authenticated = self._data.get('authenticated')
        self._headers = settings.DEFAULT_REQUEST_HEADER
        self._params = self._data.get('payload') or dict()
        self._payload = dict()
        self._token = token

    def isAuthenticated(self):
        return self._authenticated

    def send(self, params=None):
        if params is not None and len(params):
            for arg in self._params:
                if params.get(arg.get('name')) is not None:
                    self._payload.update({arg.get('name'): params.get(arg.get('name'))})

        message = self._isValid()
        if message:
            return message

        return self._doRequest()

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

        for arg in self._params:
            arg_name = arg.get('name')
            arg_type = arg.get('type')
            arg_required = arg.get('required')
            param = self._payload.get(arg_name)

            if arg_required and param is None:
                return "Parameter {0} is required".format(arg_name)

            if not arg_required and param is not None:
                if param.__class__.__name__ != arg_type:
                    return "Parameter {0} should be {1}".format(arg_name, arg_type)

    def _doRequest(self):
        if self._token:
            self._headers['Authorization'] = 'Bearer {0}'.format(self._token)

        response = requests.request(self._method, url=self._url, headers=self._headers, data=self._payload)
        return response.json()


class User():

    def token(self, username=None, password=None):
        username = None if username is '' else username
        password = None if username is '' else password

        if username is not None and password is not None:
            data = Request(self).send(dict({"username": username, "password": password}))
            helpers.write_json(settings.API_ACCESS_TOKEN, data)

        data = helpers.laod_json(settings.API_ACCESS_TOKEN)
        return data.get('access_token')

    def credits(self, token=None):
        if token is None:
            token = self.token()

        response = Request(self, token).send()
        if 'quantidade_creditos' in response:
            return response['quantidade_creditos']

        return response
