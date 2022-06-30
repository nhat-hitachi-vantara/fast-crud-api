FROM python:3.10.5
WORKDIR /usr/src/personalised_nudges
COPY ./ ./app
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
#CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]