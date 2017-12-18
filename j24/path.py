# coding: utf-8
from __future__ import absolute_import, division, print_function, unicode_literals
__metaclass__ = type

import os


def home():
    """home directory"""
    return os.path.expanduser('~')


def ensure_join(*args):
    """like os.path.join, but creating the path if missing"""
    return ensure_dir(os.path.join(*args))


def ensure_dir(directory):
    """Make sure the directory exists. If not, create it."""
    if not os.path.exists(directory):
        os.makedirs(directory)
    return directory


def filename_friendly(namestr, space_replacement='_'):
    """make string filename friendly"""
    # avoid circular import
    from j24.tools import try_decode
    namestr = try_decode(namestr)
    namestr = namestr.rstrip().replace(' ', space_replacement)
    keepchars = ('-', '.', '_')
    return ''.join(c for c in namestr if c.isalnum() or c in keepchars)
