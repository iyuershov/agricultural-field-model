FROM python:3.9
LABEL authors="iyuershov"

WORKDIR /server
COPY . .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

ENTRYPOINT ["tail"]
CMD ["-f","/dev/null"]