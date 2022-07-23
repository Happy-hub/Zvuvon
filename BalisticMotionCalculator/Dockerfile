FROM python:3.8-slim

ADD requirements.txt /
RUN python -m pip install -r requirements.txt

ADD . /BalisticMotionCalculator
WORKDIR /BalisticMotionCalculator

# RUN ["python", "Src/ba"]