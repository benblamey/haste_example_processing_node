from haste_storage_client.core import HasteStorageClient

import json
import os.path
import urllib.request

haste_storage_clients = {}


def __get_magic_haste_client_config_from_server(host):
    t = 'w0rj540vhw8dx0ng0t6nw8cghp'
    stream = urllib.request.urlopen('http://' + host + '/' + t + '/haste_storage_client_config.json')
    config = stream.read()
    config = json.load(config)
    return config


def __get_haste_storage_client_config(host):
    # If a local config file exists, use it:
    json_config = os.path.expanduser('~/.haste/haste_storage_client_config.json')
    if os.path.isfile(json_config):
        return None  # Client will attempt to read config from this file.
    else:
        # Otherwise, use the auto-configuration server:
        try:
            config = __get_magic_haste_client_config_from_server(host)
            return config
        except Exception as e:
            print('failed to reading config from auto-configuration host')
            raise e


def get_storage_client(stream_id, auto_configuration_host='130.239.81.96'):
    if stream_id not in haste_storage_clients:
        haste_storage_client_config = __get_haste_storage_client_config(auto_configuration_host)

        client = HasteStorageClient(stream_id,
                                    config=haste_storage_client_config)

        haste_storage_clients[stream_id] = client


    # TODO: only cache N clients.

    return haste_storage_clients[stream_id]
