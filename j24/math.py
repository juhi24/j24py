# coding: utf-8
from __future__ import absolute_import, division, print_function, unicode_literals
__metaclass__ = type

import numpy as np
import pandas as pd


def pol2cart(r, theta):
    """Return coordinates as complex numbers."""
    return r*np.exp(1j*theta)


def wind2uv(ws, wd):
    """wind speed and direction to u and v components"""
    theta = -np.deg2rad(wd)-np.pi/2
    return pol2cart(ws, theta)


def pol2cart_df(*args, cols=('x', 'y'), conv_func=pol2cart):
    """
    input depends on conv_func
    returns: DataFrame
    """
    cxy = conv_func(*args)
    lcxy = cxy.apply(lambda x: (x.real, x.imag))
    df = pd.DataFrame.from_items(zip(lcxy.index, lcxy.values)).T
    df.columns = cols
    return df


def wind2uv_df(*args):
    """Wrapper for pol2cart_df for converting Series of wind speed and
    direction to u and v components."""
    return pol2cart_df(*args, cols=('u', 'v'), conv_func=wind2uv)
