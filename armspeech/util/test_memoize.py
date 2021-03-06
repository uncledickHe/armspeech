"""Unit tests for function memoization."""

# Copyright 2011, 2012, 2013, 2014, 2015 Matt Shannon

# This file is part of armspeech.
# See `License` for details of license and warranty.

import unittest

from codedep import codeDeps

from armspeech.util.memoize import memoize

@codeDeps()
class FnEval(object):
    def __init__(self, f):
        self.f = f

        self.evalCount = 0

    def __call__(self, x):
        self.evalCount += 1
        return self.f(x)

@codeDeps(FnEval, memoize)
class TestMemoize(unittest.TestCase):
    def test_memoize(self):
        def f(x):
            return x * x
        fe = FnEval(f)
        fm = memoize(fe)
        assert fe.evalCount == 0
        x1 = 0.1
        x2 = 0.2
        x3 = 0.3
        assert fm(x1) == f(x1)
        assert fe.evalCount == 1
        assert fm(x2) == f(x2)
        assert fe.evalCount == 2
        assert fm(x1) == f(x1)
        assert fe.evalCount == 2
        assert fm(x2) == f(x2)
        assert fe.evalCount == 2
        assert fm(x2) == f(x2)
        assert fe.evalCount == 2
        assert fm(x3) == f(x3)
        assert fe.evalCount == 3

@codeDeps(TestMemoize)
def suite():
    return unittest.TestLoader().loadTestsFromTestCase(TestMemoize)

if __name__ == '__main__':
    unittest.main()
