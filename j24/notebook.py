# coding: utf-8
from __future__ import absolute_import, division, print_function, unicode_literals
__metaclass__ = type

import matplotlib.pyplot as plt
from IPython.display import display


class Caption():
    """captions for figures and tables in notebooks"""

    def __init__(self,s):
        self.s = s

    def _repr_html_(self):
        return '<center>{0}</center>'.format(self.s)

    def _repr_latex_(self):
        return '\\begin{center}\n'+self.s+'\n\\end{center}'


def show(fig, name=None, caption=''):
    plt.close(fig)
    if len(caption) > 0:
        if name is None:
            name = fig.number
        caption = 'Figure {n}: {text}'.format(n=name, text=caption)
    display(fig, Caption(caption))