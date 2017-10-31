# coding: utf-8
from __future__ import absolute_import, division, print_function, unicode_literals
__metaclass__ = type

import numpy as np
import pandas as pd


def pol2cart(r,theta):
    """Return coordinates as complex numbers."""
    return r*np.exp(1j*theta)


def pol2cart_df(*args, cols=None):
    """direction in radians"""
    cxy = pol2cart(*args)
    lcxy = cxy.apply(lambda x: (x.real, x.imag))
    df = pd.DataFrame.from_items(zip(lcxy.index, lcxy.values)).T
    df.columns = cols or ('x', 'y')
    return df

