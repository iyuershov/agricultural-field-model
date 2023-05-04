FROM python:3.9
LABEL authors="iyuershov"

WORKDIR /server
COPY . .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN echo 'alias collectdata="python3 /server/main.py"' >> ~/.bashrc

ENTRYPOINT ["tail"]
CMD ["-f","/dev/null"]