import rasterio

# ---
@profile
def writing_one_raster():
    with rasterio.open('data/rasterio/RGB.byte.tif') as src:
        arr = src.read()

    with rasterio.open('data/rasterio/writing_one_raster.tif', 'w', **src.meta) as dst:
        i = 1
        for band in arr:
            dst.write_band(i, band)
            i += 1
writing_one_raster()
