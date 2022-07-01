# Dockerfile
# pull the official docker image
FROM python:3.11-rc-bullseye
# 
WORKDIR /code
# 
COPY ./requirements.txt /code/requirements.txt
# 
RUN pip install  -r requirements.txt

# 
COPY ./app /code/app
# 

CMD ["uvicorn", "app.main:app","reload=True", "--host", "0.0.0.0", "--port", "80]

