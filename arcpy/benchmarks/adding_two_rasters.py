import arcpy
from arcpy.sa import ApplyEnvironment
arcpy.CheckOutExtension("Spatial")
arcpy.env.overwriteOutput=True

# ---

@profile
def adding_two_rasters():
    a = arcpy.Raster('data/rasterio/R.byte.tif')
    b = arcpy.Raster('data/rasterio/G.byte.tif')
    arcpy.env.snapRaster = a
    dst = (a + b) % 255
    ApplyEnvironment(dst).save('data/rasterio/arcpy_adding_two_rasters.tif')

adding_two_rasters()
