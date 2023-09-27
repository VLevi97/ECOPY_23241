import random
import math


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

    def gen_random(self) -> float:
        u = self.rand.random()
        return self.loc - self.scale * math.copysign(math.log(1 - 2 * u), self.rand.random() - 0.5)

    def mean(self) -> float:
        return self.loc

    def variance(self) -> float:
        return 2 * self.scale ** 2

    def skewness(self) -> float:
        return 0.0

    def ex_kurtosis(self) -> float:
        return 3.0

    def mvsk(self) -> List[float]:
        return [self.mean(), self.variance(), self.skewness(), self.ex_kurtosis()]