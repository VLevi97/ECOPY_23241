import random
import math
from math import sqrt, pi


class LaplaceDistribution:
    def __init__(self, rand: random.Random, loc: float, scale: float):
        self.rand = rand
        self.loc = loc
        self.scale = scale

    def pdf(self, x: float) -> float:
        return 0.5 * math.exp(-abs(x - self.loc) / self.scale) / self.scale

    def cdf(self, x: float) -> float:
        if x < self.loc:
            return 0.5 * math.exp((x - self.loc) / self.scale)
        else:
            return 1 - 0.5 * math.exp(-(x - self.loc) / self.scale)

    def ppf(self, p: float) -> float:
        if p < 0 or p > 1:
            raise ValueError("Probability value must be in [0, 1]")
        if p < 0.5:
            return self.loc + self.scale * math.log(2 * p)
        elif p == 0.5:
            return self.loc
        else:
            return self.loc - self.scale * math.log(2 - 2 * p)

    def gen_rand(self):
        u = self.rand.random()
        return self.ppf(u)


    def mean(self) -> float:
        return self.loc

    def variance(self) -> float:
        return 2 * self.scale ** 2

    def skewness(self) -> float:
        return 0.0

    def ex_kurtosis(self) -> float:
        return 3.0

    def mvsk(self):
        return [self.mean(), self.variance(), self.skewness(), self.ex_kurtosis()]


class ParetoDistribution:
    def __init__(self, rand, scale, shape):
        self.rand = rand
        self.scale = scale
        self.shape = shape

    def pdf(self, x):
        if x < self.scale:
            return 0
        return (self.shape * self.scale**self.shape) / (x**(self.shape + 1))

    def cdf(self, x):
        if x < self.scale:
            return 0
        return 1 - (self.scale/x)**self.shape

    def ppf(self, p):
        if p < 0 or p > 1:
            raise ValueError("p must be between 0 and 1")
        return self.scale / pow(1 - p, 1/self.shape)

    def gen_rand(self):
        u = self.rand.random()
        return self.ppf(u)

    def mean(self):
        if self.shape <= 1:
            raise Exception("Moment undefined")

        return (self.shape * self.scale) / (self.shape - 1)

    def variance(self):
        if self.shape <= 2:
            raise Exception("Moment undefined")
        return (self.scale ** 2 * self.shape) / ((self.shape - 1) ** 2 * (self.shape - 2))

    def skewness(self):
        if self.shape <= 3:
            raise Exception("Skewness undefined")
        return (2 * (1 + self.shape)) / (self.shape - 3) * ((self.shape - 2) / self.shape) ** 0.5

    def ex_kurtosis(self):
        if self.shape <= 4:
            raise Exception("Excess Kurtosis undefined")
        return 6 * (self.shape ** 3 + self.shape ** 2 - 6 * self.shape - 2) / \
            (self.shape * (self.shape - 3) * (self.shape - 4))

    def mvsk(self):
        if self.shape <= 4:
            raise Exception("Moment undefined")

        mean = self.mean()
        variance = self.variance()
        skewness = self.skewness()
        ex_kurtosis = self.ex_kurtosis()

        return [mean, variance, skewness, ex_kurtosis]