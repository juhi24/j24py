# coding: utf-8
import os


def ensure_join(*args):
    """like os.path.join, but creating the path if missing"""
    return ensure_dir(os.path.join(*args))


def ensure_dir(directory):
    """Make sure the directory exists. If not, create it."""
    if not os.path.exists(directory):
        os.makedirs(directory)
    return directory


def ordinal(n):
    '''number to ordinal string'''
    if 10 <= n % 100 < 20:
        return str(n) + 'th'
    else:
        return str(n) + {1 : 'st', 2 : 'nd', 3 : 'rd'}.get(n % 10, "th")


def home():
    '''home directory'''
    return os.path.expanduser('~')
