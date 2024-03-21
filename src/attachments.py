import io
import os

from contextlib import closing

import requests


def down_atta(id_attachment, value_token):
    by = []
    headers_down_att = {
        'Content-Type': 'application/json',
        'Cookie': "LWSSO_COOKIE_KEY={token}".format(token=value_token)
    }
    url_da = "https://sma-csc.itstk.com/rest/716383812/ces/attachment/{id}".format(id=id_attachment)

    r = requests.get(url_da, headers=headers_down_att, verify=False)

    return r.content


def save_attachments(folder_path, attachment_name, attachment_data):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    open(folder_path + "/" + attachment_name, 'wb').write(attachment_data)
