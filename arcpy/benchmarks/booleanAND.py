import arcpy
from arcpy.sa import ApplyEnvironment
arcpy.CheckOutExtension("Spatial")
arcpy.env.overwriteOutput=True

# ---

@profile
def boolean_and():
    a = arcpy.Raster('data/rasterio/R.byte.tif') > 0
    b = arcpy.Raster('data/rasterio/G.byte.tif') > 0
    arcpy.env.snapRaster = a
    dst = (a & b) * 255
    ApplyEnvironment(dst).save('data/rasterio/arcpy_boolean_and.tif')

boolean_and()
