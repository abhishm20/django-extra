# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import mimetypes
import random
import string
import uuid
from collections import OrderedDict
from itertools import tee

from unidecode import unidecode


def generate_password():
    # characters to generate password from
    characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")
    random.shuffle(characters)
    # picking random characters from the list
    password = []
    password.append(random.choice(characters))
    # shuffling the resultant password
    random.shuffle(password)
    return "".join(password)


def remove_non_ascii(text):
    return unidecode(str(text, encoding="utf-8"))


def pairwise(iterable):
    """s -> (s0,s1), (s1,s2), (s2, s3), ..."""
    _a, _b = tee(iterable)
    next(_b, None)
    return zip(_a, _b)


def split_full_name(full_name):
    splitted_name = full_name.split()
    if len(splitted_name) == 3:
        return splitted_name
    if len(splitted_name) == 2:
        return splitted_name[0], "", splitted_name[1]
    if len(splitted_name) == 1:
        return splitted_name[0], "", ""
    return splitted_name[0], splitted_name[1], " ".join(splitted_name[2:])


def get_mime_type(file_path):
    return mimetypes.MimeTypes().guess_type(file_path)[0]


def format_constants(value):
    """
    Converts abc_xyz > Abc Xyz
    :param value:
    :return:
    """
    return " ".join(value.split("_")).title()


def get_client_ip(request):
    x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
    if x_forwarded_for:
        _ip = x_forwarded_for.split(",")[0]
    else:
        _ip = request.META.get("REMOTE_ADDR")
    return _ip


def is_exists(obj, value):
    return hasattr(obj, value) and getattr(obj, value)


def make_name_value_pair(set_list):
    return [{"name": x[1], "value": x[0]} for x in set_list]


def flatten_object(obj):
    new_obj = {}
    for key in obj.keys():
        if type(obj[key]) in [dict, OrderedDict]:
            _a = flatten_object(obj[key])
            new_obj.update({key + "_" + k: _a[k] for k in _a.items()})
        else:
            new_obj[key] = obj[key]
    return new_obj


def mask_string(s_value, unmasked_length=4):
    if s_value:
        return f"{'*' * (len(s_value) - unmasked_length)}{s_value[:unmasked_length]}"
    return ""


def upload_to_s3(instance, filename):
    return f"{instance.__class__.__name__.lower()}/{instance.id}/{str(uuid.uuid4())}_{filename}"
