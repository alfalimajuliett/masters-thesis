import rasterio

with rasterio.open('data/rasterio/RGB.byte.tif') as src:
    arr = src.read()

meta = src.meta.copy()
meta.update(count=1)

with rasterio.open('data/rasterio/R.byte.tif', 'w', **meta) as red:
    red.write_band(1, arr[0])

with rasterio.open('data/rasterio/G.byte.tif', 'w', **meta) as green:
    green.write_band(1, arr[1])

with rasterio.open('data/rasterio/B.byte.tif', 'w', **meta) as blue:
    blue.write_band(1, arr[2])
