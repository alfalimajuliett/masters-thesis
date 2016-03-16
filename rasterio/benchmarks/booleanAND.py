import rasterio
import numpy

# ---
@profile
def booleanAND():
    with rasterio.open('data/rasterio/R.byte.tif') as src:
        a = src.read() > 0


    with rasterio.open('data/rasterio/G.byte.tif') as src:
        b = src.read() > 0

    arr = b & a

    # convert back to int:
    arr = (arr * 255).astype('uint8')

    with rasterio.open('data/rasterio/boolean_and.tif', 'w', **src.meta) as dst:
        dst.write_band(1, arr[0])

booleanAND()
