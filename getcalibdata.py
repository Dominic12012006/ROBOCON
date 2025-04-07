import numpy as np

# load in the calibration data
calib_data_path = r"C:\Users\Happy Home\OneDrive\Desktop\ROBOCON\MultiMatrix.npz"

calib_data = np.load(calib_data_path)
print(calib_data)
