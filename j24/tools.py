# coding: utf-8
from __future__ import absolute_import, division, print_function, unicode_literals
__metaclass__ = type
import os
import shutil
import numpy as np
import sys
from j24 import home


def eprint(*args, **kwargs):
    """print to stderr"""
    print(*args, file=sys.stderr, **kwargs)


def running_py3():
    """Check if python major version is greater than 2."""
    return sys.version_info.major > 2


def limitslist(limits):
    """
    Translate a one dimensional vector to a list of pairs of consecutive
    elements.
    """
    return [(mini, limits[i+1]) for i, mini in enumerate(limits[:-1])]


def ordinal(n):
    '''number to ordinal string'''
    if 10 <= n % 100 < 20:
        return str(n) + 'th'
    else:
        return str(n) + {1 : 'st', 2 : 'nd', 3 : 'rd'}.get(n % 10, "th")


def install_systemd_service(name, template_path):
    filename = name + '.service'
    install_path = os.path.join('/etc/systemd/system', filename)
    with open(template_path, 'r') as f:
        service = f.read()
    service = service.format(working_dir=home(), exec_start=shutil.which(name))
    with open(install_path, 'w') as f:
        f.write(service)


def last_delta(x):
    """difference between 2 last elements"""
    return x[-1]-x[-2]


def extrap_last_delta(x):
    """Append element x[i+1] = x[i]-x[i-1] to the end of x."""
    return np.append(x, x[-1]+last_delta(x))


def shift_edge(x):
    """
    In case of linear x, the output is bin edges instead of central values.
    Output length is len(x)+1.
    """
    return extrap_last_delta(x) - last_delta(x)/2

