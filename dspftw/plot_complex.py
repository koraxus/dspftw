# vim: expandtab tabstop=4 shiftwidth=4

from numpy import ndarray

import matplotlib.pyplot as plt

def plot_complex(*args, **kwargs) -> plt.Figure:
    '''
    Plots complex data in the complex plane.

    Parameters
    ----------
    complex_array: array_like
        The complex array to plot
    kwargs: dict
        Parameters passed through to plt.Figure.scatter().

    '''
    plotargs = []

    for arg in args:
        if type(arg) is ndarray:
            plotargs.append(arg.real)
            plotargs.append(arg.imag)
        else:
            plotargs.append(arg)

    plt.plot(*plotargs, **kwargs)


def plotc(*args, **kwargs) -> plt.Figure:
    '''
    An alias of plot_complex().
    '''
    return plot_complex(*args, **kwargs)