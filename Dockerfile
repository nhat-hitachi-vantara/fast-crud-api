<<<<<<< HEAD
# Dockerfile
# pull the official docker image
FROM python:3.6.9
# 
WORKDIR /code
# 
COPY ./requirements.txt /code/requirements.txt
# 
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
# 
COPY ./app /code/app
# 

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]

=======
FROM python:3.10.5
WORKDIR /usr/src/personalised_nudges
COPY ./ ./app
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
#CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
>>>>>>> 4e3ab0c3809db51945b62d5a718772bfc01bd73c
