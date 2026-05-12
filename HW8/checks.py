import rasterio
import numpy as np
import xdem
import matplotlib.pyplot as plt
from pyproj import Transformer

# #Check: check what would happen if Nuth Kaab coreg was used
# # Load raw unprocessed DEMs and sample a known pixel
# dem1 = xdem.DEM('/Users/miajacoombs/REPOS/GEOS694_ICG/Labs/Lab7/DEMs/Isabel-Horz-Alaska-AEAC/IsabelPass_DSM_2000.tif', nodata=0)
# dem2 = xdem.DEM('/Users/miajacoombs/REPOS/GEOS694_ICG/Labs/Lab7/DEMs/Canwell_4Aug25_DTM.tif', nodata=-9999)

# # Fit Nuth & Kaab
# nuth_kaab = xdem.coreg.NuthKaab()
# nuth_kaab.fit(dem2, dem1)

# print(f"Detected shift_z: {nuth_kaab.meta['outputs']['affine']['shift_z']:.2f}m")

# # Apply correction then reproject back onto dem2's grid
# dem1_coreg = nuth_kaab.apply(dem1)
# dem1_coreg = dem1_coreg.reproject(dem2, resampling="bilinear")
# dem1_coreg.set_vcrs("EGM96")

# # Difference corrected DEMs
# diff_corrected = dem2 - dem1_coreg

# # Check stable terrain offset after correction
# slope = xdem.terrain.slope(diff_corrected)
# flat_mask = (slope.data < 5) & (~np.ma.getmaskarray(diff_corrected.data))
# diff_flat = diff_corrected.data.data[flat_mask]

# print(f"\nStable terrain after coregistration:")
# print(f"  Mean offset:   {np.mean(diff_flat):.2f}m")
# print(f"  Median offset: {np.median(diff_flat):.2f}m")
# print(f"  Std dev:       {np.std(diff_flat):.2f}m")

# # Plot to visually confirm improvement
# diff_corrected.plot(cmap='RdYlBu', vmin=-20, vmax=20,
#                     cbar_title='Elevation difference after coreg (m)')

# # check c - estimate vertical difference 
# transformer = Transformer.from_crs("EPSG:32606", "EPSG:4326", always_xy=True)
# lon, lat = transformer.transform(568785.0, 7028255.0)

# transformer2 = Transformer.from_crs("EPSG:4979", "EPSG:4326+5773", always_xy=True)
# lon_out, lat_out, h_out = transformer2.transform(lon, lat, 0.0)
# print(f"Geoid separation (EGM96 - Ellipsoid) at this location: {h_out:.2f}m")

# # check b - stability 
# diff = xdem.DEM('/Users/miajacoombs/REPOS/GEOS694_ICG/Labs/Lab7/Lidar2025_IsabelIFSAR2000.tif')
# slope = xdem.terrain.slope(diff)

# flat_mask = (slope.data < 5) & (~np.ma.getmaskarray(diff.data))
# diff_flat = diff.data.data[flat_mask]

# # Plot histogram of flat terrain offsets
# plt.figure(figsize=(10, 5))
# plt.hist(diff_flat, bins=200, range=(-50, 100), color='steelblue', edgecolor='none')
# plt.axvline(np.mean(diff_flat), color='red', linestyle='--', label=f'Mean: {np.mean(diff_flat):.1f}m')
# plt.axvline(np.median(diff_flat), color='orange', linestyle='--', label=f'Median: {np.median(diff_flat):.1f}m')
# plt.axvline(0, color='black', linestyle='-', label='Zero (expected)')
# plt.xlabel('Elevation difference (m)')
# plt.ylabel('Pixel count')
# plt.title('Flat terrain elevation differences — vertical datum check')
# plt.legend()
# plt.tight_layout()
# plt.show()

