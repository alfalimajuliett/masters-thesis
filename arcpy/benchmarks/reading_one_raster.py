import arcpy

# ---

@profile
def reading_one_raster():
    src = arcpy.Raster('data/rasterio/RGB.byte.tif')

reading_one_raster()
