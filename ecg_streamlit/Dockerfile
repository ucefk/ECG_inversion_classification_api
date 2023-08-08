FROM python:3.9.16

WORKDIR /app

ADD ./ecg_streamlit /app
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 8501

CMD ["streamlit", "run", "ecg_streamlit.py"]