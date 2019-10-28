import logging
import json
from app.rpc import api

logging.basicConfig(level=logging.INFO)


def info():
    info = api.getinfo()
    logging.info(info)

    return json.dumps(info)

def zpp_info():
    asset_info = api.listassets('ZPP')

    logging.info(asset_info)

    return json.dumps(asset_info)


def get_address_balance(data):
    _data = json.load(data)
    balance = api.getaddressbalances(_data['address'])

    logging.info(balance)

    return json.dumps(balance)

def issue_from_original_address(data):
    _data = json.load(data)
    address = _data['address']

    return json.dumps({'hello':'world'})