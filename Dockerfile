FROM python:3
EXPOSE 8000

RUN git clone https://github.com/debilmen/avito-test.git
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
