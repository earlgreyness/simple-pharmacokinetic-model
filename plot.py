#!/usr/bin/env python3
from functools import lru_cache
import math

import click
import matplotlib.pyplot as plt
import numpy as np


def F(t, halflife):
    if t <= 0:
        return 1
    return math.exp(-0.69 * t / halflife)


@lru_cache()
def g(n, period, halflife):
    if n == 0:
        return 1
    return g(n - 1, period, halflife) * F(period, halflife) + 1


@lru_cache()
def f(t, period, halflife):
    if t <= 0:
        return 1
    n = int(t // period)
    return g(n, period, halflife) * F(t - n * period, halflife)


@click.command()
@click.argument('halflife', type=int)
@click.argument('period', type=int)
@click.option('--save', is_flag=True)
def main(halflife, period, save):
    time = np.arange(0, 180, 0.25)
    concentration = np.array([f(x, period, halflife) for x in time])

    figure, ax = plt.subplots()

    ax.plot(time, concentration)
    ax.set(
        xlabel='Time (hours)',
        ylabel='Drug concentration (pills)',
        title=f'Half-life: {halflife} hours, dosing frequency: {period} hours'
    )
    ax.grid()

    if save:
        figure.savefig(f'pharmacokinetic-curve-{halflife}-{period}.png')
    plt.show()


if __name__ == '__main__':
    main()
