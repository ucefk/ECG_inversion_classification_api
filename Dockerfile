FROM python:3.9

WORKDIR /app

ADD requirements.txt .
ADD . /app

RUN pip install -r requirements.txt

CMD jupyter notebook --no-browser --NotebookApp.allow_origin_pat='*'
