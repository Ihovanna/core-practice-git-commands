import pytest


def always_returns_true():
    print ("Hi Ihovanna")
    return False
    #why isn't this working lol


def test_always_returns_true():
    assert always_returns_true()
