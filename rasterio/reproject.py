import os.path

import numpy
import rasterio
from rasterio import transform
from rasterio.warp import reproject, RESAMPLING

DATA_DIR = os.path.join(os.path.abspath(os.path.join('..', '..')), 'data')

TIFF_2008 = os.path.join(DATA_DIR, 'CDL_2008_clip_20141116183622_536727822.tif')
TIFF_2013 = os.path.join(DATA_DIR, 'CDL_2013_clip_20141116183622_536727822.tif')
TIFF_2013_REPROJECTED = os.path.join(DATA_DIR, 'CDL_2013_clip_20141116183622_536727822-reprojected.tif')
TIFF_2008_2013_CHANGED = os.path.join(DATA_DIR, 'CDL_2008_2013_changed.tif')

with rasterio.drivers():
    with rasterio.open(TIFF_2008) as src2008:
        d2008 = src2008.read()
    with rasterio.open(TIFF_2013) as src2013:
        d2013 = src2013.read()

    # Need to match bounds and other metadata:
    src_shape=(src2013.meta['height'],src2013.meta['width'])
    src_transform = src2013.meta['transform']
    src_crs=src2013.meta['crs']

    dst_shape=(src2008.meta['height'],src2008.meta['width'])
    dst_transform = src2008.meta['transform']
    dst_crs=src2008.meta['crs']

    destination = numpy.zeros(dst_shape, numpy.uint8)

    reproject(
        d2013,
        destination,
        src_transform=src_transform,
        src_crs=src_crs,
        dst_transform=dst_transform,
        dst_crs=dst_crs)

    with rasterio.open(
            TIFF_2013_REPROJECTED,
            'w',
            driver='GTiff',
            width=dst_shape[1],
            height=dst_shape[0],
            count=1,
            dtype=numpy.uint8,
            nodata=0,
            transform=dst_transform,
            crs=dst_crs) as dst:
        dst.write_band(1, destination)

    changed = d2008 ^ destination

    # changed's shape is (1, X, Y) and it should be (X, Y)
    changed = changed[0,:,:]

    with rasterio.open(
            TIFF_2008_2013_CHANGED,
            'w',
            driver='GTiff',
            width=dst_shape[1],
            height=dst_shape[0],
            count=1,
            dtype=numpy.uint8,
            nodata=0,
            transform=dst_transform,
            crs=dst_crs) as dst:
        dst.write_band(1, changed)
