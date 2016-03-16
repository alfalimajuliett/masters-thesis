import arcpy
arcpy.env.overwriteOutput=True

# ---
@profile
def writing_one_raster():
    src = arcpy.Raster('data/rasterio/RGB.byte.tif')
    src.save('data/rasterio/arcpy_writing_one_raster.tif')

writing_one_raster()
