import numpy as np

if __name__ == "__main__":
    sensor_readings = np.array([22.5, 23.1, -999.0, 24.0, 150.2, 22.8, 23.5, -999.0, 24.2])

    # 1. Extract valid entries
    valid_mask = (sensor_readings != -999.0) & (sensor_readings <= 100.0)
    valid_data = sensor_readings[valid_mask]
    print("Valid readings:", valid_data)

    # 2. Replace -999.0 with valid mean
    valid_mean = np.mean(valid_data)
    imputed_readings = np.where(sensor_readings == -999.0, valid_mean, sensor_readings)
    print("Imputed array:\n", imputed_readings)

    # 3. Total invalid/outlier count
    invalid_count = np.sum(~valid_mask)
    print("Invalid entries count:", invalid_count)