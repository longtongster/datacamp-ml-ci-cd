DATASET_TYPES = ["test", "train"]
DROP_COLNAMES = ["row ID"]
TARGET_COLUMN = "RainTomorrow"
RAW_DATASET = "./dvc_tracked_dataset/weather_training_data.csv"
PROCESSED_DATASET = "./processed_dataset/weather.csv"


def delete_and_recreate_dir(path):
    try:
        shutil.rmtree(path)
    except:
        pass
    finally:
        Path(path).mkdir(parents=True, exist_ok=True)
