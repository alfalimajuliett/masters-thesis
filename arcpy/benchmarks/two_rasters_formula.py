import arcpy
from arcpy.sa import ApplyEnvironment
arcpy.CheckOutExtension("Spatial")
arcpy.env.overwriteOutput=True

# ---

@profile
def two_rasters_formula():
    a = arcpy.Raster('data/rasterio/R.byte.tif')
    b = arcpy.Raster('data/rasterio/G.byte.tif')
    c = arcpy.Raster('data/rasterio/B.byte.tif')
    arcpy.env.snapRaster = a
    dst = ((a * b) + c) % 255
    ApplyEnvironment(dst).save('data/rasterio/arcpy_two_rasters_formula.tif')

two_rasters_formula()
