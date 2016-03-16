# Benchmark for read of raster data to ndarray

import timeit
import math
import os
import os.path
import gc
import json

IMPLEMENTATION = 'rasterio'  # arcpy

def floor(n):
    return int(math.floor(n))

def mean(dataset):
    return sum(dataset) / len(dataset)

def median(dataset):
    return quantile(dataset, 2)

def quantile(dataset, partition, partitions=4):
    return dataset[floor(partition * len(dataset) / partitions)]

def summary_statistics(dataset):
    return {
        'min': min(dataset),
        'mean': mean(dataset),
        'median': median(dataset),
        'max': max(dataset),
        'first_quartile': quantile(dataset, 1),
        'third_quartile': quantile(dataset, 3),
        'dataset': dataset
    }

def microseconds(t):
    return t * 1000

def profile(stmt='pass', setup='pass', run_gc=False):
    n = 40
    setup = '\ndef profile(f):\n    return f\n\ngc.collect();' + setup
    if run_gc:
        setup = 'gc.enable();' + setup
    t = timeit.Timer(stmt, setup)
    results = [microseconds(x / n) for x in t.repeat(repeat=n, number=n)]
    return summary_statistics(results)

results = {IMPLEMENTATION: {}}

benchmarks_dir = os.path.abspath(os.path.join("scripts", IMPLEMENTATION, "benchmarks"))

for filename in os.listdir(benchmarks_dir):
    with open(os.path.join(benchmarks_dir, filename)) as f:
        benchmark = f.read()
    setup, stmt = benchmark.split('# ---')
    # print 'Benchmarking:', filename
    results[IMPLEMENTATION][filename] = profile(stmt, setup)
    results[IMPLEMENTATION][filename + 'withGCon'] = profile(stmt, setup, True)
print json.dumps(results)
