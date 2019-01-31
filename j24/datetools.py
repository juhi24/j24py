# coding: utf-8
from __future__ import absolute_import, division, print_function, unicode_literals
__metaclass__ = type

from datetime import datetime, timedelta
from copy import deepcopy
from string import Template


class DeltaTemplate(Template):
    delimiter = "%"


def strfdelta(tdelta, fmt):
    d = {"D": tdelta.days}
    hours, rem = divmod(tdelta.seconds, 3600)
    minutes, seconds = divmod(rem, 60)
    d["H"] = '{:02d}'.format(hours)
    d["M"] = '{:02d}'.format(minutes)
    d["S"] = '{:02d}'.format(seconds)
    t = DeltaTemplate(fmt)
    return t.substitute(**d)


def daterange2str(start, end=None, dtformat='{day}{month}{year}', delimiter='-',
          hour_fmt='%H', day_fmt='%d.', month_fmt='%m.', year_fmt='%Y'):
    """date range in simple human readable format"""
    formats = {'hour':hour_fmt, 'day':day_fmt, 'month':month_fmt,
               'year':year_fmt}
    if end is None:
        return start.strftime(dtformat.format(**formats))
    yr_first = dtformat[:6]=='{year}'
    same_date = start.date() == end.date()
    start_fmt = dtformat
    end_fmt = dtformat
    stripped_fmt = dtformat
    for attr in ('minute', 'hour', 'day', 'month', 'year'):
        if getattr(start, attr) == getattr(end, attr) and not same_date:
            stripped_fmt = stripped_fmt.replace(('{%s}' % attr),'')
    stripped_fmt = stripped_fmt.strip()
    if yr_first:
        end_fmt = stripped_fmt
    else:
        start_fmt = stripped_fmt
    start_str = start.strftime(start_fmt.format(**formats))
    end_str = end.strftime(end_fmt.format(**formats))
    if same_date:
        return start_str
    return start_str + delimiter + end_str


def mldatenum2datetime(datenum, round_ms=True):
    """matlab datenum to datetime, round microseconds by default"""
    dt0 = timedelta(days=366)
    time = datetime.fromordinal(int(datenum)) + timedelta(days=datenum%1) - dt0
    if round_ms:
        return round_microseconds(time)
    return time


def round_microseconds(t):
    t_out = deepcopy(t)
    extrasec = timedelta(seconds=round(t.microsecond/1000000))
    return t_out + extrasec - timedelta(microseconds=t.microsecond)
