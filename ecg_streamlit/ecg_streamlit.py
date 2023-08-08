import os
import requests
import pandas as pd
import streamlit as st

# Title
st.title("ECG Inversion Classification")

st.write(
    "ECG inversion classification.\
    Upload the csv file containing the 12 leads \
    to classify whether the ECG is correctly classified or inverted."
)

ecg_file = st.file_uploader(
    label="Choose a CSV file", 
    type="csv",
    accept_multiple_files=False,
)

if ecg_file is not None:

    if st.button("Submit"):

        dataframe = pd.read_csv(ecg_file, header=None)

        if not os.path.isdir("./tmp/"):
            os.mkdir("./tmp")

        dataframe.to_csv(
            path_or_buf="./tmp/tmp.csv",
            index=False,
            header=False,
        )
        st.write(dataframe)

        files = {'file': open('./tmp/tmp.csv', 'r')}
            
        response = requests.post(
            f"http://host.docker.internal:8001/api/v1/inversion/", 
            # f"http://localhost:8001/api/v1/inversion/", 
            files=files, 
            verify=False
        )

        # response = requests.get('http://localhost:8001/api/v1/classes/')
        
        json_response = response.json()

        prediction = json_response.get("output")

        st.subheader(f"The prediction is **{json_response}!**")