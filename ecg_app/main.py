"""Main module."""
import logging
from pathlib import Path

from app.ModelPredict import ModelPredict
from app.utils.DataHandler import DataHandler


def set_logger():
    """Sets the logger."""
    logging.basicConfig(level=logging.INFO)
    fmt = logging.Formatter("%(asctime)s [%(levelname)s]\t%(message)s", datefmt="%d/%m/%Y %I:%M:%S")
    log_output_path = "app/output/log/run.log"
    file_handler = logging.FileHandler(log_output_path, mode="w")
    console_handler = logging.StreamHandler()
    file_handler.setFormatter(fmt)
    console_handler.setFormatter(fmt)
    logger = logging.getLogger("MainLogger")
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)
    logger.propagate = False


def main():
    set_logger()
    data_handler = DataHandler()
    uploaded_data = data_handler.process_data(data_file=Path("sample_data/correct/correct_5.csv"))
    model_predict = ModelPredict()
    predictions = model_predict.predict(ecg_signal=uploaded_data)
    print(predictions["Inversion"])
    print(predictions["Prediction"])


if __name__ == "__main__":
    main()
