# coding: utf-8
from __future__ import absolute_import, division, print_function, unicode_literals
__metaclass__ = type

import sys


def running_py3():
    return sys.version_info.major > 2


def limitslist(limits):
    return [(mini, limits[i+1]) for i, mini in enumerate(limits[:-1])]


def ordinal(n):
    '''number to ordinal string'''
    if 10 <= n % 100 < 20:
        return str(n) + 'th'
    else:
        return str(n) + {1 : 'st', 2 : 'nd', 3 : 'rd'}.get(n % 10, "th")


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

