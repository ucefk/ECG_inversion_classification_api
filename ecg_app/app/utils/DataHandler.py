import logging
from pathlib import Path
from typing import Union

import numpy as np


class DataHandler:
    def process_data(self, data_file: Union[Path, str]) -> None:
        logger = logging.getLogger("MainLogger")
        try:
            np_data = np.loadtxt(data_file, delimiter=",")
        except:
            logger.critical(f"{data_file} does not existe.")
            raise FileNotFoundError(f"{data_file} does not existe.")

        logger.info(f"Data loaded from {data_file}")
        return np_data
