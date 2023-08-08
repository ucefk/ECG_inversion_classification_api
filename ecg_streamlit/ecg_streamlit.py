import os
import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
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

colors = {
    "Correctly realized": "g",
    "Inverted": "r",
}

limit = 600

leads_names = ["I", "II", "III", "AVF", "AVL", "AVR", "V1", "V2", "V3", "V4", "V5", "V6"]
keys = np.arange(12)
leads_channels = dict(list(zip(keys, leads_names)))




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
        
        # st.write(dataframe)

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

        st.subheader(f"The ECG given as input is **{prediction.get('Inversion')}!** \
                     ({prediction.get('Prediction')})")
        
        fig, axs = plt.subplots(12, 1, figsize=(15, 40))

        fig.tight_layout()

        fig.subplots_adjust(hspace=0.5, wspace=0.2)

        for i in range(12):
            axs[i].plot(
                dataframe.values[i,:limit], 
                color=colors[prediction.get('Inversion')]
            )
            axs[i].set_title(
                "{} ECG: {}.".format(
                    prediction.get('Inversion'), 
                    leads_channels[i]
                )
            )

        for ax in axs.flat:
            ax.set(xlabel='Time', ylabel='Voltage')

        st.pyplot(fig)