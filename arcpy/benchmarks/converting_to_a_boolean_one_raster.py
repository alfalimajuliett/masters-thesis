import arcpy
from arcpy.sa import ApplyEnvironment
arcpy.CheckOutExtension("Spatial")
arcpy.env.overwriteOutput=True

# ---

@profile
def converting_to_a_boolean_one_raster():
    src = arcpy.Raster('data/rasterio/R.byte.tif')
    arcpy.env.snapRaster = src
    dst = (src > 0) * 255
    ApplyEnvironment(dst).save('data/rasterio/arcpy_converting_to_a_boolean_one_raster.tif')

converting_to_a_boolean_one_raster()
