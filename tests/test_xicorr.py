import pytest

import numpy as np
from chatterjee import xicorr


def test_different_lengths():
    """Both arrays must be same length"""
    with pytest.raises(ValueError):
        xicorr.xicorr(np.ones(5), np.ones(6))


def test_min_length():
    """Min length = 2"""
    with pytest.raises(ValueError):
        xicorr.xicorr(np.ones(1), np.ones(1))


def test_anscombes_coef(anscombes_quartet_r):
    """Anscombe's quartet coefficient"""
    for quartet in anscombes_quartet_r:
        (x, y), xi = quartet
        calc_xi, _ = xicorr.xicorr(x, y)
        assert calc_xi == pytest.approx(xi, rel=10e-6)


def test_anscombes_pval(anscombes_quartet_p):
    """Anscombe's quartet coefficient"""
    for quartet in anscombes_quartet_p:
        (x, y), p = quartet
        _, calc_p = xicorr.xicorr(x, y)
        assert calc_p == pytest.approx(p, rel=10e-6)


@pytest.mark.skip(reason="Same test but for debugging")
def test_anscombes_coef2(anscombes_quartet, anscombes_rr, anscombes_pval):
    quartet = list(zip(anscombes_quartet, zip(anscombes_rr, anscombes_pval)))

    (x, y), (xi, p) = quartet[0]
    calc_xi, calc_p = xicorr.xicorr(x, y)
    assert calc_xi == pytest.approx(xi, rel=10e-6)
    assert calc_p == pytest.approx(p, rel=10e-6)

    (x, y), (xi, p) = quartet[1]
    calc_xi, calc_p = xicorr.xicorr(x, y)
    assert calc_xi == pytest.approx(xi, rel=10e-6)
    assert calc_p == pytest.approx(p, rel=10e-6)

    (x, y), (xi, p) = quartet[2]
    calc_xi, calc_p = xicorr.xicorr(x, y)
    assert calc_xi == pytest.approx(xi, rel=10e-6)
    assert calc_p == pytest.approx(p, rel=10e-6)

    (x, y), (xi, p) = quartet[3]
    calc_xi, calc_p = xicorr.xicorr(x, y)
    assert calc_xi == pytest.approx(xi, rel=10e-6)
    assert calc_p == pytest.approx(p, rel=10e-6)