# # Also check step 2 - geoid separation at this location
# from pyproj import Transformer
# transformer = Transformer.from_crs("EPSG:32606", "EPSG:4326", always_xy=True)
# lon, lat = transformer.transform(568785.0, 7028255.0)
# print(f"Glacier center: {lat:.4f}N, {lon:.4f}W")

# transformer2 = Transformer.from_crs("EPSG:4979", "EPSG:4326+5773", always_xy=True)
# lon_out, lat_out, h_out = transformer2.transform(lon, lat, 0.0)
# print(f"Geoid separation (EGM96 - Ellipsoid) at this location: {h_out:.2f}m")

# Check a
# # Check nodata type
# with rasterio.open('/Users/miajacoombs/REPOS/GEOS694_ICG/Labs/Lab7/DEMs/Isabel-Horz-Alaska-AEAC/IsabelPass_DSM_2000.tif') as src:
#     print("Nodata:", src.nodata)
#     print("Dtype:", src.dtypes)
#     # Check what value fills the blue void areas
#     import numpy as np
#     data = src.read(1)
#     print("Min value:", np.min(data))
#     print("Max value:", np.max(data))
#     print("Unique values near zero:", np.unique(data[np.abs(data) < 1]))
#     print("Value at known void pixel (top right corner):", data[0, -1])

# #Identify issue overlapping
# dem1 = xdem.DEM('/Users/miajacoombs/REPOS/GEOS694_ICG/Labs/Lab7/DEMs/Isabel-Horz-Alaska-AEAC/IsabelPass_DSM_2000.tif')
# dem2 = xdem.DEM('/Users/miajacoombs/REPOS/GEOS694_ICG/Labs/Lab7/DEMs/Canwell_4Aug25_DTM.tif')

# # Plot each DEM individually to see where data exists
# fig, axes = plt.subplots(1, 2, figsize=(14, 6))

# dem1.plot(cmap='terrain', cbar_title='Elevation (m)', ax=axes[0])
# axes[0].set_title('IFSAR — valid data extent')

# dem2.plot(cmap='terrain', cbar_title='Elevation (m)', ax=axes[1])
# axes[1].set_title('Lidar — valid data extent')

# plt.tight_layout()
# plt.show()

# Check the mask of each DEM in the lower right corner area
# The blue block appears around x=580000-588000, y=7017000-7021000
# print("IFSAR valid pixel %:", 100 * np.sum(~dem1.data.mask) / dem1.data.size)
# print("Lidar valid pixel %:", 100 * np.sum(~dem2.data.mask) / dem2.data.size)

# # Check nodata values
# print(f"\nIFSAR nodata: {dem1.nodata}")
# print(f"Lidar nodata: {dem2.nodata}")

# # Check for any values suspiciously close to zero in the blue block area
# # which would indicate unfilled nodata rather than masked nodata
# data1 = dem1.data.compressed()
# data2 = dem2.data.compressed()
# print(f"\nIFSAR pixels == 0: {np.sum(data1 == 0)}")
# print(f"Lidar pixels == 0: {np.sum(data2 == 0)}")
# print(f"IFSAR pixels < 0: {np.sum(data1 < 0)}")
# print(f"Lidar pixels < 0: {np.sum(data2 < 0)}")

# # Plot diff dem
# import xdem
# import numpy as np
# import matplotlib.pyplot as plt

# diff = xdem.DEM('/Users/miajacoombs/REPOS/GEOS694_ICG/Labs/Lab7/Lidar2025_IsabelIFSAR2000.tif')

# fig, axes = plt.subplots(1, 2, figsize=(14, 6))

# # Plot 1: tight scale to see datum-level differences
# diff.plot(cmap='RdYlBu', vmin=-50, vmax=50, 
#           cbar_title='Difference (m)', ax=axes[0])
# axes[0].set_title('Tight scale (-50 to 50m)')

