import unittest
from math import exp
import numpy as np


def approx_ode(h, t0, y0, tn):
    # Inputs - h  : step size
    #          t0 : initial t value (at step 0)
    #          y0 : initial y value (at step 0)
    #          tn : t value at step n
    # Add your code below!
    y = y0
    t = t0
    for t in np.arange(t0, tn, h):
        y = y + h * (3 + exp(-t) - 1/2*y)
    return y

# approx_ode(0.1,0,1,5) Output: 5.770729097292093
# approx_ode (0.1 ,0 ,1 ,2.5) Output: 5.045499895356848
# approx_ode(0.1,0,1,3) Output: 5.291824495018364
# approx_ode(0.1,0,1,1) Output: 3.51748514403281
# approx_ode(0.1,0,1,0) Output: 1


class Testing(unittest.TestCase):
    def test_ode1(self):
        a = approx_ode(0.1, 0, 1, 5)
        b = 5.770729097292093
        self.assertAlmostEqual(a, b, places=4)
    def test_ode2(self):
        a = approx_ode(0.1, 0, 1, 2.5)
        b = 5.045499895356848
        self.assertAlmostEqual(a, b, places=4)
    def test_ode3(self):
        a = approx_ode(0.1, 0, 1, 3)
        b = 5.291824495018364
        self.assertAlmostEqual(a, b, places=4)
    def test_ode4(self):
        a = approx_ode(0.1, 0, 1, 1)
        b = 3.51748514403281
        self.assertAlmostEqual(a, b, places=4)
    def test_ode5(self):
        a = approx_ode(0.1, 0, 1, 0)
        b = 1
        self.assertAlmostEqual(a, b, places=4)


unittest.main()
