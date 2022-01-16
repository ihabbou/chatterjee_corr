import pytest


@pytest.fixture
def anscombes_quartet():
    """ https://en.wikipedia.org/wiki/Anscombe%27s_quartet """
    quartet = [([10.0, 8.0, 13.0, 9.0, 11.0, 14.0, 6.0, 4.0, 12.0, 7.0, 5.0],
                [8.04, 6.95, 7.58, 8.81, 8.33, 9.96, 7.24, 4.26, 10.84, 4.82, 5.68]),
               ([10.0, 8.0, 13.0, 9.0, 11.0, 14.0, 6.0, 4.0, 12.0, 7.0, 5.0],
                [9.14, 8.14, 8.74, 8.77, 9.26, 8.1, 6.13, 3.1, 9.13, 7.26, 4.74]),
               ([0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 2.0, 3.0],
                [0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0]),
               ([8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 19.0, 8.0, 8.0, 8.0],
                [6.58, 5.76, 7.71, 8.84, 8.47, 7.04, 5.25, 12.5, 5.56, 7.91, 6.89])]

    return quartet


@pytest.fixture
def anscombes_rr():
    """Anscombe's quartet's Xi coefficient calculated using CRAN R code

    https://github.com/cran/XICOR/blob/master/R/calculateXI.R"""

    return [
        0.275,
        0.6,
        0.6666666666666667,
        0.175
    ]


@pytest.fixture
def anscombes_quartet_r(anscombes_quartet, anscombes_rr):
    """Anscombe's quartet and its coefficient"""
    return zip(anscombes_quartet, anscombes_rr)
