#Fit an excel like smooth curve, return a function of the curve
import numpy as np
from scipy.interpolate import Akima1DInterpolator

def Spline_fit(x, y, extend=True):
    c = np.asarray([x, y])
    d = c[:,c[0].argsort()]
    x, y = d[0], d[1]
    f = Akima1DInterpolator(x, y)
    x_min, x_max = x[0], x[-1]

    if extend:
        def output(x1):
            if x1 <= x_max and x1 >= x_min:
                return f(x1)
            elif x1 < x_min:
                return y[0]
            else:
                return y[-1]
            return out
        output1 = np.vectorize(output)
        return output1
    else:
        def output(x1):
            if x1 <= x_max and x1 >= x_min:
                return f(x1)
            elif x1 < x_min:
                return '-inf'
            else:
                return 'inf'
            return out
        output1 = np.vectorize(output)
        return output1
