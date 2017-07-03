# coding: utf-8

def limitslist(limits):
    return [(mini, limits[i+1]) for i, mini in enumerate(limits[:-1])]


def ordinal(n):
    '''number to ordinal string'''
    if 10 <= n % 100 < 20:
        return str(n) + 'th'
    else:
        return str(n) + {1 : 'st', 2 : 'nd', 3 : 'rd'}.get(n % 10, "th")
