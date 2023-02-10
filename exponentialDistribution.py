import math


def exponential_prob(lam, x):
    return 1 - math.exp(-lam * x)


lam = 2.5  # rate of events
x = 2      # time interval

result = exponential_prob(lam, x)

print("The probability of an event happening in the first",
      x, "seconds with rate", lam, "per second is", result)
