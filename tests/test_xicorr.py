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
        assert xicorr.xicorr(x, y) == pytest.approx((xi,), rel=10e-6)


@pytest.mark.skip(reason="Same test but for debugging")
def test_anscombes_coef2(anscombes_quartet_r):
    quartet = list(anscombes_quartet_r)

    (x, y), xi = quartet[0]
    assert xicorr.xicorr(x, y) == pytest.approx((xi,), rel=10e-6)

    (x, y), xi = quartet[1]
    assert xicorr.xicorr(x, y) == pytest.approx((xi,), rel=10e-6)

    (x, y), xi = quartet[2]
    assert xicorr.xicorr(x, y) == pytest.approx((xi,), rel=10e-6)

    (x, y), xi = quartet[3]
    assert xicorr.xicorr(x, y) == pytest.approx((xi,), rel=10e-6)


@pytest.mark.skip(reason="pvalues not implemented")
def test_anscombes_pval():
    assert True is False
