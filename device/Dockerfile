FROM python:3.9-alpine
LABEL authors="iyuershov"

ADD requirements.txt /device/requirements.txt
COPY *.py /device/
WORKDIR /device
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD ["gunicorn", "main:app", "--worker-class", "uvicorn.workers.UvicornWorker", "--bind", "0.0.0.0:5555"]
