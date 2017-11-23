# coding: utf-8
from __future__ import absolute_import, division, print_function, unicode_literals
__metaclass__ = type

import pandas as pd
import matplotlib.pyplot as plt


def fit_predict(t, km):
    km.fit(t.T)
    classes = pd.Series(data=km.predict(t.T), index=t.columns)
    return classes


def centroids(t, km):
    """cluster centroids as DataFrame"""
    return pd.DataFrame(km.cluster_centers_.T, index=t.index)


def class_fraction(classes):
    """occurrence fraction of each cluster"""
    counts = classes.groupby(classes).count()
    return counts/classes.count()


def normalized_class_sizes(classes):
    """cluster sizes normalized around 1"""
    return class_fraction(classes)*classes.unique().size


def pca_stats(pca):
    with plt.style.context('fivethirtyeight'):
        plt.figure();
        plt.title('Explained variance ratio over component');
        plt.plot(pca.explained_variance_ratio_);
        plt.figure();
        plt.title('Cumulative explained variance over component');
        plt.plot(pca.explained_variance_ratio_.cumsum());
    print('PCA captures {:.2f}% of the variance in the dataset.'.format(pca.explained_variance_ratio_.sum() * 100))
