# coding: utf-8
from __future__ import absolute_import, division, print_function, unicode_literals
__metaclass__ = type

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.ticker as mticker
from j24.tools import shift_edge, last_delta


DEFAULT_DISCRETE_CMAP = 'tab20'


def class_color(cid, cm=None, cmap=DEFAULT_DISCRETE_CMAP, mapping=None,
                default=(1, 1, 1)):
    """Pick a color for cid using optional mapping."""
    cm = cm or plt.get_cmap(cmap)
    if mapping is not None:
        if cid in mapping.index:
            return cm.colors[mapping[cid]]
        return default
    return cm.colors[cid]


def class_colors(classes, ymin=-0.2, ymax=0, ax=None, alpha=1, mapping=None,
                 cmap=DEFAULT_DISCRETE_CMAP, displacement_factor=0.5, **kws):
    """Plot time series of color coding under x axis."""
    if not isinstance(classes, pd.Series):
        classes = pd.Series(data=classes, index=classes)
    if isinstance(classes.index, pd.DatetimeIndex):
        t = classes.index
        dt = last_delta(t)*displacement_factor
        clss = classes.shift(freq=dt).dropna().astype(int)
    else:
        clss = classes
        dt = displacement_factor
        clss.index = clss.index+dt
    ax = ax or plt.gca()
    cm = plt.get_cmap(cmap)
    t0 = clss.index[0]-2*dt
    for t1, cid in clss.iteritems():
        color = class_color(cid, cm, mapping=mapping)
        ax.axvspan(t0, t1, ymin=ymin, ymax=ymax, facecolor=color,
                   alpha=alpha, clip_on=False, **kws)
        t0 = t1


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
