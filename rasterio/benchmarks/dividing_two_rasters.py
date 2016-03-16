import rasterio

# ---
@profile
def dividing_two_rasters():
    with rasterio.open('data/rasterio/R.byte.tif') as src:
        a = src.read()


    with rasterio.open('data/rasterio/G.byte.tif') as src:
        b = src.read()

    output = a / b

    with rasterio.open('data/rasterio/dividing_two_rasters.tif', 'w', **src.meta) as dst:
        dst.write_band(1, output[0])

dividing_two_rasters()
