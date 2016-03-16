import rasterio

# ---
@profile
def multiplying_one_raster_by_a_constant():
    with rasterio.open('data/rasterio/R.byte.tif') as src:
        arr = src.read()

    arr = arr * 3

    with rasterio.open('data/rasterio/multiplying_one_raster_by_a_constant.tif', 'w', **src.meta) as dst:
        dst.write_band(1, arr[0])

multiplying_one_raster_by_a_constant()
