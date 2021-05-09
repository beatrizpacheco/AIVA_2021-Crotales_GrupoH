FROM python:3.8

# El directorio de trabajo es desde donde se ejecuta el contenedor al iniciarse
WORKDIR /usr/src/app

RUN apt-get update
RUN apt-get install -y libgl1-mesa-dev

RUN apt-get -y install vim

RUN apt-get -y install tesseract-ocr
RUN apt-get install tesseract-ocr-ben
ADD . /usr/src/app/tesseract-python

RUN apt-get update && \
    apt-get install -y openjdk-11-jre-headless && \
    apt-get clean;

# Fix certificate issues
RUN apt-get update && \
    apt-get install ca-certificates-java && \
    apt-get clean && \
    update-ca-certificates -f;

ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64/
RUN export JAVA_HOME

# Ejecutamos pip para instalar las dependencias en el contenedor
COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY . .

WORKDIR /usr/src/app