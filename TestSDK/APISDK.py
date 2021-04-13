# encoding: utf-8

import requests
import json
from TestSDK.Payload import Payload


def __send_request(method, _url, _params):

    json_string = json.dumps(_params, indent=4, sort_keys=True)
    print ("INPUT PAYLOAD: " + json_string)

    _headers = {'Content-type': 'application/json'}

    if method == "post":
        response = requests.post(url=_url, params=_params, headers=_headers)
    elif method == "get":
        response = requests.get(url=_url, params=_params, headers=_headers)
    elif method == "put":
        response = requests.put(url=_url, params=_params, headers=_headers)
    elif method == "patch":
        response = requests.patch(url=_url, params=_params, headers=_headers)
    else:
        raise ValueError('Please, specify a valid REST method: POST, GET, PUT or PATCH')

    json_data = json.loads(response.text)
    print("RESPONSE BODY: " + json.dumps(json_data, indent=4, sort_keys=True))

    _object = Payload(json.dumps(json_data))
    status = _object.__getattribute__('status')
    print("RESPONSE STATUS: " + status)

    return response


def post(_url, _params):
    print("Running POST")
    return __send_request("post", _url, _params)


def get(_url, _params):
    print("Running GET")
    return __send_request("get", _url, _params)


def put(_url, _params):
    print("Running PUT")
    return __send_request("put", _url, _params)


def patch(_url, _params):
    print("Running PACTH")
    return __send_request("patch", _url, _params)
