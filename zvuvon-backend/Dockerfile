FROM python:3.8-slim

ADD requirements.txt /
RUN python -m pip install -r requirements.txt

ADD . /Zvuvon
WORKDIR /Zvuvon

ENV PYTHONPATH=/Zvuvon

WORKDIR /Zvuvon/ZvuvonAPI/app

#CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]