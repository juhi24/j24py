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
    return pd.DataFrame(km.cluster_centers_.T, index=t.index)


def pca_stats(pca):
    with plt.style.context('fivethirtyeight'):
        plt.figure();
        plt.title('Explained variance ratio over component');
        plt.plot(pca.explained_variance_ratio_);
        plt.figure();
        plt.title('Cumulative explained variance over component');
        plt.plot(pca.explained_variance_ratio_.cumsum());
    print('PCA captures {:.2f}% of the variance in the dataset.'.format(pca.explained_variance_ratio_.sum() * 100))
