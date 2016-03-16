IMPLEMENTATION='rasterio'  # arcpy
for filename in scripts/${IMPLEMENTATION}/benchmarks/*; do
  /cygdrive/c/Python27/ArcGIS10.3/python -m memory_profiler $filename
done
