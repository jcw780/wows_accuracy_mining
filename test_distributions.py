import math
import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt
from matplotlib.colors import Normalize as normalize

sigma = 1.9
dispersion = 160
fallAngle = 7.607
verticalCompression = 1/np.sin(np.deg2rad(fallAngle))

nsCDF = norm.cdf(-1*sigma)

def generateDispersion(uniform):
    return norm.ppf(
        uniform*(norm.cdf(sigma)-nsCDF)+nsCDF
    ) * dispersion / sigma

points = 100000
uniformValues = np.random.rand(points)
angle = math.pi * np.random.rand(points)
output = generateDispersion(uniformValues)
print(output)
x = np.cos(angle) * output
y = np.sin(angle) * output * verticalCompression

fig = plt.figure(figsize=(7,7))
graph = fig.add_subplot(111)
graph.set_xlim([-600, 600])
graph.set_ylim([-600, 600])
graph.hexbin(x, y, gridsize=(100, 100), norm=normalize(vmin=0, vmax=100))

plt.show()