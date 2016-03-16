import rasterio

# ---
@profile
def two_raster_formula():
    with rasterio.open('data/rasterio/R.byte.tif') as src:
        a = src.read()


    with rasterio.open('data/rasterio/G.byte.tif') as src:
        b = src.read()

    with rasterio.open('data/rasterio/B.byte.tif') as src:
        c = src.read()

    output = (a * b) + c

    with rasterio.open('data/rasterio/two_raster_formula.tif', 'w', **src.meta) as dst:
        dst.write_band(1, output[0])
two_raster_formula()
