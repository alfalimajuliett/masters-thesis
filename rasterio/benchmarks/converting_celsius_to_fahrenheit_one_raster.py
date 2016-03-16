import rasterio

# ---
@profile
def converting_celsius_to_fahrenheit_one_raster():
    with rasterio.open('data/rasterio/R.byte.tif') as src:
        arr = src.read()

    arr = (arr * 9) / 5 + 32

    with rasterio.open('data/rasterio/converting_celsius_to_fahrenheit_one_raster.tif', 'w', **src.meta) as dst:
        dst.write_band(1, arr[0])

converting_celsius_to_fahrenheit_one_raster()
