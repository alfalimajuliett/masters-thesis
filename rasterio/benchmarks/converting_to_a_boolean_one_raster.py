import rasterio
import numpy

# ---
@profile
def converting_to_boolean_one_raster():
    with rasterio.open('data/rasterio/R.byte.tif') as src:
        arr = src.read()

    arr = arr > 0

    # convert back to int:
    arr = (arr * 255).astype('uint8')

    with rasterio.open('data/rasterio/converting_to_boolean_one_raster.tif', 'w', **src.meta) as dst:
        dst.write_band(1, arr[0])

converting_to_boolean_one_raster()
