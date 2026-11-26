import pandas as pd
import numpy as np

def calculate_player_load(dataframe: pd.DataFrame) -> float:
    if len(dataframe) < 2:
        return 0.0
    
    diff_x = np.diff(dataframe['ax'])
    diff_y = np.diff(dataframe['ay'])
    diff_z = np.diff(dataframe['az'])

    # apply pythagorean theroem to each 1D array to create 3D load
    instantaneous_load = np.sqrt(np.square(diff_x) + np.square(diff_y) + np.square(diff_z))

    # cumulative stress over all samples
    player_load = np.sum(instantaneous_load) / 100.0

    return float(player_load)

if __name__ == "__main__":
    
    df_still = pd.DataFrame({"ax": [0.0, 0.0, 0.0], "ay": [0.0, 0.0, 0.0], "az": [1.0, 1.0, 1.0]})
    
    assert calculate_player_load(df_still) == 0.0

    df_jump = pd.DataFrame({"ax": [0, 3], "ay": [0, 4], "az": [1, 1]})

    assert np.isclose(calculate_player_load(df_jump), 0.05)

    df_fake = pd.read_csv("data/fake_imu.csv")
    fake_player_load = calculate_player_load(df_fake)

    print(f"player load: {fake_player_load}\n")
    print("All tests passed!")