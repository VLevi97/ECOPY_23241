import random
import math
import typing
import scipy.special
from typing import List
import pyerf

class NormalDistribution:
    def __init__(self, rand, loc, scale):
        self.rand = rand
        self.loc = loc
        self.scale = scale

    def pdf(self, x):
        exponent = -0.5 * (((x - self.loc) / self.scale) ** 2)
        normalization = 1 / (self.scale * math.sqrt(2 * math.pi))
        probability_density = normalization * math.exp(exponent)
        return probability_density

    def cdf(self, x):
        z = (x - self.loc) / (self.scale * math.sqrt(2))
        cumulative_probability = 0.5 * (1 + math.erf(z))
        return cumulative_probability

    def ppf(self, p):
        if self.scale <= 0:
            raise ValueError("A szórásnak pozitívnak kell lennie.")
        if p < 0 or p > 1:
            raise ValueError("A valószínűségnek 0 és 1 között kell lennie.")

        z = math.erfinv(2 * p - 1) * math.sqrt(2)
        x = z * self.scale + self.loc
        return x

    def gen_rand(self):
        if self.scale <= 0:
            raise ValueError("A szórásnak pozitívnak kell lennie.")

        z = random.normalvariate(0, 1)
        x = z * self.scale + self.loc
        return x

    def mean(self):
        return self.loc

    def median(self):
        return self.loc

    def variance(self):
        if self.scale is None:
            raise Exception("Moment undefined")
        return self.scale ** 2

    def skewness(self):
        return 0

    def ex_kurtosis(self):
        return 0

    def mvsk(self):
        mean = self.loc
        variance = self.scale ** 2
        std_dev = math.sqrt(variance)
        skewness = 0
        kurtosis = 0

        return [mean, std_dev, skewness, kurtosis]



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
        if self.dof:
            return 2 * self.dof
        else:
            raise Exception("Moment undefined")

    def skewness(self):
        if self.dof:
            return math.sqrt(8 / self.dof)
        else:
            raise Exception("Moment undefined")

    def ex_kurtosis(self):
        if self.dof:
            return 12 / self.dof
        else:
            raise Exception("Moment undefined")


    def mvsk(self):
        moments = [self.mean(), self.variance(), self.skewness(), self.ex_kurtosis()]
        return moments


class UniformDistribution:
    def __init__(self, rand, a, b):
        self.rand = rand
        self.a = a
        self.b = b

    def pdf(self, x):
        if self.a >= self.b:
            raise ValueError("Az alsó határnak kisebbnek kell lennie, mint a felső határ.")

        if x < self.a or x > self.b:
            return 0
        else:
            interval_length = self.b - self.a
            probability_density = 1 / interval_length
            return probability_density

    def cdf(self, x):
        if self.a >= self.b:
            raise ValueError("Az alsó határnak kisebbnek kell lennie, mint a felső határ.")

        if x < self.a:
            return 0
        elif x >= self.b:
            return 1
        else:
            interval_length = self.b - self.a
            cumulative_probability = (x - self.a) / interval_length
            return cumulative_probability

    def ppf(self, p):
        if self.a >= self.b:
            raise ValueError("Az alsó határnak kisebbnek kell lennie, mint a felső határ.")
        if p < 0 or p > 1:
            raise ValueError("A valószínűségnek 0 és 1 között kell lennie.")

        x = self.a + p * (self.b - self.a)
        return x

    def gen_rand(self):
        x = random.uniform(self.a, self.b)
        return x

    def mean(self):
        return (self.a + self.b) / 2

    def median(self):
        return (self.a + self.b) / 2

    def variance(self):
        return ((self.b - self.a) ** 2) / 12

    def skewness(self):
        return 0

    def ex_kurtosis(self):
        return -6 / 5

    def mvsk(self):
        if self.a is None or self.b is None:
            raise Exception("Moments undefined")

        mean = (self.a + self.b) / 2
        variance = ((self.b - self.a) ** 2) / 12
        skewness = self.skewness()
        kurtosis = -6 / 5

        return [mean, variance, skewness, kurtosis]





class CauchyDistribution:
    def __init__(self, rand, loc, scale):
        self.rand = rand
        self.loc = loc
        self.scale = scale

    def pdf(self, x):
        if self.scale <= 0:
            raise ValueError("A skála értékének pozitívnak kell lennie.")

        denominator = math.pi * self.scale * (1 + ((x - self.loc) / self.scale) ** 2)
        probability_density = 1 / denominator
        return probability_density

    def cdf(self, x):
        if self.scale <= 0:
            raise ValueError("A skála értékének pozitívnak kell lennie.")

        cumulative_probability = 0.5 + math.atan((x - self.loc) / self.scale) / math.pi
        return cumulative_probability

    def ppf(self, p):
        if self.scale <= 0:
            raise ValueError("A skála értékének pozitívnak kell lennie.")
        if p < 0 or p > 1:
            raise ValueError("A valószínűségnek 0 és 1 között kell lennie.")

        x = self.loc + self.scale * math.tan(math.pi * (p - 0.5))
        return x

    def gen_rand(self):
        if self.scale <= 0:
            raise ValueError("A skála értékének pozitívnak kell lennie.")

        z = random.uniform(0, 1)
        x = self.loc + self.scale * math.tan(math.pi * (z - 0.5))
        return x

    def mean(self):
        raise Exception('Moments undefined')

    def median(self):
        return self.loc

    def variance(self):
        raise Exception('Moments undefined')

    def skewness(self):
        raise Exception('Moments undefined')

    def ex_kurtosis(self):
        raise Exception('Moments undefined')

    def mvsk(self):
        mean = self.mean()
        variance = self.variance()
        skewness = self.skewness()
        ex_kurtosis = self.ex_kurtosis()

        try:
            return [mean, variance, skewness, ex_kurtosis]
        except:
            raise Exception("Moments undefined")

