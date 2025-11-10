import math
from pprint import pprint

import matplotlib.pyplot as plt

# source: https://companiesmarketcap.com/cisco/revenue/
# source2: https://www.macrotrends.net/stocks/charts/CSCO/cisco/stock-price-history
year_close = {
    2024: 59.2000,
    2023: 48.9301,
    2022: 44.7662,
    2021: 57.7309,
    2020: 39.6074,
    2019: 41.0582,
    2018: 36.0732,
    2017: 30.9460,
    2016: 23.5740,
    2015: 20.4652,
    2014: 20.3383,
    2013: 15.9006,
    2012: 13.6223,
    2011: 12.2068,
    2010: 13.5076,
    2009: 15.9848,
    2008: 10.8836,
    2007: 18.0747,
    2006: 18.2483,
    2005: 11.4311,
    2004: 12.9000,
    2003: 16.1785,
    2002: 8.7469,
    2001: 12.0921,
    2000: 25.5397,
    1999: 35.7555,
    1998: 15.5241,
    1997: 6.2041,
    1996: 4.7199
}

data: dict[int, float] = {
    2024: 54.17,
    2023: 57.23,
    2022: 53.16,
    2021: 51.54,
    2020: 48.02,
    2019: 51.55,
    2018: 50.82,
    2017: 48.09,
    2016: 48.57,
    2015: 49.58,
    2014: 48.08,
    2013: 47.87,
    2012: 47.25,
    2011: 44.84,
    2010: 42.36,
    2009: 35.53,
    2008: 39.57,
    2007: 37.68,
    2006: 31.92,
    2005: 25.94,
    2004: 23.57,
    2003: 19.81,
    2002: 19.20,
    2001: 18.29,
    2000: 23.94,
    1999: 15.03,
    1998: 10.01,
    1997: 7.29,
    1996: 5.68
}

# Extract years and values
years = list(data.keys())
d1values = list(data.values())

length = 4
# [n-th derivative][point] where when point=-1, the center of the series is.
derivatives: list[list[float]] = [d1values[::-1][0:length + 1]]
for n in range(1, length + 1):
    derivatives.append([])
    for i in range(0, length - n + 1):
        derivatives[n].append(derivatives[n - 1][i + 1] - derivatives[n - 1][i])

# print(derivatives)
taylor_approx_coeffs = [ders[-1] for ders in derivatives]
print("Taylor Series Coefficients:",
      *[f"{taylor_approx_coeffs[i]:.2f}x^{i} + " for i in range(length)], flush=False, end="")
print("\b\b\b")


def taylor_approx(coeffs: list[float], x: float, offset: float = 0) -> float:
    output = 0
    for i in range(len(coeffs)):
        output += coeffs[i] * math.pow(x - offset, i) / math.factorial(i)
    return output


cut = 2004
data2: dict[int, float] = {year: taylor_approx(taylor_approx_coeffs, year, offset=2000) for year in range(1996, cut)}
d2values = list(data2.values())

# Create the plot

# plt.figure(figsize=(8, 6))  # Set figure size
plt.figure(figsize=(8, 8))  # Set figure size
plt.subplot(211)
plt.plot(data.keys(), data.values(), linestyle='-', color='tab:blue', label='הכנסות'[::-1])
plt.plot(list(data2.keys()), d2values, marker='o', linestyle='--', color='tab:green', label="קירוב טיילור"[::-1])
plt.legend()

plt.title("הכנסות על פני זמן"[::-1], fontsize=16)
plt.ylabel("הכנסות )מיליארדי דולרים("[::-1], fontsize=12)

plt.grid(alpha=0.5)

plt.subplot(212)
plt.title("שווי מנייה על פני זמן"[::-1], fontsize=16)
plt.plot(year_close.keys(), year_close.values(), color='tab:red')
plt.ylabel("דולרים"[::-1], fontsize=12)
plt.grid(alpha=0.5)


plt.tight_layout()
plt.show()