# # Plot 2: wide scale to see the full range
# diff.plot(cmap='RdYlBu', vmin=-500, vmax=500,
#           cbar_title='Difference (m)', ax=axes[1])
# axes[1].set_title('Wide scale (-500 to 500m)')

# plt.tight_layout()
# plt.show()

# #Check for spatially uniform error
# # Load your diff dem after processing
# import xdem
# import numpy as np

# diff = xdem.DEM('/Users/miajacoombs/REPOS/GEOS694_ICG/Labs/Lab7/Lidar2025_IsabelIFSAR2000.tif')

# data = diff.data

# print(f"Array dtype: {data.dtype}")
# print(f"Nodata value: {diff.nodata}")
# print(f"Total pixels: {data.size}")
# print(f"Masked pixels: {np.sum(data.mask)}")
# print(f"Valid pixels: {np.sum(~data.mask)}")
# print(f"Valid %: {100 * np.sum(~data.mask) / data.size:.1f}%")

# # Stats on valid only
# valid = data.compressed()
# print(f"\nStats on valid pixels only:")
# print(f"  Mean:   {np.mean(valid):.2f}m")
# print(f"  Std:    {np.std(valid):.2f}m")
# print(f"  Min:    {np.min(valid):.2f}m")
# print(f"  Max:    {np.max(valid):.2f}m")
# print(f"  Median: {np.median(valid):.2f}m")
# print(f"  10th percentile: {np.percentile(valid, 10):.2f}m")
# print(f"  90th percentile: {np.percentile(valid, 90):.2f}m")

# # Check if nodata value is actually being masked correctly
# print(f"\nPixels equal to nodata value ({diff.nodata}): {np.sum(data.data == diff.nodata)}")
# print(f"Pixels that are NaN: {np.sum(np.isnan(data.data))}")
# print(f"Pixels > 500m difference (suspiciously large): {np.sum(np.abs(valid) > 500)}")

# # Check dem stats
# for path, name in [
#     ('/Users/miajacoombs/REPOS/GEOS694_ICG/Labs/Lab7/DEMs/Isabel-Horz-Alaska-AEAC/IsabelPass_DSM_2000.tif', 'Isabel Pass-1'),
#     ('/Users/miajacoombs/REPOS/GEOS694_ICG/Labs/Lab7/DEMs/Canwell_4Aug25_DTM.tif', 'Lidar -2')
# ]:
#     with rasterio.open(path) as src:
#         data = src.read(1)
#         valid = data[data != src.nodata]
#         print(f"\n{name}:")
#         print(f"  Min: {np.min(valid):.2f}m")
#         print(f"  Max: {np.max(valid):.2f}m")
#         print(f"  Mean: {np.mean(valid):.2f}m")
#         print(f"  Upper left: {src.bounds.left:.2f}, {src.bounds.top:.2f}")
#         print(f"  Pixel size: {src.res}")
#         print(f"  CRS: {src.crs}")


# Check g: check real crs 
with rasterio.open('~/IFSAR_DSM_Summer_2010.tif') as src:
    print(src.crs)
    print(src.crs.to_wkt())
    print("CRS from metadata:", src.crs)
    print("Upper left corner:", src.bounds.left, src.bounds.top)
    print("Lower right corner:", src.bounds.right, src.bounds.bottom)
    print("Pixel size:", src.res)
    print("\n=== Vertical ===")
    # Try to extract vertical CRS from the full WKT
    try:
        full_crs = CRS.from_wkt(src.crs.to_wkt())
        if full_crs.is_compound:
            sub_crs = full_crs.sub_crs_list
            print("Compound CRS detected:")
            for c in sub_crs:
                print(f"  - {c.name} | type: {c.type_name} | EPSG: {c.to_epsg()}")
        elif full_crs.is_vertical:
            print("Vertical CRS:", full_crs.name)
        else:
            print("No vertical CRS found in metadata — must be assigned manually")
    except Exception as e:
        print(f"Could not parse vertical CRS: {e}")
