FROM python:3.7-alpine

MAINTAINER Sergey Miletskiy 's.miletskiy@ukr.net'

RUN apk --update --no-cache add linux-headers gcc build-base make

COPY . /script

WORKDIR /script

RUN pip install -r requirements.txt

# CMD python /script/metrics.py
ENTRYPOINT ["python", "/script/metrics.py"]
