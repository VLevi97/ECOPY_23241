import random
import math
from typing import List
import pyerf



class LogisticDistribution:
    def __init__(self, rand, loc, scale):
        self.rand = rand
        self.location = loc
        self.scale = scale

    def pdf(self, x):
        exp_term = math.exp(-(x - self.location) / self.scale)
        pdf = exp_term / (self.scale * (1 + exp_term)**2)
        return pdf

    def cdf(self, x):
        exp_term = math.exp(-(x - self.location) / self.scale)
        cdf = 1 / (1 + exp_term)
        return cdf

    def ppf(self, p):
        if 0 < p < 1:
            ppf = self.location - self.scale * math.log(1 / p - 1)
            return ppf
        else:
            raise ValueError("p must between 0 and 1")

    def gen_rand(self):
        u = self.rand.random()
        rand_val = self.location - self.scale * math.log(1 / u - 1)
        return rand_val

    def mean(self):
        return self.location

    def variance(self):
        var = (math.pi**2 * self.scale**2) / 3
        return var

    def skewness(self):
        return 0

    def ex_kurtosis(self):
        return 1.2

    def mvsk(self):
        return [self.mean(), self.variance(), self.skewness(), self.ex_kurtosis()]








import random
import math
from scipy.special import gamma, gammainc, gammaincinv


class ChiSquaredDistribution:
    def __init__(self, rand, dof):
        self.rand = rand
        self.dof = dof

    def pdf(self, x):
        if x < 0:
            return 0.0
        prefactor = 1 / (2 ** (self.dof / 2) * gamma(self.dof / 2))
        return prefactor * x ** (self.dof / 2 - 1) * math.exp(-x / 2)

    def cdf(self, x):
        if x < 0:
            return 0.0
        return gammainc(self.dof / 2, x / 2)

    def ppf(self, p):
        if p < 0 or p > 1:
            raise ValueError("p must be between 0 and 1")
        return 2 * gammaincinv(self.dof / 2, p)

    def gen_rand(self):
        u = self.rand.random()
        return self.ppf(u)

    def mean(self):
        if self.dof > 1:
            return self.dof
        else:
            raise Exception("Moment undefined")

    def variance(self):
        if self.dof > 2:
            return 2 * self.dof
        else:
            raise Exception("Moment undefined")

    def skewness(self):
        if self.dof > 3:
            return math.sqrt(8 / self.dof)
        else:
            raise Exception("Moment undefined")

    def ex_kurtosis(self):
        if self.dof > 4:
            return 12 / self.dof
        else:
            raise Exception("Moment undefined")

    def mvsk(self):
        moments = []
        if self.dof > 0:
            moments.append(self.mean())
        else:
            raise Exception("Moment undefined")

        if self.dof > 1:
            moments.append(self.variance())
        else:
            raise Exception("Moment undefined")

        if self.dof > 3:
            moments.append(self.skewness())
            moments.append(self.ex_kurtosis())
        else:
            raise Exception("Moment undefined")

        return moments
