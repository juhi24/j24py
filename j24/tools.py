# coding: utf-8
import os
import shutil


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
    '''user home directory'''
    return os.path.expanduser('~')


def install_systemd_service(name, template_path):
    filename = name + '.service'
    install_path = os.path.join('/etc/systemd/system', filename)
    with open(template_path, 'r') as f:
        service = f.read()
    service = service.format(working_dir=home(), exec_start=shutil.which(name))
    with open(install_path, 'w') as f:
        f.write(service)