"""FastAPI app
server start command: uvicorn server:app --reload
"""
import io
import logging

import pandas as pd
import uvicorn
from fastapi import FastAPI
from fastapi import File
from fastapi import UploadFile

from app.exceptions.ServerError import ServerError
from app.Service import predict
from main import set_logger

version = "v1"

set_logger()

# FastAPI app
app = FastAPI(
    title="ECG Inversion Classification API",
    description="This API is used for classifying inverted adn correctly realized ECGs.",
)


# GET request
@app.get(path=f"/api/{version}/leads/", description="Names of an ECG leads.")
def get_leads():
    """Returns the names of ECG leads.
    Handles a GET request sent to the app.
    Corresponding cURL command: '''
        curl -X 'GET' \
            'http://localhost:8000/api/v1/classes/' \
            -H 'accept: application/json'
    '''

    Returns:
        dict
            Response to the GET request.

    """
    leads_names = ["I", "II", "III", "AVF", "AVL", "AVR", "V1", "V2", "V3", "V4", "V5", "V6"]

    return {"response": {"leads_names": leads_names}}


# GET request
@app.get(path=f"/api/{version}/classes/", description="Classes predicted by the inference model.")
def get_classes():
    """Returns the classes predicted by the model
    Handles a GET request sent to the app.
    Corresponding cURL command: '''
        curl -X 'GET' \
            'http://localhost:8000/api/v1/leads/' \
            -H 'accept: application/json'
    '''

    Returns:
        dict
            Response to the GET request.

    """
    classes = {
        "0": "Correctly realized",
        "1": "Inverted",
    }

    return {"response": {"classes": classes}}


# POST request
@app.post(
    path=f"/api/{version}/inversion/", description="Inference API for the classification of ECG."
)
async def predict_inv_class(file: UploadFile = File(...)):
    """Predict if the ECG signal is inverted or is
    correctly realized.
    Handles a POST request sent to the app.
    The POST request contains a file to be sent to
    image captioning handler module.
    The file passed in the POST request is a csv file
    of 12 rows and 2500 columns with no header.
    Corresponding cURL command: '''
        curl -X 'POST' \
            'http://localhost:8000/api/v1/inversion/' \
            -H 'accept: application/json' \
            -H 'Content-Type: multipart/form-data' \
            -F 'file=@file_name.csv;type=text/csv'
    '''

    Args:
        file : fastapi.UploadFile
            File to pass in the POST request

    Returns:
        dict
            Response to the POST request.

    Raises:
        ServerError:
            If file uploading fails.

    """
    logger = logging.getLogger("MainLogger")
    try:
        contents = file.file.read()
        df_contents = pd.read_csv(io.StringIO(contents.decode("utf-8")), header=None)
        logger.info(f"df_contents.values.shape: {df_contents.values.shape}")

        output = predict(df_contents.values)
        logger.info(f"output: {output}")

    except ServerError as err:
        return {"message": f"There was an error uploading the file ({err})"}
    finally:
        file.file.close()

    return {"message": f"Successfully uploaded {file.filename}", "output": output}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
