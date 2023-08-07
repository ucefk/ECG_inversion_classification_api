from app.ModelPredict import ModelPredict


def predict(contents):
    # data_handler = DataHandler()
    # uploaded_data = data_handler.process_data(data_file=Path("sample_data/correct/correct_5.csv"))
    model_predict = ModelPredict()
    predictions = model_predict.predict(ecg_signal=contents)
    return predictions
