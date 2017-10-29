# coding: utf-8
from __future__ import absolute_import, division, print_function, unicode_literals
__metaclass__ = type

import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.ticker as mticker
from j24.tools import shift_edge


def heatmap(t, ax=None, **kws):
    """Plot DataFrame as a heatmap."""
    if ax is None:
        fig, ax = plt.subplots()
    x = shift_edge(t.columns.values)
    y = shift_edge(t.index.values)
    #y = t.index.values
    mesh = ax.pcolormesh(x, y, t, **kws)
    fig = ax.get_figure()
    fig.colorbar(mesh)
    return fig, ax


def fmt_axis_date(axis, locator=None, datefmt='%b'):
    """Format date axis (e.g. ax.xaxis) ticks."""
    date_formatter = mdates.DateFormatter(datefmt)
    locator = locator or mdates.MonthLocator()
    axis.set_major_locator(locator)
    axis.set_major_formatter(date_formatter)


def fmt_axis_str(axis, locations=None, fmt='{x}'):
    """Format ticks"""
    if locations is not None:
        locator = mticker.FixedLocator(locations)
        axis.set_major_locator(locator)
    formatter = mticker.StrMethodFormatter(fmt)
    axis.set_major_formatter(formatter)
