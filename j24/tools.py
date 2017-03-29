# coding: utf-8


def limitslist(limits):
    return [(mini, limits[i+1]) for i, mini in enumerate(limits[:-1])]


def ordinal(n):
    '''number to ordinal string'''
    if 10 <= n % 100 < 20:
        return str(n) + 'th'
    else:
        return str(n) + {1 : 'st', 2 : 'nd', 3 : 'rd'}.get(n % 10, "th")


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



