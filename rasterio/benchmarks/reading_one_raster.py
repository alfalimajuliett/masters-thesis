import rasterio

# ---
@profile
def reading_one_raster():
    with rasterio.open('data/rasterio/RGB.byte.tif') as src:
        arr = src.read()

reading_one_raster()
