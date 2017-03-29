# coding: utf-8
import os


def home():
    '''home directory'''
    return os.path.expanduser('~')


def ensure_join(*args):
    """like os.path.join, but creating the path if missing"""
    return ensure_dir(os.path.join(*args))


def ensure_dir(directory):
    """Make sure the directory exists. If not, create it."""
    if not os.path.exists(directory):
        os.makedirs(directory)
    return directory
