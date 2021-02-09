FROM python:3
EXPOSE 8000

RUN git clone https://github.com/debilmen/avito-test.git
RUN pip install -r avito-test/requirements.txt
