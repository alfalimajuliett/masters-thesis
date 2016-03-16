import arcpy
from arcpy.sa import ApplyEnvironment
arcpy.CheckOutExtension("Spatial")
arcpy.env.overwriteOutput=True

# ---

@profile
def subtracting_one_raster_by_a_constant():
    src = arcpy.Raster('data/rasterio/R.byte.tif')
    arcpy.env.snapRaster = src
    dst = (src - 3) % 255
    ApplyEnvironment(dst).save('data/rasterio/arcpy_subtracting_one_raster_by_a_constant.tif')

subtracting_one_raster_by_a_constant()
