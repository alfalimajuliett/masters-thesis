import arcpy
from arcpy.sa import ApplyEnvironment
arcpy.CheckOutExtension("Spatial")
arcpy.env.overwriteOutput=True

# ---

@profile
def converting_celsius_to_fahrenheit_one_raster():
    src = arcpy.Raster('data/rasterio/R.byte.tif')
    arcpy.env.snapRaster = src
    dst = ((src * 9) / 5 + 32) % 255
    ApplyEnvironment(dst).save('data/rasterio/arcpy_converting_celsius_to_fahrenheit_one_raster.tif')

converting_celsius_to_fahrenheit_one_raster()
