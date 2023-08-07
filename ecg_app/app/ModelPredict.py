import logging
from pathlib import Path
from typing import Union

import numpy as np
import tensorflow as tf

from app.exceptions.ModelPredictError import ModelPredictError


class ModelPredict:
    def __init__(
        self,
        saved_model_path: Union[Path, str] = Path("models/ecg_inversion_model.keras"),
    ) -> None:
        logger = logging.getLogger("MainLogger")
        logger.info("Initialized model prediction module")
        self.model = tf.keras.models.load_model(saved_model_path, compile=False)

    def predict(self, ecg_signal: np.ndarray) -> dict:
        logger = logging.getLogger("MainLogger")

        expected_shape = (12, 2500)

        if ecg_signal.shape != expected_shape:
            logger.critical(
                f"Input data isn't in the required shape. "
                f"Expected {expected_shape} but got {ecg_signal.shape}."
            )
            raise ModelPredictError(
                f"Input data isn't in the required shape. "
                f"Expected {expected_shape} but got {ecg_signal.shape}."
            )

        ecg_signal_reshaped = ecg_signal.reshape((1, *expected_shape, 1))
        logger.info(f"Input data reshaped to {(1,*expected_shape, 1)}.")

        logger.info("Predicting from the input data ...")
        ecg_inv_prediction = self.model.predict(ecg_signal_reshaped)
        logger.info("Prediction made for input data.")

        returned_dict = {}

        if ecg_inv_prediction < 0.5:
            returned_dict["Inversion"] = "Correctly realized"
        else:
            returned_dict["Inversion"] = "Inverted"

        returned_dict["Prediction"] = str(ecg_inv_prediction[0, 0])

        return returned_dict
