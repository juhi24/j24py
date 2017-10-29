# coding: utf-8
from __future__ import absolute_import, division, print_function, unicode_literals
__metaclass__ = type

import matplotlib.pyplot as plt
import matplotlib.dates as mdates
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


def fmt_axis_date(axis, xlocator=None, datefmt='%b'):
    """Format date axis (e.g. ax.xaxis) ticks."""
    date_formatter = mdates.DateFormatter(datefmt)
    xloc = xlocator or mdates.MonthLocator()
    axis.set_major_locator(xloc)
    axis.set_major_formatter(date_formatter)
