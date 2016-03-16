# Benchmark for read of raster data to ndarray

import timeit
import math

def floor(n):
    return int(math.floor(n))

def mean(l):
    return sum(l) / len(l)

def median(l):
    return quantile(l, 2)

def quantile(l, partition, partitions=4):
    return l[floor(partition * len(l) / partitions)]

def summary_statistics(l):
    return {
        'min': min(l),
        'mean': mean(l),
        'median': median(l),
        'max': max(l),
        'first_quartile': quantile(l, 1),
        'third_quartile': quantile(l, 3)
    }

def microseconds(t):
    return t * 1000

def profile(stmt='pass', setup='pass'):
    n = 100
    t = timeit.Timer(stmt, setup)
    results = [microseconds(x / n) for x in t.repeat(repeat=n, number=n)]
    return summary_statistics(results)

# Rasterio
s = """
with rasterio.open('data/rasterio/RGB.byte.tif') as src:
    arr = src.read(1, masked=False)
"""

p = profile(s, setup='import rasterio')
print("Rasterio read a file:")
print(p)

# Rasterio
s = """
with rasterio.open('data/rasterio/RGB.byte.tif') as src:
    transform = src.affine
    proj = src.crs
    wkt = src.crs_wkt
    arr = src.read(1, masked=False)
"""

p = profile(s, setup='import rasterio')
print("Rasterio read a file and its metadata:")
print(p)
