# -*- coding: utf-8 -*-

import json


def json_data(data):
    if not isinstance(data, dict):
        data = json.dumps(data, ensure_ascii=False)
    return data
