
import numpy as np
import scipy.stats as ss


def xicorr(x, y):
    """Xi Correlation Coefficient adapted from the original CRAN R code

    https://github.com/cran/XICOR/blob/master/R/calculateXI.R


    Computes robust association measures that do not presuppose linearity.
    The xi correlation (xicor) is based on cross correlation between ranked increments.
    The reference for the methods implemented here is [1]_.

    Parameters
    ----------
    x : (N,) array_like
        Input array.
    y : (N,) array_like
        Input array.

    Returns
    -------
    xi : float
        Xi correlation coefficient.

    References
    ----------
    .. [1] Chatterjee, Sourav. "A New Coefficient of Correlation."
           Journal of the American Statistical Association 116 (2020)

    Examples
    --------
    >>> from chatterjee import xicorr
    >>> a = np.array([0, 0, 0, 1, 1, 1, 1])
    >>> b = np.arange(7)
    >>> xicorr.xicorr(a, b)
    (0.625,)

    >>> xicorr.xicorr([1, 2, 3, 4, 5], [10, 9, 2.5, 6, 4])
    (0.1250000000000001,)

    """

    n = len(x)
    if n != len(y):
        raise ValueError('x and y must have the same length.')

    if n < 2:
        raise ValueError('x and y must have length at least 2.')

    x = np.asarray(x)
    y = np.asarray(y)

    # PI is the rank vector for x, with ties broken at random
    PI = ss.rankdata(x, method="average")

    # fr[i] is number of j s.t. y[j] <= y[i], divided by n.
    fr = ss.rankdata(y, method="average") / n

    # gr[i] is number of j s.t. y[j] >= y[i], divided by n.
    gr = ss.rankdata(y, method="average") / n

    # order of the x's, ties broken at random.
    ord = np.argsort(PI, kind="quicksort")

    # Rearrange fr according to ord.
    fr = fr[ord]

    # xi is calculated in the next three lines:
    A1 = np.abs(np.diff(fr)).sum() / (2 * n)
    CU = np.mean(gr * (1. - gr))
    xi = 1. - (A1 / CU)
    return (xi,)
