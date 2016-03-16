import os.path

import numpy
import rasterio
from rasterio import transform
from rasterio.warp import reproject, RESAMPLING

# Data from: http://forecast.io/quicksilver/

DATA_DIR = os.path.join(os.path.abspath(os.path.join('..', '..')), 'data')

TIFF_28 = os.path.join(DATA_DIR, '2013_08_28_15.tif')
TIFF_29 = os.path.join(DATA_DIR, '2014_02_28_15.tif')
TIFF_28_29_CHANGED = os.path.join(DATA_DIR, '2013_08-2014-02_28_15_changed.tif')

with rasterio.drivers():
    with rasterio.open(TIFF_28) as src28:
        d28 = src28.read()
    with rasterio.open(TIFF_29) as src29:
        d29 = src29.read()

    changed = d29 - d28

    # changed's shape is (1, X, Y) and it should be (X, Y)
    changed = changed[0,:,:]

    kwargs = src28.meta
    kwargs.update(
        dtype=rasterio.uint16,
        count=1,
        compress='lzw')

    with rasterio.open(TIFF_28_29_CHANGED, 'w', **kwargs) as dst:
        dst.write_band(1, changed)
