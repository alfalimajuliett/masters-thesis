import arcpy
from arcpy.sa import ApplyEnvironment
arcpy.CheckOutExtension("Spatial")
arcpy.env.overwriteOutput=True

# ---

@profile
def boolean_not_one_raster():
    src = arcpy.Raster('data/rasterio/R.byte.tif')
    arcpy.env.snapRaster = src
    dst = (~(src > 0)) * 255
    ApplyEnvironment(dst).save('data/rasterio/arcpy_boolean_not_one_raster.tif')

boolean_not_one_raster()
