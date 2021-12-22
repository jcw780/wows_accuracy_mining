import math
import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt
from matplotlib.colors import Normalize as normalize

sigma = 1.9
dispersion = 240
fallAngle = 18.989
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

size = 1250

fig = plt.figure(figsize=(8,8))
'''graph = fig.add_subplot(121)
graph.set_xlim([-size, size])
graph.set_ylim([-size, size])
graph.hexbin(x, y, gridsize=(100, 100), norm=normalize(vmin=0, vmax=100))'''
'''
scatter = fig.add_subplot(111)
scatter.set_xlim([-size, size])
scatter.set_ylim([-size, size])
scatter.scatter(x, y, s=0.0001)
'''
plt.show()