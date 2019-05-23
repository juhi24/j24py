# coding: utf-8
from __future__ import absolute_import, division, print_function, unicode_literals
__metaclass__ = type

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.ticker as mticker
from j24.tools import shift_edge, last_delta


DEFAULT_DISCRETE_CMAP = 'tab20'


def class_color(cid, cm=None, cmap=DEFAULT_DISCRETE_CMAP, mapping=None,
                default=(1, 1, 1)):
    """Pick a color for cid using optional mapping."""
    if cid < 0:
        return default
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
        clss = classes.shift(freq=dt).fillna(-1).astype(int)
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


def contour(t, ax=None, **kws):
    """Plot DataFrame contours."""
    ax = ax or plt.gca()
    x = t.columns.values
    y = t.index.values
    ax.contour(x, y, t, **kws)
    return ax


def scatter_kde(x, y, ax=None, s=50, **kws):
    """Scatter plot colored by kernel density
    Source: https://stackoverflow.com/questions/20105364
    """
    from scipy.stats import gaussian_kde
    ax = ax or plt.gca()
    xy = np.vstack([x, y])
    # The first call creates a new gaussian_kde object
    # second call evaluates the estimated pdf on the set of points
    # (shortcut for calling the evaluate method)
    z = gaussian_kde(xy)(xy)
    # Sort by density, such that the densest points are plotted last
    idx = z.argsort()
    x, y, z = x[idx], y[idx], z[idx]
    return ax.scatter(x, y, c=z, s=s, edgecolor='')


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


def axis_equal_3d(ax, dims='xyz'):
    extents = np.array([getattr(ax, 'get_{}lim'.format(dim))() for dim in dims])
    sz = extents[:,1] - extents[:,0]
    centers = np.mean(extents, axis=1)
    maxsize = max(abs(sz))
    r = maxsize/2
    for ctr, dim in zip(centers, dims):
        getattr(ax, 'set_{}lim'.format(dim))(ctr - r, ctr + r)

