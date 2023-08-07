FROM python:3.9

WORKDIR /app

ADD ./ecg_app/requirements.txt .
# ADD ./ecg_app/run.sh .
ADD ./ecg_app/ /app

RUN adduser --disabled-password --gecos '' ml-api-user

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

RUN chmod +x run.sh
RUN chown -R ml-api-user:ml-api-user ./

USER ml-api-user

EXPOSE 8001

CMD ["bash", "./run.sh"]
