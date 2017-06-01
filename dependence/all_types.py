"""
Dependency criteria covering all types (Numerical, Categorical, Binary)
Author: Diviyan Kalainathan
Date: 1/06/2017

"""

import sklearn.metrics as metrics
import numpy as np

def ajd_mi_fd(a, b):
    """ Dependency criterion made of binning and mutual information

    The dependency metric relies on using the clustering metric adjusted mutual information applied
    to binned variables using the Freedman Diaconis Estimator.
    Ref: Vinh, Nguyen Xuan and Epps, Julien and Bailey, James, "Information theoretic measures for clusterings
        comparison: Variants, properties, normalization and correction for chance", Journal of Machine Learning
        Research, Volume 11, Oct 2010.
    Ref: Freedman, David and Diaconis, Persi, "On the histogram as a density estimator:L2 theory",
        "Zeitschrift für Wahrscheinlichkeitstheorie und Verwandte Gebiete", 1981, issn=1432-2064,
        doi=10.1007/BF01025868.

    :param a: input data
    :param b: input data
    :type a: array-like, numerical data
    :type b: array-like, numerical data
    :return: dependency statistic (1=Highly dependent, 0=Not dependent)
    :rtype: float
    """

    def bin_variable(var1):  # bin with normalization
        var1 = np.array(var1).astype(np.float)

        var1 = (var1 - np.mean(var1)) / np.std(var1)

        val1 = np.digitize(var1, np.histogram(var1, bins='fd')[1])

        return val1

    return metrics.adjusted_mutual_info_score(bin_variable(a),
                                              bin_variable(b))